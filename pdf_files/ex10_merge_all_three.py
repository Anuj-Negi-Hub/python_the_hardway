from io import BytesIO
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

input_pdf = "Microsoft Manual of Style, Fourth Edition eBook.pdf"

reader = PdfReader(input_pdf)

total_pages = len(reader.pages)
pages_per_part = total_pages // 3

# ------------------------------------
# STEP 1: Split into 3 PDFs
# ------------------------------------

for part_num in range(3):

    writer = PdfWriter()

    start_page = part_num * pages_per_part

    if part_num == 2:
        end_page = total_pages
    else:
        end_page = start_page + pages_per_part

    for pdf_page_num in range(start_page, end_page):
        writer.add_page(reader.pages[pdf_page_num])

    output_file = f"part_{part_num + 1}.pdf"

    with open(output_file, "wb") as file:
        writer.write(file)

    print(f"Created: {output_file}")

# ------------------------------------
# STEP 2: Jumble and merge PDFs
# ------------------------------------

jumbled_parts = [
    "part_2.pdf",
    "part_1.pdf",
    "part_3.pdf"
]

merged_writer = PdfWriter()

for pdf_file in jumbled_parts:

    part_reader = PdfReader(pdf_file)

    for page in part_reader.pages:
        merged_writer.add_page(page)

with open("merged_jumbled.pdf", "wb") as file:
    merged_writer.write(file)

print("Created: merged_jumbled.pdf")

# ------------------------------------
# STEP 3: Add new page numbering
# ------------------------------------

reader = PdfReader("merged_jumbled.pdf")
writer = PdfWriter()

page_number = 1

for page in reader.pages:

    packet = BytesIO()

    c = canvas.Canvas(packet)

    c.drawString(460, 20, f"Page - {page_number}")

    c.save()

    packet.seek(0)

    overlay_pdf = PdfReader(packet)
    overlay_page = overlay_pdf.pages[0]

    page.merge_page(overlay_page)

    writer.add_page(page)

    page_number += 1

with open("final_output.pdf", "wb") as file:
    writer.write(file)

print("Created: final_output.pdf")