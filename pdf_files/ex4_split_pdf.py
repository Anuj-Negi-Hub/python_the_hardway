# Exercise 4: Split a PDF

# Goal
# Create separate PDF files for each page.

from pypdf import PdfReader, PdfWriter

reader = PdfReader(r"D:\PDFs\split_file.pdf")

for page_num in range(len(reader.pages)):
    writer = PdfWriter()

    writer.add_page(reader.pages[page_num])

    output_name = rf"D:\PDFs\page_{page_num + 1}.pdf"

    with open(output_name, "wb") as output_file:
        writer.write(output_file)

print("PDF split completed.")