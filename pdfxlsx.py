import tabula
import pandas as pd

# Especifique o caminho do arquivo PDF
caminho_pdf = r"C:\Users\stefa\OneDrive\Documentos\extrato SARA.pdf"

# Use a função read_pdf para extrair os dados do PDF para um DataFrame do pandas
df = tabula.read_pdf(caminho_pdf, pages='all')

# Salve o DataFrame como um arquivo Excel
df.to_excel("saida.xlsx", index=False)