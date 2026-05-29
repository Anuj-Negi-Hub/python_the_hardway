#!/usr/bin/env python3
"""
PDF Page Numbering Utility
--------------------------
This script automates adding page numbers to a PDF file.
It dynamically checks and installs its dependencies ('pypdf' and 'reportlab') if they are missing.
It supports different positions, custom margins, formats, fonts, and option to skip the cover page.
"""

import sys
import os
import subprocess
import io
import argparse

# ---------------------------------------------------------------------------
# Dependency Checker & Auto-installer
# ---------------------------------------------------------------------------
def ensure_dependencies():
    """Checks and installs required external libraries if they are missing."""
    required_packages = {
        "pypdf": "pypdf",
        "reportlab": "reportlab"
    }
    missing_packages = []
    
    for import_name, install_name in required_packages.items():
        try:
            __import__(import_name)
        except ImportError:
            missing_packages.append(install_name)
            
    if missing_packages:
        print(f"[*] Missing required packages: {', '.join(missing_packages)}")
        print("[*] Attempting to install them automatically using pip...")
        try:
            # Run pip install safely
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", *missing_packages],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT
            )
            print("[+] Successfully installed dependencies.")
        except Exception as e:
            print(f"[-] Error installing dependencies: {e}", file=sys.stderr)
            print("[-] Please install them manually using: pip install pypdf reportlab", file=sys.stderr)
            sys.exit(1)

# Ensure dependencies are available before importing them
ensure_dependencies()

# Now it is safe to import them
try:
    from pypdf import PdfReader, PdfWriter
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
except ImportError:
    print("[-] Failed to import pypdf or reportlab even after installation.", file=sys.stderr)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Core PDF Numbering Function
# ---------------------------------------------------------------------------
def add_page_numbers(
    input_path: str,
    output_path: str,
    position: str = "bottom-right",
    margin: float = 36.0,
    font_name: str = "Helvetica",
    font_size: int = 9,
    format_str: str = "Page {page} of {total}",
    skip_first: bool = False,
    start_number: int = 1
):
    """
    Adds page numbers to the given PDF file.
    
    Parameters:
        input_path: Path to the input PDF file.
        output_path: Path where the numbered PDF will be saved.
        position: Position of the text: 'bottom-right', 'bottom-center', 'bottom-left', 'top-right', 'top-center', 'top-left'.
        margin: Margin from the edge of the page in points (1 inch = 72 points).
        font_name: Font to use (default: Helvetica). Standard PDF fonts: Helvetica, Times-Roman, Courier.
        font_size: Size of the font in points.
        format_str: The text format. Supports '{page}' and '{total}'.
        skip_first: If True, skips numbering the first page (useful for covers).
        start_number: The page number to start counting from (usually 1).
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found at: {input_path}")
        
    print(f"[*] Reading: {input_path}")
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    total_pages = len(reader.pages)
    print(f"[*] Found {total_pages} pages in PDF.")
    
    # Pre-calculate totals for labeling
    # If we skip first, we might want the total pages to either be actual total or total - 1
    # We will use the actual total pages, but we can customize if needed.
    effective_total = total_pages
    
    for idx, page in enumerate(reader.pages):
        page_num = idx + 1
        
        # If skip_first is True and this is the first page, just add it unchanged
        if skip_first and page_num == 1:
            writer.add_page(page)
            continue
            
        # Calculate actual page number value to display
        display_num = page_num if not skip_first else page_num - 1
        display_num = display_num + (start_number - 1)
        
        # Format the text to draw
        text = format_str.format(page=display_num, total=effective_total)
        
        # Get page dimensions dynamically (handles mixed page sizes and orientations)
        width = float(page.mediabox.width)
        height = float(page.mediabox.height)
        
        # Draw the text onto a canvas in-memory
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=(width, height))
        can.setFont(font_name, font_size)
        can.setFillColorRGB(0.2, 0.2, 0.2)  # Sleek dark gray instead of harsh solid black
        
        # Calculate X and Y coordinates based on chosen position
        x, y = 0.0, 0.0
        
        # Determine Y coordinate
        if position.startswith("top"):
            y = height - margin - font_size
        else:  # bottom
            y = margin
            
        # Determine X coordinate and alignment
        if position.endswith("left"):
            x = margin
            can.drawString(x, y, text)
        elif position.endswith("center"):
            x = width / 2
            can.drawCentredString(x, y, text)
        else:  # right
            x = width - margin
            can.drawRightString(x, y, text)
            
        can.save()
        packet.seek(0)
        
        # Load the newly created single-page PDF containing only the page number
        number_pdf = PdfReader(packet)
        number_page = number_pdf.pages[0]
        
        # Overlay the page number onto the original page
        page.merge_page(number_page)
        writer.add_page(page)
        
        print(f"[+] Processed page {page_num}/{total_pages}")
        
    print(f"[*] Writing output to: {output_path}")
    # Ensure directory of output path exists
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
        
    with open(output_path, "wb") as f:
        writer.write(f)
        
    print("[+] Page numbering completed successfully!")


# ---------------------------------------------------------------------------
# CLI Argument Parsing
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="A utility to add page numbers to a PDF file.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "-i", "--input",
        type=str,
        required=True,
        help="Path to the input PDF file"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="Path to the output PDF file (defaults to input file with '_numbered' suffix)"
    )
    parser.add_argument(
        "-p", "--position",
        type=str,
        choices=["bottom-right", "bottom-center", "bottom-left", "top-right", "top-center", "top-left"],
        default="bottom-right",
        help="Position to place the page numbers"
    )
    parser.add_argument(
        "-m", "--margin",
        type=float,
        default=36.0,
        help="Margin from the edge of the page in points (72 points = 1 inch)"
    )
    parser.add_argument(
        "-f", "--format",
        type=str,
        default="Page {page} of {total}",
        help="Format string for the page numbers. Use '{page}' and '{total}' as placeholders."
    )
    parser.add_argument(
        "--skip-first",
        action="store_true",
        help="Skip adding page number to the first page (cover page)"
    )
    parser.add_argument(
        "--start-number",
        type=int,
        default=1,
        help="The page number to start counting from"
    )
    parser.add_argument(
        "--font",
        type=str,
        default="Helvetica",
        help="Standard font to use (Helvetica, Times-Roman, Courier)"
    )
    parser.add_argument(
        "--size",
        type=int,
        default=9,
        help="Font size in points"
    )

    args = parser.parse_args()

    # Deduce output file path if not provided
    if not args.output:
        base, ext = os.path.splitext(args.input)
        args.output = f"{base}_numbered{ext}"

    try:
        add_page_numbers(
            input_path=args.input,
            output_path=args.output,
            position=args.position,
            margin=args.margin,
            font_name=args.font,
            font_size=args.size,
            format_str=args.format,
            skip_first=args.skip_first,
            start_number=args.start_number
        )
    except Exception as e:
        print(f"[-] Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
