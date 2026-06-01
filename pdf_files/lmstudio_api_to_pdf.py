import requests
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
)
from reportlab.lib.styles import getSampleStyleSheet

# API Endpoint
API_URL = "http://127.0.0.1:1234/api/v1/models"

# Fetch data
response = requests.get(API_URL)
print(response.content)
response.raise_for_status()

data = response.json()
# print(data)
# Create PDF
pdf_file = "models_report.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=letter)

styles = getSampleStyleSheet()

content = []

# Title
title = Paragraph("Models API Report", styles["Title"])
content.append(title)
content.append(Spacer(1, 12))

# API Information
content.append(
    Paragraph(
        f"<b>Endpoint:</b> {API_URL}",
        styles["Normal"]
    )
)
content.append(Spacer(1, 12))

# Extract model list
models = data.get("models", [])
print(models)
# Summary Section
content.append(
    Paragraph(
        f"<b>Total Models:</b> {len(models)}",
        styles["Heading2"]
    )
)
content.append(Spacer(1, 12))

# Model Details
for index, model in enumerate(models, start=1):

    content.append(
        Paragraph(
            f"Model {index}",
            styles["Heading2"]
        )
    )

    content.append(
        Paragraph(
            f"<b>ID:</b> {model.get('id', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Object:</b> {model.get('object', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Owned By:</b> {model.get('owned_by', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Created:</b> {model.get('created', 'N/A')}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 10))

    # Draw a separator line using HTML
    content.append(
        Paragraph(
            "<font color='grey'>----------------------------------------------------</font>",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 10))

# Build PDF
doc.build(content)

print(f"PDF generated successfully: {pdf_file}")