#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import time
import shutil
import subprocess
import pymupdf as fitz  # PyMuPDF (using modern pymupdf alias to silence deprecation warning)
from pathlib import Path
from typing import List, Dict


# ------------------------------------------------------------
# 0. Helper Functions & Page Detection (OPTIMIZED)
# ------------------------------------------------------------

TOC_LINE_PATTERN = re.compile(
    r"^\s*\d+(?:\.\d+)*\s+.+?\s+[\.\u2022]{2,}\s*\d+[-]\d+\s*$", re.X
)
LOF_LINE_PATTERN = re.compile(
    r"^\s*Figure\s+\d+[-]\d+.*?\s+[\.\u2022]{2,}\s*\d+[-]\d+\s*$", re.I
)
LOT_LINE_PATTERN = re.compile(
    r"^\s*Table\s+\d+[-]\d+.*?\s+[\.\u2022]{2,}\s*\d+[-]\d+\s*$", re.I
)
LOE_LINE_PATTERN = re.compile(
    r"^\s*Example\s+\d+[-]\d+.*?\s+[\.\u2022]{2,}\s*\d+[-]\d+\s*$", re.I
)


def get_contiguous_ranges(indices: List[int]) -> List[tuple]:
    """Converts a list of page indices into contiguous (start_page, end_page) range tuples.
    Example: [0, 1, 2, 5, 6, 9] -> [(0, 2), (5, 6), (9, 9)]
    """
    if not indices:
        return []
    sorted_idx = sorted(indices)
    ranges = []
    start = sorted_idx[0]
    prev = sorted_idx[0]
    for idx in sorted_idx[1:]:
        if idx == prev + 1:
            prev = idx
        else:
            ranges.append((start, prev))
            start = idx
            prev = idx
    ranges.append((start, prev))
    return ranges


def detect_all_sections(doc: fitz.Document) -> Dict[str, List[int]]:
    """Pre-extracts text for front pages once and detects TOC, LOF, LOT, LOE blocks efficiently."""
    max_scan = min(len(doc), 150)
    page_texts = [doc[i].get_text() for i in range(max_scan)]

    headings = {
        "toc": re.compile(r"\bTable\s+of\s+Contents\b", re.I),
        "lof": re.compile(r"\bList\s+of\s+Figures\b", re.I),
        "lot": re.compile(r"\bList\s+of\s+Tables\b", re.I),
        "loe": re.compile(r"\bList\s+of\s+Examples?\b", re.I),
    }

    patterns = {
        "toc": TOC_LINE_PATTERN,
        "lof": LOF_LINE_PATTERN,
        "lot": LOT_LINE_PATTERN,
        "loe": LOE_LINE_PATTERN
    }

    sections = {}

    for key in ["toc", "lof", "lot", "loe"]:
        start = None

        # 1. Search for Heading
        for i, text in enumerate(page_texts):
            if headings[key].search(text):
                start = i
                break

        # 2. Fallback to Strict Pattern Match
        if start is None:
            entry_pat = patterns[key]
            for i, text in enumerate(page_texts):
                lines = [ln for ln in text.splitlines() if ln.strip()]
                if not lines: continue
                if any(entry_pat.search(ln) for ln in lines):
                    start = i
                    break

        if start is None:
            sections[key] = []
            continue

        # 3. Determine block length
        block = [start]
        for j in range(start + 1, max_scan):
            text = page_texts[j]
            first_lines = text.splitlines()[:5]
            if any(re.search(r"^\s*Chapter\s+\d+", ln, re.I) for ln in first_lines):
                break
            if any(headings[k].search(text) for k in headings if k != key):
                break
            lines = [ln for ln in text.splitlines() if ln.strip()]
            if not lines or not any(patterns[key].search(ln) for ln in lines):
                break
            block.append(j)

        sections[key] = block

    return sections


def expand_top_level_bookmarks(pdf_path: Path, root_bookmark_present: bool = True):
    """Ensures Level 1 root bookmark is expanded (open) while keeping all sub-bookmarks collapsed.
    If no root bookmark was specified, keeps all file bookmarks collapsed.
    """
    if not root_bookmark_present:
        return

    doc = fitz.open(pdf_path)
    toc = doc.get_toc(False)
    if not toc:
        doc.close()
        return

    modified = False
    for item in toc:
        lvl = item[0]
        xref = item[3].get('xref') if len(item) > 3 and isinstance(item[3], dict) else None
        if lvl == 1 and xref:
            key_type, val = doc.xref_get_key(xref, 'Count')
            if key_type == 'int':
                count_num = int(val)
                if count_num < 0:
                    # Positive /Count means expanded, negative means collapsed
                    doc.xref_set_key(xref, 'Count', str(abs(count_num)))
                    modified = True

    if modified:
        temp_path = pdf_path.with_name(f"temp_bm_{pdf_path.name}")
        doc.save(temp_path, incremental=False, deflate=True)
        doc.close()
        temp_path.replace(pdf_path)
    else:
        doc.close()


