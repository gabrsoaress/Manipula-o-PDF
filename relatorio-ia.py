import pdfplumber

from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_ollama.llms import OllamaLLM


pdf_path = 'docs/boleto.pdf'
text = ''
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        text += page.extract_text()
        

llm = OllamaLLM(
    model='deepseek-r1',
    temperature=0.5,
)

template = """
Gere um relatório organizado e objetivo do texto fornecido:

Retorne os dados no formato JSON com nomes dos campos em snake_case.
{text}
"""




prompt = PromptTemplate(
    input_variables=['text'],
    template=template,
)

chain = prompt | llm | JsonOutputParser()

response = chain.invoke({'text': text})

print(response)
