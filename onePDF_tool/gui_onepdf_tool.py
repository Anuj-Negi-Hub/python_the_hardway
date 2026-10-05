#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import time
import threading
import queue
from pathlib import Path
from typing import List, Dict

import pypdf
from pypdf import PdfReader, PdfWriter

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext


# ------------------------------------------------------------
# 0. Helper Functions & Page Detection
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


def extract_toc_pypdf(reader: PdfReader) -> List[List]:
    """Extract outline/bookmarks as [[level, title, 1_indexed_page], ...]"""
    toc = []
    def parse_items(items, level=1):
        i = 0
        while i < len(items):
            item = items[i]
            if isinstance(item, list):
                parse_items(item, level + 1)
            else:
                try:
                    title = str(item.title)
                    pg_num = reader.get_destination_page_number(item)
                    if pg_num is not None:
                        toc.append([level, title, pg_num + 1])
                except Exception:
                    pass
            i += 1
    if reader.outline:
        parse_items(reader.outline, 1)
    return toc


def detect_all_sections(reader: PdfReader) -> Dict[str, List[int]]:
    max_scan = min(len(reader.pages), 150)
    page_texts = []
    for i in range(max_scan):
        try:
            txt = reader.pages[i].extract_text() or ""
        except Exception:
            txt = ""
        page_texts.append(txt)

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
        for i, text in enumerate(page_texts):
            if headings[key].search(text):
                start = i
                break

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

        block = [start]
        for j in range(start + 1, max_scan):
            text = page_texts[j]
            if any(headings[k].search(text) for k in headings if k != key):
                break
            lines = [ln for ln in text.splitlines() if ln.strip()]
            if not lines or not any(patterns[key].search(ln) for ln in lines):
                break
            block.append(j)

        sections[key] = block

    return sections


def merge_pdfs_advanced_pypdf(folder_path: str, output_name: str, root_bookmark: str = None):
    start_time = time.time()
    folder = Path(folder_path)

    pdf_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(".pdf") and f != output_name])

    if not pdf_files:
        print("No PDF files found."); return

    writer = PdfWriter()
    page_map = {}
    file_data = []

    print(f"🔍 Found {len(pdf_files)} PDF files in the folder. Analyzing the PDF files...")
    for idx, filename in enumerate(pdf_files):
        path = folder / filename
        reader = PdfReader(path)
        sections = detect_all_sections(reader)
        src_toc = extract_toc_pypdf(reader)

        front_pages = set().union(*sections.values())
        content_pages = [i for i in range(len(reader.pages)) if i not in front_pages]

        file_data.append({
            "reader": reader,
            "sections": sections,
            "content_pages": content_pages,
            "src_toc": src_toc,
            "filename": filename
        })

    base = file_data[0]
    toc_start = base["sections"]["toc"][0] if base["sections"]["toc"] else 0
    base_front_set = set().union(*base["sections"].values())
    base_remaining = [i for i in range(len(base["reader"].pages)) if i not in base_front_set and i >= toc_start]

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
    inserted_pages = set()

    def get_progress_str():
        if total_pages > 0:
            pct = (current_final_pg / total_pages) * 100
            return f"{current_final_pg}/{total_pages} pages ({pct:.1f}%)"
        return f"{current_final_pg} pages"

    def insert_pages(reader_obj, indices, f_idx):
        nonlocal current_final_pg
        to_insert = [p for p in indices if (f_idx, p) not in inserted_pages]
        if not to_insert:
            return

        for p_idx in to_insert:
            inserted_pages.add((f_idx, p_idx))
            page_map[(f_idx, p_idx)] = current_final_pg + 1
            current_final_pg += 1
            writer.add_page(reader_obj.pages[p_idx])

    insert_pages(base["reader"], list(range(0, toc_start)), 0)

    print("⏳ The movement of ToC pages is in progress...")
    for f_idx, data in enumerate(file_data):
        insert_pages(data["reader"], data["sections"]["toc"], f_idx)
    print("   ✔ The ToC pages are moved successfully.")

    print("⏳ The movement of LoF pages is in progress...")
    for f_idx, data in enumerate(file_data):
        insert_pages(data["reader"], data["sections"]["lof"], f_idx)
    print("   ✔ The LoF pages are moved successfully.")

    print("⏳ The movement of LoT pages is in progress...")
    for f_idx, data in enumerate(file_data):
        insert_pages(data["reader"], data["sections"]["lot"], f_idx)
    print("   ✔ The LoT pages are moved successfully.")

    print("⏳ The movement of LoE pages is in progress...")
    for f_idx, data in enumerate(file_data):
        insert_pages(data["reader"], data["sections"]["loe"], f_idx)
    print("   ✔ The LoE pages are moved successfully.")

    insert_pages(base["reader"], base_remaining, 0)

    print("⏳ Moving remaining pages...")
    for f_idx, data in enumerate(file_data):
        insert_pages(data["reader"], data["content_pages"], f_idx)
        print(f"   ↳ {data['filename']} processed [{get_progress_str()}]")

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

    # Rebuild outline hierarchy in pypdf
    parent_stack = {0: None}
    for lvl, title, page_1idx in reordered_toc:
        pg_0idx = max(0, page_1idx - 1)
        parent = parent_stack.get(lvl - 1)
        is_expanded = (lvl == 1)
        try:
            new_item = writer.add_outline_item(title, pg_0idx, parent=parent, expanded=is_expanded)
            parent_stack[lvl] = new_item
        except Exception as e:
            print(f"   ⚠ Warning building bookmark '{title}': {e}")

    output_path = folder / output_name
    print("💾 Saving the merged PDF ...")
    with open(output_path, "wb") as f_out:
        writer.write(f_out)

    print(f"\n☑ Success! The PDF is saved to: {output_path}")
    print(f"The total time taken to complete the merged activities is {time.time() - start_time:.2f}s.")


