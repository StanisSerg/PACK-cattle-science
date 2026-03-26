#!/usr/bin/env python3
import PyPDF2
import sys

pdf_path = sys.argv[1]
output_path = pdf_path + '.txt'

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for i, page in enumerate(reader.pages[:5]):  # First 5 pages
            text += page.extract_text() + '\n'
        
        with open(output_path, 'w', encoding='utf-8') as out:
            out.write(text)
    print("OK")
except Exception as e:
    with open(output_path + '.error', 'w') as err:
        err.write(str(e))
    print("ERROR")
