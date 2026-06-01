from reportlab.pdfgen import canvas

pdf = canvas.Canvas("page_numbers.pdf")

print(type(pdf))

for i in range(1, 1000):
    pdf.drawString(100, 750, f"Page {i}")
    pdf.showPage()


pdf.save()

print("PDF created")

# reportlab.pdfgen.canvas.Canvas