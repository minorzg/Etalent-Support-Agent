# ✦ eTalent AI Assistant

> Agent conversationnel RAG (Retrieval-Augmented Generation) intelligent et sécurisé pour l'exploration de la documentation interne d'eTalent, propulsé par LangGraph, Google Gemini et Streamlit.

---

## 🚀 Présentation du Projet

**eTalent AI Assistant** est une application full-stack basée sur l'intelligence artificielle permettant d'interroger la base de connaissances documentaire de l'entreprise en langage naturel (Français, Anglais, Arabe). 

Grâce à une architecture RAG avec **ChromaDB** et à la gestion d'agents autonomes via **LangGraph**, l'assistant fournit des réponses précises et directes sur la structure organisationnelle, les équipes et les procédures, sans aucune hallucination.

---

## 🛠️ Stack Technique

* **Orchestration & Agents :** LangGraph, LangChain
* **Modèles LLM & Embeddings :** Google Gemini (`gemini-3.5-flash-lite`, `gemini-embedding-001`)
* **Base de Données Vectorielle :** ChromaDB
* **Traitement de Documents :** `PyPDFLoader`, `RecursiveCharacterTextSplitter`
* **Interface Utilisateur :** Streamlit (Design personnalisé en mode sombre)
* **Backend & Environnement :** Python 3.11+, `python-dotenv`

---

## 📁 Structure du Projet

```text
Etalent_Agent/
├── .venv/                          # Environnement virtuel Python
├── chroma_db/                      # Stockage persistant des vecteurs ChromaDB
├── f1test.py                       # Pipeline RAG & Définition de l'Agent LangGraph
├── app.py                          # Interface utilisateur web Streamlit
├── etalent_dossier_rag_complet.pdf # Document source de la base de connaissances
├── requirements.txt                # Dépendances du projet
└── .env                            # Configuration des variables d'environnement
⚡ Installation et Lancement
1. Cloner le dépôt
Bash
git clone [https://github.com/votre-utilisateur/Etalent_Agent.git](https://github.com/votre-utilisateur/Etalent_Agent.git)
cd Etalent_Agent
2. Créer et activer l'environnement virtuel
PowerShell
python -m venv .venv
.venv\Scripts\Activate.ps1
3. Installer les dépendances
Bash
pip install -r requirements.txt
4. Configurer la clé API
Créez un fichier .env à la racine du projet :

Extrait de code
GOOGLE_API_KEY=votre_cle_api_google_gemini
5. Lancer l'application
Bash
streamlit run app.py
✨ Fonctionnalités Clés
Recherche Vectorielle (RAG) : Découpage adaptatif (chunk_size=700, overlap=120) et indexation sémantique pour retrouver rapidement l'information pertinente.

Agent LangGraph Autonome : Gestion des boucles de décision et appels de tools dynamiques avec historique de conversation.

Support Multi-langue : Compréhension et réponse fluide en Français, Anglais et Arabe.

Sécurité & Règles Métier : Guardrails intégrés pour empêcher les hallucinations, isoler les instructions système et protéger les accès ERP.

Interface Modernisée : Dashboard Streamlit personnalisé avec suivi d'état du système et réinitialisation de session en un clic.

👤 Auteur
Mohamed Amine Rezzoug — Developpeur Full-Stack & AI Engineer
