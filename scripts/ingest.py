import os
import shutil
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def main():
    print("Démarrage du processus de vectorisation (ingestion)...")
    
    # Chemin vers la base vectorielle locale
    persist_directory = "chroma_db"
    
    # Supprimer l'ancienne base de données si elle existe
    if os.path.exists(persist_directory):
        print(f"Nettoyage de l'ancienne base vectorielle dans '{persist_directory}'...")
        shutil.rmtree(persist_directory)
        
    # 1. Chargement des documents (fichiers .md dans le dossier data/)
    print("Chargement des fichiers de connaissances...")
    loader = DirectoryLoader(
        "data", 
        glob="*.md", 
        loader_cls=TextLoader, 
        loader_kwargs={"encoding": "utf-8"}
    )
    documents = loader.load()
    print(f"Nombre de documents chargés : {len(documents)}")
    
    # 2. Découpage du texte en morceaux (Chunking)
    print("Découpage des documents en morceaux (chunks)...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800, 
        chunk_overlap=100,
        separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Nombre total de fragments créés : {len(chunks)}")
    
    # 3. Initialisation du modèle d'embeddings (Modèle local et gratuit de HuggingFace)
    print("Initialisation du modèle d'embeddings local ('all-MiniLM-L6-v2')...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'}
    )
    
    # 4. Création et persistance de la base vectorielle ChromaDB
    print("Indexation des fragments dans la base vectorielle ChromaDB...")
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    
    # Sauvegarder la base de données sur le disque
    vectordb.persist()
    print(f"Indexation terminée avec succès ! La base vectorielle est sauvegardée dans '{persist_directory}'.")

if __name__ == "__main__":
    main()