# ------------------------------------------------------------
# 1. Tkinter GUI Application
# ------------------------------------------------------------

class TextRedirector:
    """Redirects stdout / stderr to a tkinter Text widget."""
    def __init__(self, widget, queue):
        self.widget = widget
        self.queue = queue

    def write(self, str_val):
        self.queue.put(str_val)

    def flush(self):
        pass


class OnePDFToolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("OnePDF Tool")
        self.root.geometry("750x600")
        self.root.minsize(680, 520)

        # Apply Modern Styling
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Color Palette
        self.bg_color = "#f4f6f9"
        self.header_bg = "#1e293b"
        self.header_fg = "#ffffff"

        self.root.configure(bg=self.bg_color)
        self.log_queue = queue.Queue()

        self.create_widgets()
        self.root.after(100, self.process_log_queue)

    def create_widgets(self):
        # Header Banner
        header = tk.Frame(self.root, bg=self.header_bg, padx=15, pady=15)
        header.pack(fill=tk.X)

        title_lbl = tk.Label(
            header,
            text="OnePDF Tool",
            font=("Segoe UI", 18, "bold"),
            bg=self.header_bg,
            fg=self.header_fg
        )
        title_lbl.pack(anchor="w")

        subtitle_lbl = tk.Label(
            header,
            text="Automated PDF Merging, Section Reordering & Bookmark Management",
            font=("Segoe UI", 10),
            bg=self.header_bg,
            fg="#94a3b8"
        )
        subtitle_lbl.pack(anchor="w")

        # Main Card Frame
        main_frame = tk.Frame(self.root, bg=self.bg_color, padx=20, pady=15)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Inputs Card Box
        input_box = ttk.LabelFrame(main_frame, text=" File & Folder Settings ", padding=12)
        input_box.pack(fill=tk.X, pady=(0, 10))

        # Folder Path Entry
        ttk.Label(input_box, text="PDF Folder Path:", font=("Segoe UI", 9, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        self.path_entry = ttk.Entry(input_box, width=52)
        self.path_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.browse_btn = ttk.Button(input_box, text="Browse Folder...", command=self.browse_path)
        self.browse_btn.grid(row=0, column=2, padx=5, pady=5)

        # Output Name Entry
        ttk.Label(input_box, text="Output File Name:", font=("Segoe UI", 9, "bold")).grid(row=1, column=0, sticky="w", pady=5)
        self.out_entry = ttk.Entry(input_box, width=52)
        self.out_entry.insert(0, "merged_output.pdf")
        self.out_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Bookmark Title Entry
        ttk.Label(input_box, text="Top-Level Bookmark Title:", font=("Segoe UI", 9)).grid(row=2, column=0, sticky="w", pady=5)
        self.bm_entry = ttk.Entry(input_box, width=52)
        self.bm_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        ttk.Label(input_box, text="(Optional)", font=("Segoe UI", 8), foreground="#64748b").grid(row=2, column=2, sticky="w")

        input_box.columnconfigure(1, weight=1)

        # Action Button Box
        action_frame = tk.Frame(main_frame, bg=self.bg_color)
        action_frame.pack(fill=tk.X, pady=(0, 10))

        self.start_btn = tk.Button(
            action_frame,
            text="▶ MERGE PDFS NOW",
            font=("Segoe UI", 11, "bold"),
            bg="#0284c7",
            fg="#ffffff",
            activebackground="#0369a1",
            activeforeground="#ffffff",
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2",
            command=self.start_processing
        )
        self.start_btn.pack(side=tk.LEFT)

        # Log & Output Box
        log_box = ttk.LabelFrame(main_frame, text=" Real-Time Process Output ", padding=10)
        log_box.pack(fill=tk.BOTH, expand=True)

        self.log_text = scrolledtext.ScrolledText(
            log_box,
            font=("Consolas", 9),
            bg="#0f172a",
            fg="#f8fafc",
            insertbackground="#ffffff",
            wrap=tk.WORD,
            state="disabled",
            height=12
        )
        self.log_text.pack(fill=tk.BOTH, expand=True)

    def browse_path(self):
        folder = filedialog.askdirectory(title="Select Folder Containing PDF Files")
        if folder:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, folder)

    def append_log(self, text):
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, text)
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")

    def process_log_queue(self):
        while not self.log_queue.empty():
            msg = self.log_queue.get_nowait()
            self.append_log(msg)
        self.root.after(100, self.process_log_queue)

    def start_processing(self):
        path = self.path_entry.get().strip()
        out_name = self.out_entry.get().strip()
        bm_name = self.bm_entry.get().strip() or None

        if not path or not os.path.exists(path):
            messagebox.showwarning("Invalid Input", "Please select a valid folder path containing PDF files.")
            return

        if not out_name.lower().endswith(".pdf"):
            out_name += ".pdf"

        self.start_btn.config(state="disabled", text="⏳ PROCESSING...")
        
        # Clear previous log
        self.log_text.config(state="normal")
        self.log_text.delete("1.0", tk.END)
        self.log_text.config(state="disabled")

        # Run background worker thread
        thread = threading.Thread(
            target=self.worker_thread,
            args=(path, out_name, bm_name),
            daemon=True
        )
        thread.start()

    def worker_thread(self, path, out_name, bm_name):
        old_stdout = sys.stdout
        sys.stdout = TextRedirector(self.log_text, self.log_queue)
        try:
            merge_pdfs_advanced_pypdf(path, out_name, bm_name)
        except Exception as e:
            print(f"\n❌ Error encountered during processing:\n{e}")
        finally:
            sys.stdout = old_stdout
            self.root.after(0, lambda: self.start_btn.config(state="normal", text="▶ MERGE PDFS NOW"))


def main():
    root = tk.Tk()
    app = OnePDFToolGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
