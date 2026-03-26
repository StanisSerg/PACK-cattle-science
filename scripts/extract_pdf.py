#!/usr/bin/env python3
"""Extract text from PDF for SoTA processing"""

import PyPDF2
import sys
import os

def extract_pdf_text(pdf_path, pages=3):
    """Extract text from first N pages of PDF"""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            num_pages = min(pages, len(reader.pages))
            for i in range(num_pages):
                page = reader.pages[i]
                text += page.extract_text() + '\n'
            return text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf.py <pdf_path> [num_pages]")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    pages = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    
    text = extract_pdf_text(pdf_path, pages)
    # Save to file to avoid encoding issues
    output_path = pdf_path + '.txt'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("OK")
