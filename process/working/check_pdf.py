import fitz
doc = fitz.open('Optimal_21d_PR_Guide.pdf')
print(f'Страниц: {len(doc)}')
for i, page in enumerate(doc):
    rect = page.rect
    w_inch = rect.width / 72
    h_inch = rect.height / 72
    orientation = "книжная" if h_inch > w_inch else "альбомная"
    print(f'Страница {i+1}: {w_inch:.1f}" x {h_inch:.1f}" ({orientation})')
