import requests
from reportlab.pdfgen import canvas

# API endpoint
url = "https://jsonplaceholder.typicode.com/comments"

# Fetch data from API
response = requests.get(url)
comments = response.json()

# Create PDF
pdf = canvas.Canvas("comments_report.pdf")

y = 800

pdf.setTitle("Comments Report")
pdf.drawString(200, 820, "Comments Report")

for comment in comments:
    pdf.drawString(50, y, f"ID: {comment['id']}")
    pdf.drawString(100, y, f"Name: {comment['name'][:50]}")

    y -= 20

    # Create a new page if space runs out
    if y < 50:
        pdf.showPage()
        y = 800

pdf.save()

print("PDF created successfully: comments_report.pdf")