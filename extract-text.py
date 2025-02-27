import pdfplumber


pdf_path = 'docs/orcamento.pdf'

text = ''
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text += page.extract_text()

print(text)