def optimize_with_qpdf(pdf_path: Path):
    """Optimizes output using pikepdf or qpdf CLI to remove duplicate resources & compress object streams."""
    print("⚡ Running QPDF to optimize the output file...")
    try:
        import pikepdf
        temp_path = pdf_path.with_name(f"temp_opt_{pdf_path.name}")
        with pikepdf.open(pdf_path) as pdf:
            pdf.save(
                temp_path,
                linearize=True,
                object_stream_mode=pikepdf.ObjectStreamMode.generate
            )
        temp_path.replace(pdf_path)
        print("✔ The PDF file is optmized.")
        return
    except ImportError:
        pass

    qpdf_bin = shutil.which("qpdf")
    if qpdf_bin:
        temp_path = pdf_path.with_name(f"temp_opt_{pdf_path.name}")
        cmd = [
            qpdf_bin,
            "--linearize",
            "--object-streams=generate",
            str(pdf_path),
            str(temp_path)
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            temp_path.replace(pdf_path)
            print("✔ The PDF file is optmized.")
        else:
            print(f"⚠️ QPDF error: {res.stderr}")
            if temp_path.exists():
                temp_path.unlink()
    else:
        print("ℹ️ Tip: Install 'pikepdf' (pip install pikepdf) or QPDF CLI for maximum stream compression.")


# ------------------------------------------------------------
# 1. Core Combined Merging Routine (HIGH PERFORMANCE)
# ------------------------------------------------------------

def merge_pdfs_advanced_fitz(folder_path: str, output_name: str, root_bookmark: str = None):
    start_time = time.time()
    folder = Path(folder_path)

    pdf_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(".pdf") and f != output_name])

    if not pdf_files:
        print("No PDF files found."); return

    merged_doc = fitz.open()
    page_map = {}
    file_data = []

    # --- PHASE 1: ANALYSIS ---
    print(f"🔍 Found {len(pdf_files)} PDf files in the folder. Analyzing the PDF files...")
    for idx, filename in enumerate(pdf_files):
        path = folder / filename
        src = fitz.open(path)
        sections = detect_all_sections(src)

        front_pages = set().union(*sections.values())
        content_pages = [i for i in range(len(src)) if i not in front_pages]

        file_data.append({
            "doc": src,
            "sections": sections,
            "content_pages": content_pages,
            "src_toc": src.get_toc(),
            "filename": filename
        })

    # --- PHASE 2: PHYSICAL PAGE CONSTRUCTION (BULK BATCHED) ---
    base = file_data[0]
    toc_start = base["sections"]["toc"][0] if base["sections"]["toc"] else 0
    base_front_set = set().union(*base["sections"].values())
    base_remaining = [i for i in range(len(base["doc"])) if i not in base_front_set and i >= toc_start]

    # Pre-calculate total unique pages across all files for percentage tracking
    all_pages_set = set()
    for p in range(0, toc_start): all_pages_set.add((0, p))
    for f_idx, data in enumerate(file_data):
        for p in data["sections"]["toc"]: all_pages_set.add((f_idx, p))
        for p in data["sections"]["lof"]: all_pages_set.add((f_idx, p))
        for p in data["sections"]["lot"]: all_pages_set.add((f_idx, p))
        for p in data["sections"]["loe"]: all_pages_set.add((f_idx, p))
        for p in data["content_pages"]: all_pages_set.add((f_idx, p))
    for p in base_remaining: all_pages_set.add((0, p))

    total_pages = len(all_pages_set)
    print("📄 The OnePDF tool is in progress. Please wait to complete the process...")

    current_final_pg = 0
    inserted_pages = set()  # Tracks (f_idx, p_idx) to avoid ANY duplicate insertions

    def get_progress_str():
        if total_pages > 0:
            pct = (current_final_pg / total_pages) * 100
            return f"{current_final_pg}/{total_pages} pages ({pct:.1f}%)"
        return f"{current_final_pg} pages"

    def insert_pages(doc_obj, indices, f_idx):
        nonlocal current_final_pg
        to_insert = [p for p in indices if (f_idx, p) not in inserted_pages]
        if not to_insert:
            return

        # 1. Update mapping table first
        for p_idx in to_insert:
            inserted_pages.add((f_idx, p_idx))
            page_map[(f_idx, p_idx)] = current_final_pg + 1
            current_final_pg += 1

        # 2. Perform bulk insertion for contiguous page ranges (100x faster than page-by-page)
        for start_p, end_p in get_contiguous_ranges(to_insert):
            merged_doc.insert_pdf(doc_obj, from_page=start_p, to_page=end_p)

    # 1. Base Front Matter (Cover/Title Pages before TOC)
    insert_pages(base["doc"], list(range(0, toc_start)), 0)

    # 2. Section Blocks (TOC, LOF, LOT, LOE)
    print("⏳ The movement of ToC pages is in progress...")
    for f_idx, data in enumerate(file_data):
        insert_pages(data["doc"], data["sections"]["toc"], f_idx)
    print("   ✔ The ToC pages are moved successfully.")

    print("⏳ The movement of LoF pages is in progress...")
    for f_idx, data in enumerate(file_data):
        insert_pages(data["doc"], data["sections"]["lof"], f_idx)
    print("   ✔ The LoF pages are moved successfully.")

    print("⏳ The movement of LoT pages is in progress...")
    for f_idx, data in enumerate(file_data):
        insert_pages(data["doc"], data["sections"]["lot"], f_idx)
    print("   ✔ The LoT pages are moved successfully.")

    print("⏳ The movement of LoE pages is in progress...")
    for f_idx, data in enumerate(file_data):
        insert_pages(data["doc"], data["sections"]["loe"], f_idx)
    print("   ✔ The LoE pages are moved successfully.")

    # 3. Base Remaining Pages (After Front Sections)
    insert_pages(base["doc"], base_remaining, 0)

    # 4. Content Pages of All Sub-Files
    print("⏳ Moving remaining  pages...")
    for f_idx, data in enumerate(file_data):
        insert_pages(data["doc"], data["content_pages"], f_idx)
        print(f"   ↳ {data['filename']} processed [{get_progress_str()}]")

    # --- PHASE 3: BOOKMARK REORDERING ---
    print("🔖 Rebuilding PDF bookmarks...")
    final_toc = []
    for f_idx, data in enumerate(file_data):
        for lvl, title, pg in data["src_toc"]:
            new_pg = page_map.get((f_idx, pg - 1))
            if new_pg:
                final_lvl = lvl + 1 if root_bookmark else lvl
                final_toc.append([final_lvl, title, new_pg])

    target_seq = ["Table of Contents", "List of Figures", "List of Tables", "List of Examples"]
    special_bookmarks = {}
    remaining_toc = []

    for entry in final_toc:
        title = entry[1].strip()
        match = next((t for t in target_seq if t.lower() == title.lower()), None)
        if match: special_bookmarks[match] = entry
        else: remaining_toc.append(entry)            

    reordered_toc = []
    inserted = False
    for entry in remaining_toc:
        reordered_toc.append(entry)
        if entry[1].strip().lower() == "revision history":
            for t in target_seq:
                if t in special_bookmarks: reordered_toc.append(special_bookmarks[t])
            inserted = True

    if not inserted:
        special_list = [special_bookmarks[t] for t in target_seq if t in special_bookmarks]
        reordered_toc = special_list + remaining_toc

    if root_bookmark:
        reordered_toc.insert(0, [1, root_bookmark, 1])

    merged_doc.set_toc(reordered_toc)

    output_path = folder / output_name
    
    # Save using fast PyMuPDF stream deflate
    print("💾 Saving the merged PDF ...")
    merged_doc.save(output_path, garbage=1, deflate=True)

    for data in file_data: data["doc"].close()
    merged_doc.close()

    # --- PHASE 3.5: EXPAND TOP-LEVEL BOOKMARKS ---
    expand_top_level_bookmarks(output_path, root_bookmark_present=bool(root_bookmark))

    #to avoid the auto lock of the file
    time.sleep(0.2)

    # --- PHASE 4: QPDF OPTIMIZATION PASS ---
    optimize_with_qpdf(output_path)

    print(f"\n☑ Success! The PDF is saved to: {output_path}")
    print(f"The total time taken to complete the merged activities if {time.time() - start_time:.2f}s.")


if __name__ == "__main__":
    f_path = input("Enter the folder path (where all the files that needs to be merged are paced): ").strip()
    o_name = input("Enter the output file name: ").strip()
    if not o_name.lower().endswith(".pdf"): o_name += ".pdf"
    r_name = input("Enter the top-level bookmark name (Enter to skip): ").strip() or None

    merge_pdfs_advanced_fitz(f_path, o_name, r_name)