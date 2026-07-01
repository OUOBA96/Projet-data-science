import pypdf

reader = pypdf.PdfReader("Rapport_Technique_RAG_Sante_BF.pdf")
print(f"Nombre total de pages : {len(reader.pages)}")

for idx, page in enumerate(reader.pages[:5]):
    text = page.extract_text()
    first_lines = "\n".join(text.split("\n")[:5])
    print(f"--- Page {idx+1} ---")
    print(first_lines)
