import fitz  # PyMuPDF

# Path to your PDF file
pdf_file_path = "example.pdf"

# Open the PDF
doc = fitz.open(pdf_file_path)

# Read each page
for page_number in range(len(doc)):
    page = doc.load_page(page_number)
    text = page.get_text()
    print(f"--- Page {page_number + 1} ---")
    print(text)
    print("\n")

# Close the document
doc.close()


with open("output.txt", "w", encoding="utf-8") as f:
    for page_number in range(len(doc)):
        page = doc.load_page(page_number)
        text = page.get_text()
        f.write(f"--- Page {page_number + 1} ---\n{text}\n\n")
