import pdfplumber

def pdf_to_txt(pdf_file, html_file):
  with pdfplumber.open(pdf_file) as pdf:
    text = ''
    for page in pdf.pages:
      text += page.extract_text()

  with open(html_file, 'w', encoding='utf-8') as f:
    f.write(text)

# Example usage
pdf_file = 'C:/Users/lucam/OneDrive/Desktop/FI/FI_AMIPED.PDF'
txt_file = 'tabelle.txt'
pdf_to_txt(pdf_file, txt_file)
