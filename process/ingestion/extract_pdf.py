#!/usr/bin/env python3
"""
PDF Text Extraction Script for PACK-cattle-science
Extracts metadata and text from PDF files for ingestion
"""

import os
import sys
import json
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("Error: pdfplumber not installed. Run: pip install pdfplumber")
    sys.exit(1)

def extract_pdf_info(pdf_path):
    """Extract text and metadata from PDF"""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            # Extract metadata
            metadata = pdf.metadata or {}
            
            # Extract text from first 3 pages (usually contains abstract)
            text = ""
            for i, page in enumerate(pdf.pages[:3]):
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n\n"
            
            return {
                "filename": Path(pdf_path).name,
                "metadata": {k: str(v) for k, v in metadata.items()},
                "text_preview": text[:5000],  # First 5000 chars
                "pages": len(pdf.pages)
            }
    except Exception as e:
        return {
            "filename": Path(pdf_path).name,
            "error": str(e)
        }

def main():
    # Directory with PDF files
    pdf_dir = Path("new-articles")
    
    if not pdf_dir.exists():
        print(f"Error: Directory {pdf_dir} not found")
        print("Please copy PDF files to: PACK-cattle-science/process/ingestion/new-articles/")
        sys.exit(1)
    
    # Find all PDF files
    pdf_files = list(pdf_dir.glob("*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in {pdf_dir}")
        print("Please copy PDF files to: PACK-cattle-science/process/ingestion/new-articles/")
        sys.exit(1)
    
    print(f"Found {len(pdf_files)} PDF file(s)")
    print("-" * 50)
    
    results = []
    
    for pdf_file in pdf_files:
        print(f"\nProcessing: {pdf_file.name}")
        info = extract_pdf_info(pdf_file)
        results.append(info)
        
        if "error" not in info:
            print(f"  Pages: {info['pages']}")
            print(f"  Text extracted: {len(info['text_preview'])} chars")
        else:
            print(f"  Error: {info['error']}")
    
    # Save results to JSON
    output_file = "extraction_results.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n{'='*50}")
    print(f"Results saved to: {output_file}")
    print("\nNext steps:")
    print("1. Review extraction_results.json")
    print("2. Create ingestion log entries")
    print("3. Generate SoTA annotations")

if __name__ == "__main__":
    main()
