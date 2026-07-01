# Agent d'Orientation Médicale & Prévention RAG (Santé) - Burkina Faso

Cette application est un assistant IA intelligent basé sur la méthode RAG (Retrieval-Augmented Generation). Elle utilise des données réelles issues de l'**INSD Burkina Faso** pour orienter les utilisateurs sur la nutrition, la prévention du paludisme et de la dengue, et fournit un annuaire interactif des pharmacies de garde et des centres de santé de Ouagadougou et Bobo-Dioulasso.

Le modèle linguistique (LLM) s'exécute en local via **Ollama** (par défaut avec le modèle `llama3`).

---

## Prérequis

1. **Python 3.10+** installé.
2. **Ollama** installé sur votre machine (optionnel si vous utilisez une clé API externe). Téléchargez-le depuis [ollama.com](https://ollama.com).
3. Si vous utilisez Ollama en local, téléchargez le modèle `llama3` :
   ```bash
   ollama pull llama3
   ```
4. *(Alternative)* Une clé API **Gemini** (obtenue gratuitement sur Google AI Studio) ou **Groq** si vous ne souhaitez pas exécuter de LLM en local.

---

## Installation

1. Placez-vous dans le répertoire du projet.
2. Il est fortement recommandé de créer et d'activer un environnement virtuel :
   ```bash
   # Création
   python -m venv .venv
   
   # Activation (Windows)
   .venv\Scripts\activate
   
   # Activation (macOS/Linux)
   source .venv/bin/activate
   ```
3. Installez les dépendances du projet :
   ```bash
   pip install -r requirements.txt
   ```

---

## Utilisation

Le projet se déroule en trois étapes simples :

### Étape 1 : Collecte des Données
Générer et compiler les synthèses INSD et l'annuaire des pharmacies/centres de santé :
```bash
python scripts/scrape_data.py
```
Les fichiers générés apparaîtront dans le dossier `/data`.

### Étape 2 : Ingestion dans la Base Vectorielle
Segmenter et insérer les données dans la base vectorielle locale ChromaDB :
```bash
python scripts/ingest.py
```

### Étape 3 : Lancer l'Application Web
Lancez l'interface Streamlit :
```bash
python -m streamlit run app/app.py
```

---

## Structure du Projet

* `data/` : Dossier contenant les documents textuels de connaissances.
* `scripts/scrape_data.py` : Script de collecte et de formatage des données.
* `scripts/ingest.py` : Script de vectorisation et de création de la base vectorielle ChromaDB.
* `app/rag_engine.py` : Logique d'orchestration RAG avec LangChain et Ollama.
* `app/app.py` : Interface utilisateur Streamlit moderne (discussion, annuaire, évaluation).
