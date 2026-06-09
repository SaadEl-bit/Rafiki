Tu vas agir en tant qu'expert en création de présentations techniques et pitchs de projets. Je dois préparer une présentation PowerPoint pour mon projet. La présentation finale sera en français.

Je vais te fournir la description complète et technique de mon projet. Ton rôle est d'analyser attentivement cette description, puis de me proposer une **planification complète pour la présentation** (agenda, structure des slides, et points clés à aborder dans chaque slide). 

Propose-moi ce plan détaillé en premier afin que je puisse le lire, le confirmer, ou te demander des modifications avant de passer à la rédaction finale du contenu.

Voici la description complète et technique de mon projet :

### 1. Vision Globale du Projet
- **Nom du projet :** Rafiki — رفيقي
- **Slogan :** "رفيقك في الدراسة — Ton compagnon pour le Bac"
- **Description :** Rafiki est un tuteur IA adaptatif conçu spécifiquement pour les étudiants marocains en 2ème Bac (Terminale).
- **Matières ciblées (MVP) :** Mathématiques, Physique-Chimie, et Anglais. L'application interagit en français pour les sciences et en anglais pour la langue.

### 2. Le Problème Résolu
Les lycéens marocains ont souvent du mal à trouver des corrections détaillées pour leurs exercices, et les professeurs ne peuvent pas accompagner chaque élève individuellement. Les ressources sont éparpillées (PDFs, vidéos). L'objectif est d'offrir un tuteur privé disponible 24/7 qui ne donne pas seulement la réponse, mais explique la démarche pédagogique en se basant **strictement** sur le programme officiel marocain, pour éviter les "hallucinations" des IA génériques comme ChatGPT.

### 3. Fonctionnalités Clés (MVP)
- **Chat Q&A (Opérationnel) :** L'élève peut poser une question. L'IA cherche la réponse dans une base de données vectorielle (ChromaDB) contenant tout le programme du 2ème Bac et génère une explication étape par étape.
- **Correction d'Exercices (Opérationnel) :** L'élève upload une photo ou un PDF d'un exercice. L'IA l'analyse, extrait le texte (OCR), et corrige l'exercice étape par étape comme un vrai professeur.
- **Upload & OCR en Direct (Opérationnel) :** L'application intègre un modèle de vision (Vision LLM) pour extraire le texte mathématique et physique complexe depuis des images. Ces informations sont stockées dans une mémoire RAG éphémère (liée à la session de l'utilisateur).
- **Cadre Référentiel, Génération d'Exercices, Examens (UI Prête) :** L'interface utilisateur est déjà construite pour ces fonctionnalités qui seront connectées à l'IA après le MVP.

### 4. Architecture Technique (3 Serveurs)
Le projet repose sur une architecture professionnelle divisée en 3 couches distinctes (totalement gratuite pour le MVP) :
1. **Frontend (Vercel) :** Application web développée en Next.js 16 (App Router) avec JavaScript et Tailwind CSS. L'interface offre une expérience utilisateur premium (templates Stitch).
2. **Backend & Couche IA (Kaggle) :** Serveur Python construit avec FastAPI et Uvicorn. Il tourne sur un Notebook Kaggle exploitant deux cartes graphiques (Dual T4 GPUs). Le backend est exposé au frontend via un tunnel sécurisé (Localtunnel).
3. **Stockage des Modèles (HuggingFace) :** Les poids des modèles IA et le dataset (index ChromaDB) sont téléchargés depuis HuggingFace au démarrage du serveur Kaggle.

### 5. Implémentation IA (Dual-GPU)
Pour éviter de surcharger la mémoire (Out-Of-Memory), le backend Kaggle utilise la quantification en 4-bit (BitsAndBytes) et répartit la charge sur deux GPUs :
- **GPU 0 (Modèle Texte) :** Fait tourner `Saad-Elouakate/rafiki-qwen-2.5-finetune`. C'est un modèle Qwen2.5 de 1.5B paramètres que j'ai personnellement fine-tuné (LoRA) sur 277 paires de Q&A pour qu'il adopte le style d'un professeur marocain. Il gère la génération de texte et le RAG.
- **GPU 1 (Modèle Vision) :** Fait tourner `Qwen/Qwen2.5-VL-3B-Instruct`. Il est dédié exclusivement à l'OCR (Optical Character Recognition) pour lire les exercices uploadés par les étudiants.

### 6. Les 6 Phases de Réalisation du Projet
- **Phase 1 :** Pipeline d'extraction des PDFs bruts du programme marocain vers un format Markdown structuré.
- **Phase 2 :** Création de la base de connaissances globale RAG (Index vectoriel ChromaDB).
- **Phase 3 :** Création du dataset (paires Q&A) et Fine-Tuning du modèle Qwen2.5 avec LoRA.
- **Phase 4 :** Développement du Backend FastAPI, intégration du RAG éphémère (session en mémoire) et de l'OCR en direct.
- **Phase 5 :** Développement du Frontend Next.js avec un design premium.
- **Phase 6 :** Intégration complète de bout en bout (Frontend communiquant avec les GPUs Kaggle via Localtunnel).

Confirme-moi simplement que tu as bien lu et compris ce projet. Dis-moi que tu es prêt à recevoir mes instructions et le template pour commencer à planifier la présentation PowerPoint.
