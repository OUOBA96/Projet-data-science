import markdown

with open("Rapport_Technique_RAG_Sante_BF.md", "r", encoding="utf-8") as f:
    md_content = f.read()

html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'toc'])
print("--- Début de html_content ---")
print(html_content[:500])
