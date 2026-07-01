import os
import requests
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
try:
    from langchain_ollama import ChatOllama
except ImportError:
    from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate

class RAGEngine:
    def __init__(self, persist_directory="chroma_db", model_name="llama3", base_url="http://localhost:11434"):
        self.persist_directory = persist_directory
        self.model_name = model_name
        self.base_url = base_url
        
        # 1. Charger le modèle d'embeddings
        print("Chargement des embeddings...")
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'}
        )
        
        # 2. Charger la base vectorielle si elle existe
        if os.path.exists(self.persist_directory):
            print(f"Chargement de la base vectorielle depuis '{self.persist_directory}'...")
            self.vectordb = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embeddings
            )
        else:
            print(f"Base vectorielle non trouvée dans '{self.persist_directory}'. Veuillez lancer scripts/ingest.py.")
            self.vectordb = None
            
        # 3. Initialiser le LLM via Ollama par défaut
        self.llm = None
        self.test_ollama_connection()

    def test_ollama_connection(self):
        """Tente de se connecter à Ollama et renvoie True si disponible."""
        try:
            # Vérifier si le service Ollama répond sur le port
            resp = requests.get(self.base_url, timeout=2)
            if resp.status_code == 200:
                self.llm = ChatOllama(
                    model=self.model_name,
                    base_url=self.base_url,
                    temperature=0.2
                )
                return True
        except Exception:
            pass
        self.llm = None
        return False

    def _call_gemini_api(self, prompt, api_key):
        """Appelle l'API Gemini 1.5 Flash directement via HTTP."""
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }],
            "generationConfig": {
                "temperature": 0.2
            }
        }
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=15)
            if resp.status_code == 200:
                data = resp.json()
                return data["candidates"][0]["content"]["parts"][0]["text"]
            else:
                return f"Erreur API Gemini (Code {resp.status_code}) : {resp.text}"
        except Exception as e:
            return f"Erreur de connexion à l'API Gemini : {e}"

    def _call_groq_api(self, prompt, api_key):
        """Appelle l'API Groq (Llama 3) directement via HTTP."""
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2
        }
        try:
            resp = requests.post(url, headers=headers, json=payload, timeout=15)
            if resp.status_code == 200:
                data = resp.json()
                return data["choices"][0]["message"]["content"]
            else:
                return f"Erreur API Groq (Code {resp.status_code}) : {resp.text}"
        except Exception as e:
            return f"Erreur de connexion à l'API Groq : {e}"

    def query(self, question, k=3, provider="ollama", api_key=None):
        """
        Exécute la recherche RAG avec le fournisseur spécifié (Ollama, Gemini, Groq).
        """
        if not self.vectordb:
            return {
                "answer": "La base de données de connaissances n'est pas initialisée. Veuillez d'abord exécuter l'ingestion (`python scripts/ingest.py`).",
                "sources": []
            }
            
        # Effectuer la recherche documentaire
        retrieved_docs = self.vectordb.similarity_search(question, k=k)
        
        # Concaténer le contexte
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])
        sources = [
            {
                "file": os.path.basename(doc.metadata.get("source", "INSD_Doc")),
                "content": doc.page_content
            } for doc in retrieved_docs
        ]
        
        # Prompt avec consignes strictes
        prompt_template = """Vous êtes un assistant médical intelligent et d'orientation en santé pour le Burkina Faso (Afrique de l'Ouest).
Vous devez aider et conseiller l'utilisateur sur la nutrition, la prévention du paludisme et de la dengue, et l'orienter vers les structures de santé de référence (CSPS, CMA, CHU).

Voici les consignes STRICTES que vous devez respecter dans vos réponses :
1. **ORIENTATION ET PRÉVENTION** : Donnez des conseils de prévention (élimination des gîtes larvaires pour la dengue, utilisation de MILDA/CPS pour le paludisme, valorisation des aliments locaux comme le moringa ou le soumbala pour la nutrition).
2. **SÉCURITÉ ET FEU VERT MÉDICAL** : Ne donnez JAMAIS de diagnostic ferme. S'il y a de la fièvre, conseillez TOUJOURS de consulter immédiatement le CSPS ou le centre de santé le plus proche pour effectuer un Test de Diagnostic Rapide (TDR).
3. **CONTRE-INDICATIONS ABSOLUES** : Rappelez impérativement d'ÉVITER l'aspirine, l'ibuprofène ou les anti-inflammatoires en cas de suspicion de dengue car ils provoquent des hémorragies internes graves. Seul le paracétamol est autorisé avant consultation.
4. **ANTI-HALLUCINATION STRICT** : Répondez uniquement en vous basant sur le contexte fourni ci-dessous. Si le contexte ne contient pas l'information ou si la question n'a aucun rapport avec la santé/nutrition au Burkina Faso, répondez EXACTEMENT :
"Je suis désolé, mais cette information ne figure pas dans mes documents de référence de l'INSD et de la santé du Burkina Faso. Veuillez consulter un professionnel de la santé ou le centre de santé (CSPS) le plus proche pour en savoir plus."
N'inventez rien et ne faites aucune extrapolation en dehors du contexte.

---
CONTEXTE DE RÉFÉRENCE (INSD & SANTÉ BF) :
{context}
---

QUESTION DE L'UTILISATEUR :
{question}

RÉPONSE DE L'ASSISTANT SANTE (en français) :"""

        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )
        
        formatted_prompt = prompt.format(context=context, question=question)
        
        # Sélection du modèle d'exécution
        if provider == "gemini":
            if not api_key:
                return {
                    "answer": "Erreur : Clé API Gemini manquante. Veuillez saisir votre clé d'API dans la barre latérale.",
                    "sources": sources
                }
            answer = self._call_gemini_api(formatted_prompt, api_key)
            return {"answer": answer, "sources": sources}
            
        elif provider == "groq":
            if not api_key:
                return {
                    "answer": "Erreur : Clé API Groq manquante. Veuillez saisir votre clé d'API dans la barre latérale.",
                    "sources": sources
                }
            answer = self._call_groq_api(formatted_prompt, api_key)
            return {"answer": answer, "sources": sources}
            
        else: # Ollama par défaut
            # Retester la connexion au cas où le service a démarré
            if not self.llm:
                self.test_ollama_connection()
                
            if not self.llm:
                return {
                    "answer": "Ollama est hors ligne. Assurez-vous qu'Ollama est démarré sur votre machine et que le modèle `llama3` est installé (`ollama run llama3`). Sinon, vous pouvez utiliser les clés d'API de secours (Gemini/Groq) dans la barre latérale.",
                    "sources": sources
                }
            try:
                response = self.llm.invoke(formatted_prompt)
                answer = response.content if hasattr(response, "content") else str(response)
                return {"answer": answer, "sources": sources}
            except Exception as e:
                return {
                    "answer": f"Erreur lors de la génération via Ollama : {e}",
                    "sources": sources
                }

if __name__ == "__main__":
    # Test
    engine = RAGEngine()
    print("Test d'initialisation du moteur RAG réussi.")
