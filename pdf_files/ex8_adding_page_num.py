from io import BytesIO

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

input_pdf = "dita_reference.pdf"
output_pdf = "dita_reference_with_page_numbers.pdf"

reader =PdfReader(input_pdf)
writer = PdfWriter()


total_pages = len(reader.pages)

for page_num in range(total_pages):
    page = reader.pages[page_num]

    #Create an in-memory PDf containing th epage number

    packet = BytesIO()

    c = canvas.Canvas(packet)

    # x, y coordinates
    c.drawString(
        270,            # horizontal position
        20,             # Vertical position
        f"Page {page_num + 1}"
    )

    c.save()

    # Move to start of memory buffer
    packet.seek(0)

    # read the page-number PDF
    overlay_pdf = PdfReader(packet)

    # Merge page number onto original page
    page.merge_page(overlay_pdf.pages[0])

    writer.add_page(page)

# Save final PDF
with open(output_pdf, "wb") as output_file:
    writer.write(output_file)

print("Page numbers added successfully!")
