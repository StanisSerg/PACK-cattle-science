#!/usr/bin/env python3
import os
import re

base_dir = 'd:/Exocortex-V2/PACK-cattle-science/process/ingestion/new-articles'

results = []
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith('.pdf'):
            # Check for keywords
            if any(keyword in f.lower() for keyword in ['ghaffari', 'graef', 'lin', 'caixeta', 'duffield', 'mcfadden', 'mclean', 'perez', 'venjakob', 'vercouteren', 'sammad']):
                results.append(os.path.join(root, f))

# Write to file
with open('d:/Exocortex-V2/PACK-cattle-science/scripts/found_pdfs.txt', 'w', encoding='utf-8') as out:
    for r in results:
        out.write(r + '\n')

print(f"Found {len(results)} PDFs")
