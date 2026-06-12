from io import BytesIO

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

# This code is going write page numbers to the pages.

input_pdf = "dita_reference.pdf"
output_pdf = "dita_reference_with_page_numbers.pdf"

reader = PdfReader(input_pdf) # reading the pdf
# reader is containing the input_pdf , PdfReader Object
# Every type is actually a class, 
# print(type(reader))
# x = 5
# print(type(x))
# x = float(x)
# x.as_integer_ratio()
# class was keeping both data + action  that we can on the data.

writer = PdfWriter() # writing the pages 
total_pages = len(reader.pages) # VirtualList
# print(type(reader.pages))
# print(type(total_pages))

# x1 = {"pages":[], "data": 17}

# print(x1["pages"]) # []

# x1["pages"].append()

for page_num in range(total_pages):
    page = reader.pages[page_num] #list[0]
    # reader.pages.append()
    #Create an in-memory PDf containing the page number

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

    writer.add_page(page) # writer is storing or adding pages to page variable

# Save final PDF
with open(output_pdf, "wb") as output_file:
    writer.write(output_file)

print("Page numbers added successfully!")
