import fitz  # PyMuPDF

def extract_text(pdf_path):
    pdf_path = "C:\Users\Strange\Desktop\healthDiagnosis-HackNITR\ml-api\medical_report_overview\Sample-filled-in-MR.pdf"
    text_content = ""
    try:
        # Open the PDF file
        with fitz.open(pdf_path) as pdf_document:
            # Iterate through each page
            for page_number in range(pdf_document.page_count):
                # Get the page
                page = pdf_document[page_number]
                
                # Extract text from the page
                text_content += page.get_text()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")

    return text_content

# Example usage

text_from_pdf = extract_text()

# # Print or use the extracted text content
print(text_from_pdf)
# with open('readme.txt', "w", encoding="utf-8") as f:
#     f.write(text_from_pdf)
