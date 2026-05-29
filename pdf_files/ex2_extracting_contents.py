# Exercise 2: Extract Text from All Pages

# Goal
# Loop through every page and print all text.

from pypdf import PdfReader

reader = PdfReader("affected_apps.pdf")

with open("ex2_extracting_all_contents.txt", "a", encoding="utf-8") as file:
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]

        text = page.extract_text()

        print(f"\n--- Page {page_num + 1} ---")
        file.write(f"--- Page {page_num + 1} ---\n")
        file.write(f"{text}\n\n")

    # print(text)
