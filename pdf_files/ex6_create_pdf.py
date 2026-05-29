# Exercise 7: Create a Simple PDF

# Goal
    # Generate your own PDF document.

# Skills Learned
    # PDF creation
    # Writing content


from reportlab.pdfgen import canvas

pdf = canvas.Canvas("hello_world.pdf")

pdf.drawString(100, 750, "Hello World!")
pdf.drawString(100, 730, "This is my first pdf creation!")

pdf.save()
print("PDF created successfuly.")