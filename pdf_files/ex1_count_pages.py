'''
Exercise 1: Open a PDF and Count Pages
Goal

Print the total number of pages in a PDF.

Skills Learned
Opening PDFs
Reading metadata
Accessing pages
extractig text from first page
'''

from pypdf import PdfReader

reader = PdfReader("affected_apps.pdf")
first_page = reader.pages[0]
text = first_page.extract_text()

with open("first_page", "a") as file:
    file.write(f"\n\n{text}")                
    
total_pages = len(reader.pages)
print("Total pages:", total_pages)
# print(text)
