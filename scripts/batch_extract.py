#!/usr/bin/env python3
"""Batch extract PDFs from new-articles folder"""

import os
import PyPDF2
import glob

def extract_all_pdfs():
    from pathlib import Path
    base_dir = str(Path(__file__).resolve().parent.parent / "process/ingestion/new-articles")
    
    # Find all PDFs
    pdfs = []
    for root, dirs, files in os.walk(base_dir):
        for f in files:
            if f.endswith('.pdf'):
                pdfs.append(os.path.join(root, f))
    
    # Process PDFs silently
    
    # Extract each PDF
    for pdf_path in pdfs[:5]:  # Process first 5 for now
        try:
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ''
                for i, page in enumerate(reader.pages[:3]):
                    text += page.extract_text() + '\n'
                
                # Save to txt
                txt_path = pdf_path + '.txt'
                with open(txt_path, 'w', encoding='utf-8') as out:
                    out.write(text)
                
        except Exception as e:
            pass  # Silent error

if __name__ == "__main__":
    extract_all_pdfs()
