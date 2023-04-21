import tabula
import pandas as pd


pdf_path = 'path/to/transactions.pdf'


df = tabula.read_pdf(pdf_path, pages='all')


df.to_csv('output.csv', index=False)