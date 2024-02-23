# "C:/Users/lucam/OneDrive/Desktop/FI/FI_AMIPED.PDF"

# import tabula

# def estrai_tabelle_da_pdf(pdf_file):
#     # Estrarre le tabelle dal file PDF
#     tabelle = tabula.read_pdf(pdf_file, pages='all', multiple_tables=True)

#     # Convertire le tabelle estratte in una stringa di testo
#     tabelle_text = '\n\n'.join([tabella.to_csv(index=False) for tabella in tabelle])

#     return tabelle_text

# def salva_in_file_di_testo(data, output_file):
#     with open(output_file, 'w', encoding='utf-8') as file:
#         file.write(data)

# if __name__ == "__main__":
#     # Specifica il percorso del tuo file PDF
#     pdf_file = "C:/Users/lucam/OneDrive/Desktop/FI/FI_AMIPED.PDF"

#     # Specifica il percorso del file di testo in cui vuoi salvare le tabelle estratte
#     output_file = "tabelle.txt"

#     # Estrai le tabelle dal PDF
#     tabelle_estratte = estrai_tabelle_da_pdf(pdf_file)

#     # Salva le tabelle estratte in un file di testo
#     salva_in_file_di_testo(tabelle_estratte, output_file)

#     print("Le tabelle sono state estratte con successo e salvate in", output_file)

# from langchain_community.document_loaders import PDFMinerPDFasHTMLLoader
# from bs4 import BeautifulSoup as bs

# pdf_file = "C:/Users/lucam/OneDrive/Desktop/FI/FI_AMIPED.PDF"
# loader = PDFMinerPDFasHTMLLoader(pdf_file)

# data = loader.load()[0]   # entire PDF is loaded as a single Document

# soup = bs(data.page_content, "html.parser")

# # with open("tabella.html", "w",  encoding='utf-8') as f:
# print(soup.find_all(attrs={"style": "position:absolute; border: textbox 1px solid; writing-mode:lr-tb;"}))

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
