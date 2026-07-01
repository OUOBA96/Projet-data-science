import os
import markdown
from xhtml2pdf import pisa

def convert_markdown_to_pdf():
    print("Démarrage de la conversion du rapport en PDF...")
    
    # 1. Lecture du fichier Markdown
    md_path = "Rapport_Technique_RAG_Sante_BF.md"
    pdf_path = "Rapport_Technique_RAG_Sante_BF.pdf"
    
    if not os.path.exists(md_path):
        print(f"Erreur : Le fichier {md_path} n'existe pas.")
        return
        
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
        
    html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code', 'toc'])
    
    # Eviter le saut de page pour le tout premier H1 (xhtml2pdf ne supporte pas :first-of-type)
    html_content = html_content.replace("<h1", '<h1 style="page-break-before: avoid;"', 1)
    
    # 3. Structuration HTML et injection de styles CSS Premium (optimisés pour xhtml2pdf/pisa)
    styled_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    @page {{
        size: a4;
        margin: 2.5cm 2cm 2.5cm 2cm;
    }}
    
    body {{
        font-family: 'Helvetica', 'Arial', sans-serif;
        font-size: 10.5pt;
        line-height: 1.6;
        color: #2c3e50;
    }}
    
    /* Pages et En-têtes */
    h1 {{
        font-size: 20pt;
        color: #1a4d4a;
        margin-top: 30px;
        margin-bottom: 15px;
        padding-bottom: 5px;
        page-break-before: always;
    }}
    
    /* Empêcher le saut de page pour le tout premier H1 */
    h1:first-of-type {{
        page-break-before: avoid;
    }}
    
    h2 {{
        font-size: 14pt;
        color: #1e5f5b;
        margin-top: 25px;
        margin-bottom: 10px;
        padding-bottom: 3px;
    }}
    
    h3 {{
        font-size: 12pt;
        color: #2c3e50;
        margin-top: 20px;
        margin-bottom: 8px;
    }}
    
    p {{
        margin-bottom: 12px;
        text-align: justify;
    }}
    
    /* Listes */
    ul, ol {{
        margin-bottom: 12px;
        padding-left: 20px;
    }}
    li {{
        margin-bottom: 5px;
    }}
    
    /* Tableaux */
    table {{
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
        margin-bottom: 15px;
        font-size: 9.5pt;
    }}
    th {{
        background-color: #1e5f5b;
        color: white;
        font-weight: bold;
        padding: 8px;
        border: 1px solid #1e5f5b;
        text-align: left;
    }}
    td {{
        padding: 8px;
        border: 1px solid #bdc3c7;
    }}
    tr:nth-child(even) {{
        background-color: #f8f9fa;
    }}
    
    /* Blocs de code (Mermaid, listings) */
    pre {{
        background-color: #f7f9fb;
        border: 1px solid #e2e8f0;
        border-left: 4px solid #1e5f5b;
        padding: 10px;
        font-family: 'Courier New', Courier, monospace;
        font-size: 9pt;
        overflow: hidden;
        margin-top: 10px;
        margin-bottom: 10px;
    }}
    code {{
        font-family: 'Courier New', Courier, monospace;
        background-color: #f1f5f9;
        padding: 2px 4px;
        border-radius: 3px;
        font-size: 9.5pt;
    }}
    
    /* Page de garde */
    .cover {{
        text-align: center;
        padding-top: 5cm;
        height: 100%;
        page-break-after: always;
    }}
    .cover h1 {{
        font-size: 24pt;
        color: #1a4d4a;
        border-bottom: none;
        margin-bottom: 20px;
        page-break-before: avoid;
    }}
    .cover h2 {{
        font-size: 16pt;
        color: #7f8c8d;
        border-bottom: none;
        margin-bottom: 40px;
    }}
    .cover .meta {{
        margin-top: 6cm;
        font-size: 12pt;
        line-height: 1.8;
    }}
    .cover .divider {{
        height: 3px;
        background: linear-gradient(90deg, #1a4d4a, #1e5f5b);
        width: 60%;
        margin: 20px auto;
    }}
</style>
</head>
<body>

<!-- Contenu du rapport -->
{html_content}

</body>
</html>
"""

    # 4. Conversion HTML vers PDF
    with open(pdf_path, "w+b") as result_file:
        pisa_status = pisa.CreatePDF(
            styled_html,
            dest=result_file,
            encoding='utf-8'
        )
        
    if pisa_status.err:
        print(f"Erreur lors de la génération du PDF (Code {pisa_status.err})")
    else:
        print(f"Succès : Le fichier PDF a été généré sous '{pdf_path}'.")

if __name__ == "__main__":
    convert_markdown_to_pdf()
