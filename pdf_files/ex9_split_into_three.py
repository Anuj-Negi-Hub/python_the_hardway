'''
Split the pdf files into 3 parts. Ensure you keep all the extra pages in the last part'''

from io import BytesIO
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

input_pdf = "Microsoft Manual of Style, Fourth Edition eBook.pdf"

reader = PdfReader(input_pdf)
pages = reader.pages
# print(type(pages))

total_pages = len(reader.pages)
# print(page_count)

#calculates pages per parts
pages_per_part = total_pages // 3

for page_num in range(3):
    writer = PdfWriter()

    start_page = page_num * pages_per_part

    #last parts gets remaining pages
    if page_num == 2:
        end_page = total_pages
    else:
        end_page = start_page + pages_per_part
    
    #page numbering from this part start from 1
    page_number = 1
        
    for pdf_page_num in range(start_page, end_page):
        page = reader.pages[pdf_page_num]

        #create page-number overlay
        packet = BytesIO()
        c = canvas.Canvas(packet)

        c.drawString(460, 20, str(f"Page - {page_number}"))
        c.save()

        packet.seek(0)

        overlay_pdf = PdfReader(packet)
        overlay_page = overlay_pdf.pages[0]

        #Merge page number onto original page
        page.merge_page(overlay_page)
        writer.add_page(page)
        page_number += 1
    
    output_file = f"part_{page_num + 1}.pdf"

    with open(output_file, "wb") as file:
        writer.write(file)
    
    print(f"Created: {output_file}")

# print(pages_per_parts)


