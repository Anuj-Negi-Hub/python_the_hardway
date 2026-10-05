#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import time
import fitz  # PyMuPDF
from pathlib import Path
from typing import List, Dict


# ------------------------------------------------------------
# 0. Page Detection Patterns (STRICT VERSION)
# ------------------------------------------------------------

# TOC: Digit.Digit ... Digit-Digit
TOC_LINE_PATTERN = re.compile(
    r"^\s*\d+(?:\.\d+)*\s+.+?\s+[\.\u2022]{2,}\s*\d+[-]\d+\s*$", re.X
)

# LOF: Figure X-X ... Digit-Digit
LOF_LINE_PATTERN = re.compile(
    r"^\s*Figure\s+\d+[-]\d+.*?\s+[\.\u2022]{2,}\s*\d+[-]\d+\s*$", re.I
)

# LOT: Table X-X ... Digit-Digit
LOT_LINE_PATTERN = re.compile(
    r"^\s*Table\s+\d+[-]\d+.*?\s+[\.\u2022]{2,}\s*\d+[-]\d+\s*$", re.I
)

# LOE: Example X-X ... Digit-Digit
LOE_LINE_PATTERN = re.compile(
    r"^\s*Example\s+\d+[-]\d+.*?\s+[\.\u2022]{2,}\s*\d+[-]\d+\s*$", re.I
)


def detect_section_pages(doc: fitz.Document, key: str) -> List[int]:
    """Detects a block of pages for TOC, LOF, LOT, or LOE."""
    start = None

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

    # 1. Search for Heading (Highest Confidence)
    for i in range(min(len(doc), 200)):
        text = doc[i].get_text()
        if headings[key].search(text):
            start = i
            break

    # 2. Fallback to Strict Pattern Match
    if start is None:
        entry_pat = patterns[key]
        for i in range(min(len(doc), 200)):
            lines = [ln for ln in doc[i].get_text().splitlines() if ln.strip()]
            if not lines: continue
            # MIN MATCH = 1 (as requested), but pattern is now very strict
            if any(entry_pat.search(ln) for ln in lines):
                start = i
                break

    if start is None: return []

    # 3. Determine block length
    block = [start]
    for j in range(start + 1, min(len(doc), 200)):
        text = doc[j].get_text()
    
        # Stop immediately if "Chapter X" appears at the top of the page
        first_lines = text.splitlines()[:5]
        if any(re.search(r"^\s*Chapter\s+\d+", ln, re.I) for ln in first_lines):
            break

        # Stop if another section heading is found
        if any(headings[k].search(text) for k in headings if k != key):
            break

        # Stop if the page contains no lines matching the strict pattern
        lines = [ln for ln in text.splitlines() if ln.strip()]
        if not lines or not any(patterns[key].search(ln) for ln in lines):
            break

        block.append(j)
    return block

# ------------------------------------------------------------
# 1 Core Combined Merging Routine
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
    for idx, filename in enumerate(pdf_files):
        path = folder / filename
        src = fitz.open(path)
        sections = {
            "toc": detect_section_pages(src, "toc"),
            "lof": detect_section_pages(src, "lof"),
            "lot": detect_section_pages(src, "lot"),
            "loe": detect_section_pages(src, "loe"),
        }

        front_pages = set().union(*sections.values())
        content_pages = [i for i in range(len(src)) if i not in front_pages]

        file_data.append({
            "doc": src,
            "sections": sections,
            "content_pages": content_pages,
            "src_toc": src.get_toc(),
            "filename": filename
        })


    # --- PHASE 2: PHYSICAL PAGE CONSTRUCTION ---
    current_final_pg = 0


    def insert_pages(doc_obj, indices, f_idx):
        nonlocal current_final_pg
        for p_idx in indices:
            merged_doc.insert_pdf(doc_obj, from_page=p_idx, to_page=p_idx)
            page_map[(f_idx, p_idx)] = current_final_pg + 1
            current_final_pg += 1


    base = file_data[0]
    toc_start = base["sections"]["toc"][0] if base["sections"]["toc"] else 0

    insert_pages(base["doc"], list(range(0, toc_start)), 0)   

    for f_idx, data in enumerate(file_data):
        insert_pages(data["doc"], data["sections"]["toc"], f_idx)   

    for f_idx, data in enumerate(file_data):
        insert_pages(data["doc"], data["sections"]["lof"], f_idx)

    for f_idx, data in enumerate(file_data):
        insert_pages(data["doc"], data["sections"]["lot"], f_idx)

    for f_idx, data in enumerate(file_data):
        insert_pages(data["doc"], data["sections"]["loe"], f_idx)


    base_front_set = set().union(*base["sections"].values())
    base_remaining = [i for i in range(len(base["doc"])) if i not in base_front_set and i >= toc_start]
    insert_pages(base["doc"], base_remaining, 0)


    for f_idx, data in enumerate(file_data):
        data = file_data[f_idx]
        insert_pages(data["doc"], data["content_pages"], f_idx)


    # --- PHASE 3: BOOKMARK REORDERING ---
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
        special_list = []
        for t in target_seq:
            if t in special_bookmarks: special_list.append(special_bookmarks[t])
        reordered_toc = special_list + remaining_toc

    if root_bookmark:
        reordered_toc.insert(0, [1, root_bookmark, 1])

    merged_doc.set_toc(reordered_toc)

    output_path = folder / output_name
    merged_doc.save(output_path, garbage=2, deflate=True)

    for data in file_data: data["doc"].close()
    merged_doc.close()

    print(f"\n☑ Success! PDF saved to: {output_path}")
    print(f"Total time: {time.time() - start_time:.2f}s")

if __name__ == "__main__":
    f_path = input("Enter folder path: ").strip()
    o_name = input("Enter output file name: ").strip()
    if not o_name.lower().endswith(".pdf"): o_name += ".pdf"
    r_name = input("Enter top-level bookmark title (Enter to skip): ").strip() or None

    merge_pdfs_advanced_fitz(f_path, o_name, r_name)