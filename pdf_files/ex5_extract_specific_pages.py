'''
Exercise 6: Extract Specific Pages

Goal
    Create a new PDF containing only selected pages.

Example:
Save only pages 1 and 3.
'''


from pypdf import PdfReader, PdfWriter

reader = PdfReader("Microsoft Manual of Style, Fourth Edition eBook.pdf")
# reader = PdfReader(r"D:\PDFs\Microsoft Manual of Style, Fourth Edition eBook.pdf")
writer = PdfWriter()

writer.add_page(reader.pages[1])
writer.add_page(reader.pages[5])
writer.add_page(reader.pages[8])

output_file = "specific_pages.pdf"
# output_file = r"D:\PDFs\specific_pages.pdf"



with open (output_file, "wb") as file:
    writer.write(file)


