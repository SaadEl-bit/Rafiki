# Prompt pour génération du rapport Rafiki — رفيقي

> **À utiliser avec Claude (ou tout LLM) pour générer un rapport complet au format .docx**

---

## Contexte

Tu es un assistant chargé de rédiger un **rapport académique complet** sur un projet de fin d'études intitulé **"Rafiki — رفيقي — Moroccan Adaptive AI Tutor"**. Le projet est une plateforme de tutorat adaptatif basée sur l'IA, destinée aux élèves marocains de la 2ème année Baccalauréat (2ème Bac), couvrant les matières Mathématiques, Physique-Chimie et Anglais.

Tu dois générer un rapport professionnel au format **.docx** que l'étudiant pourra soumettre à son professeur pour expliquer le projet dans son intégralité.

---

## Instructions générales

1. Génère le rapport complet en **français** (sauf les termes techniques restés en anglais).
2. Structure le rapport selon le plan détaillé ci-dessous.
3. Pour chaque section, rédige un contenu riche, précis et professionnel.
4. Utilise un style formel et académique.
5. Inclus des **diagrammes ASCII** ou des **tableaux** là où c'est pertinent.
6. À la fin de chaque section majeure, ajoute une **conclusion partielle** qui résume les points clés.
7. Le rapport doit faire environ **15-25 pages** une fois mis en page dans Word.

---

## Plan de la table des matières

Le rapport doit contenir les sections suivantes :

### Page de garde
- Titre : « Rafiki — رفيقي — Moroccan Adaptive AI Tutor »
- Sous-titre : « Plateforme de Tutorat Adaptatif par Intelligence Artificielle pour les Élèves du 2ème Baccalauréat Marocain »
- Nom de l'étudiant / développeur
- Encadrant / Professeur
- Établissement
- Date
- Année universitaire

### Résumé (1 page)
- Synthèse du projet en 200-300 mots
- Objectif, problématique, solution proposée, résultats clés
- Mots-clés : IA, tutorat adaptatif, RAG, fine-tuning, 2ème Bac, Maroc

### Abstract (English version)
- Same as résumé but in English

### Table des matières
- Liste complète des sections et sous-sections avec numérotation

### Liste des figures et tableaux
- Tableau des figures et tableaux avec leurs titres

---

### 1. Introduction (2-3 pages)

#### 1.1 Contexte et motivation
- État de l'éducation au Maroc : classes nombreuses, manque de soutien individualisé
- Difficultés des élèves du 2ème Bac : pression des examens nationaux, manque de ressources personnalisées
- Constat : absence d'un outil numérique gratuit adapté au curriculum marocain spécifique
- Motivation personnelle du développeur (pourquoi ce projet ?)

#### 1.2 Problématique
- Question centrale : « Comment offrir un accompagnement scolaire personnalisé, gratuit et adapté au curriculum marocain aux élèves de 2ème Bac ? »
- Sous-questions :
  - Comment ancrer les réponses de l'IA dans le contenu officiel (programme du 2ème Bac) ?
  - Comment rendre l'outil accessible sans frais pour les étudiants ?
  - Comment gérer le format bilingue (français pour Maths/Physique, anglais pour English) ?

#### 1.3 Objectifs du projet
- **Objectif principal** : Développer un tuteur IA capable de répondre aux questions des élèves en s'appuyant uniquement sur le curriculum officiel marocain
- **Objectifs secondaires** :
  - Correction automatique d'exercices
  - OCR temps réel pour documents personnels
  - Interface premium et intuitive
  - Architecture 100% free-tier (zéro coût de déploiement)

#### 1.4 Cahier des charges
- **Fonctionnel** :
  - Chat Q&A avec réponses détaillées et pas-à-pas
  - Correction d'exercices (copie vierge ou avec réponses)
  - Upload de PDF/images avec OCR
  - Consultation du Cadre Référenciel (الإطار المرجعي)
  - Génération d'exercices, résumés et examens (post-MVP)
- **Technique** :
  - Base de connaissances pré-construite (ChromaDB) à partir des PDFs officiels
  - Modèle de langage fine-tuné sur le style pédagogique marocain
  - OCR via Vision LLM
  - Architecture 3 serveurs : Frontend (Vercel) + Backend (Kaggle) + Stockage (HuggingFace)
  - Localtunnel pour exposer l'API

#### 1.5 Périmètre du projet
- **Inclus** : 3 matières (Maths, Physique-Chimie, Anglais) — Niveau 2ème Bac — Langues française et anglaise
- **Exclu (post-MVP)** : Matières arabes (Philosophie, Arabe, Éducation Islamique) — Comptes utilisateurs persistants — Génération d'exercices/examens complète
- **Limites connues** : Mémoire session-based uniquement (pas de persistance en MVP) — Dépendance à Localtunnel pour l'exposition de l'API — Version gratuite de Kaggle avec limitations de temps

---

### 2. Analyse de l'existant (1-2 pages)

#### 2.1 Solutions existantes
- **Khan Academy** : Excellent contenu mais pas adapté au curriculum marocain
- **Google Classroom + outils** : Pas de tutorat IA intégré
- **ChatGPT / Gemini** : Réponses généralistes, pas ancrées dans le programme marocain
- **Duolingo** : Adaptatif mais limité aux langues
- **Plateformes marocaines existantes** : Souvent payantes, pas de tutorat IA personnalisé

#### 2.2 Positionnement de Rafiki
- **Avantages concurrentiels** :
  - Réponses 100% ancrées dans le curriculum officiel (via RAG)
  - Fine-tuné sur le style pédagogique marocain (pas à pas, formules, démonstrations)
  - Complètement gratuit
  - OCR temps réel pour notes personnelles
  - Interface premium orientée mobile-first
- **Différenciation** : C'est la seule solution qui combine RAG + fine-tuning + OCR + architecture 3-serveurs gratuite spécifiquement pour le curriculum marocain

---

### 3. Architecture technique (3-4 pages)

#### 3.1 Vue d'ensemble — Architecture 3 serveurs
- **Principe** : Séparation des couches (Frontend / Backend & IA / Stockage) sur 3 plateformes distinctes
- **Schéma architecture** :

```
NAVIGATEUR ÉLÈVE
       │  HTTPS
       ▼
┌─────────────────────────────────────┐
│  VERCEL — Frontend                  │
│  Next.js 16 · JS · Tailwind CSS     │
│  Pages : /chat, /correction, ...    │
└──────────────┬──────────────────────┘
       │  POST /api/ask
       │  POST /api/correct
       │  POST /api/upload
       ▼
┌─────────────────────────────────────┐
│  KAGGLE — Backend & IA          ✅  │
│  FastAPI · Python 3.11 · Uvicorn    │
│  Dual T4 GPU (15GB chacun)          │
│  GPU 0 : Texte (4-bit)              │
│  GPU 1 : Vision (4-bit)             │
└──────────────┬──────────────────────┘
       │  Modèles & données
       ▼
┌─────────────────────────────────────┐
│  HUGGINGFACE — Stockage             │
│  Modèle texte : rafiki-qwen-2.5     │
│  Modèle vision : Qwen2.5-VL-3B      │
│  Base vecteurs : ChromaDB           │
└─────────────────────────────────────┘
```

#### 3.2 Frontend (Vercel — Next.js 16)
- **Technologies** : Next.js 16 (App Router), JavaScript, Tailwind CSS
- **Pages principales** :
  - `/` → Landing page
  - `/chat` → Q&A Chat avec streaming des réponses
  - `/correction` → Upload et correction d'exercices
  - `/cadre` → Consultation du Cadre Référenciel
  - `/generators` → Placeholders pour génération future
- **Design** : Templates premium Stitch, interface responsive mobile-first, thème sombre/clair
- **Particularité** : Découplé du backend — communique uniquement via API REST

#### 3.3 Backend & IA (Kaggle — FastAPI)
- **Environnement** : Notebook Kaggle avec Dual T4 GPU (15GB VRAM chacun)
- **GPU 0 — Modèle de texte** : `rafiki-qwen-2.5-finetune` (4-bit quantized)
  - Fine-tuné sur Qwen2.5-1.5B-Instruct via LoRA
  - Format de réponse : pas-à-pas, style professeur marocain
  - Quantification 4-bit pour tenir dans la mémoire GPU
- **GPU 1 — Modèle de vision** : `Qwen2.5-VL-3B-Instruct` (4-bit quantized)
  - OCR temps réel sur PDFs et images uploadés
  - Extraction de texte de documents manuscrits ou imprimés
- **API Endpoints** :
  - `POST /api/ask` → Question → RAG → LLM → Réponse
  - `POST /api/correct` → Exercice → OCR → LLM → Correction
  - `POST /api/upload` → PDF/Image → OCR → Texte → Session ChromaDB
- **Exposition** : Localtunnel génère une URL publique HTTPS

#### 3.4 RAG — Retrieval-Augmented Generation
- **Base de connaissances pré-construite** :
  - ChromaDB indexée à partir de tous les PDFs du 2ème Bac (Maths, PC, English)
  - Segments (chunks) optimisés pour préserver les formules mathématiques
  - Index sémantique pour retrieval instantané
- **Session RAG temporaire** :
  - ChromaDB in-memory éphémère pour les documents uploadés par l'élève
  - Fusionnée avec la base globale pour la session en cours
  - Disparait au redémarrage du serveur (MVP)
- **Processus d'une requête typique** :
  1. Question élève → embedding → retrieval ChromaDB
  2. Contexte récupéré + question → prompt → fine-tuned LLM
  3. Réponse générée en français/anglais, pas-à-pas, avec références

#### 3.5 Stockage (HuggingFace)
- **rafiki-qwen-2.5-finetune** : Poids du modèle fine-tuné (LoRA adapters)
- **Qwen2.5-VL-3B-Instruct** : Modèle de vision (base, non fine-tuné)
- **ChromaDB index** : Index vectoriel complet de la base de connaissances
- **Datasets** : Jeux de données d'entraînement pour le fine-tuning

#### 3.6 Pipeline de traitement
1. **Extraction** : PDFs officiels → PyMuPDF/Qwen2.5-VL → Markdown structuré
2. **Chunking** : Markdown → Segments sémantiques optimisés
3. **Embedding & Indexation** : Segments → Vecteurs → ChromaDB
4. **Fine-tuning** : Dataset Q&A → LoRA → Modèle fine-tuné
5. **Inférence** : Question → RAG retrieval → LLM → Réponse formatée

---

### 4. Pipeline IA — Phase par phase (3-4 pages)

#### 4.1 Phase 1 — Extraction PDF → Markdown
- **Objectif** : Convertir les PDFs bruts et non structurés en Markdown propre et queryable
- **Documents traités** : 8 documents par matière (cours, exercices, examens)
- **Pipeline** : PyMuPDF pour extraction texte + Qwen2.5-VL pour OCR des zones complexes (formules, figures)
- **Défis rencontrés** :
  - Formules mathématiques en LaTeX mal formatées dans les PDFs
  - Documents manuscrits de qualité variable
  - Tableaux et graphiques non structurés
- **Solutions** : Segmentation par leçon/théorème/exercice, nettoyage manuel assisté par IA
- **Résultat** : Fichiers Markdown propres + `chunks.json` par matière, pushés sur HuggingFace ✅

#### 4.2 Phase 2 — RAG Knowledge Base (ChromaDB)
- **Objectif** : Construire un index sémantique robuste pour retrieval instantané
- **Méthode** : Embedding des chunks Markdown dans ChromaDB
- **Optimisations** :
  - Taille de chunk optimisée pour préserver le contexte des formules
  - Chevauchement (overlap) pour éviter la perte d'information entre chunks
  - Métadonnées : matière, chapitre, type (cours/théorème/exercice)
- **Validation** : Requête « Comment calculer la dérivée d'un polynôme ? » retourne les chunks corrects ✅

#### 4.3 Phase 3 — Fine-Tuning du LLM
- **Modèle de base** : `Qwen/Qwen2.5-1.5B-Instruct`
- **Méthode** : LoRA (Low-Rank Adaptation) — efficace, léger, rapide
- **Dataset** : Paires Q&A créées manuellement et par distillation depuis des modèles plus grands
  - Format : question en français/anglais → réponse pas-à-pas style professeur marocain
  - Exemples : résolutions d'exercices, explications de théorèmes, corrigés types
- **Objectif du fine-tuning** : Enseigner au modèle le format, le style et le raisonnement attendus dans le curriculum marocain
- **Quantification** : 4-bit (bitsandbytes) pour tenir sur T4 15GB
- **Résultat** : `rafiki-qwen-2.5-finetune` — répond avec la terminologie exacte du programme, donne des démonstrations complètes ✅

#### 4.4 Phase 4 — FastAPI Backend
- **API REST** développée avec FastAPI
- **Endpoints implémentés** :
  - `/api/ask` : Question → RAG retrieval → LLM inference
  - `/api/correct` : Upload exercice → OCR → LLM correction
  - `/api/upload` : PDF/Image → OCR → extraction → session mémoire
- **Intégration** : HuggingFace Inference API pour le déploiement initial, puis local sur Kaggle
- **Session RAG** : ChromaDB in-memory pour les documents temporaires ✅

#### 4.5 Phase 4.5 — Live OCR & Session RAG
- **OCR local** : Qwen2.5-VL-3B-Instruct tourne en local sur GPU 1
- **Avantage** : Pas de coût API, latence réduite, confidentialité des données élèves
- **Session RAG** : Documents OCRisés → embeddings → ChromaDB éphémère → queryable
- **Déploiement Kaggle** : Dual T4 GPU avec quantification 4-bit pour les deux modèles ✅

#### 4.6 Phase 5 — Frontend Next.js
- **Développement UI** avec Next.js 16 App Router
- **Design** : Templates premium Stitch, Tailwind CSS
- **Pages** : Chat Q&A, Correction, Cadre Référenciel, Generators
- **UX** : Interface mobile-first, streaming des réponses en temps réel
- **Déploiement** : Vercel (free tier) ✅

#### 4.7 Phase 6 — Intégration complète (À faire)
- **Objectif** : Valider la communication entre les 3 serveurs
- **Tâches** : Tests E2E, correction des bugs d'intégration, optimisation des latences
- **Statut** : ⬜ Non commencé

---

### 5. Composition technique détaillée (2-3 pages)

#### 5.1 Stack technologique

| Composant | Technologie | Version | Rôle |
|-----------|------------|---------|------|
| Frontend | Next.js | 16 | Interface utilisateur |
| Frontend Styling | Tailwind CSS | Dernière | Design responsive |
| Backend | FastAPI | Dernière | API REST orchestrateur |
| Backend Runtime | Python | 3.11 | Exécution IA |
| LLM Texte | Qwen2.5-1.5B-Instruct (fine-tuné) | 4-bit | Génération réponses |
| LLM Vision | Qwen2.5-VL-3B-Instruct | 4-bit | OCR |
| Vector DB | ChromaDB | Dernière | Base de connaissances |
| Fine-tuning | LoRA / PEFT | - | Adaptation du modèle |
| Quantification | bitsandbytes | 4-bit | Compression mémoire |
| Tunnel | Localtunnel | Dernière | Exposition API |
| Hébergement Frontend | Vercel | Free Tier | Déploiement web |
| Hébergement Backend | Kaggle | Free Dual T4 | Calcul GPU |
| Stockage Modèles | HuggingFace | - | Distribution |

#### 5.2 Modèle de données (Knowledge Base)
- **Structure ChromaDB** :
  - Collection : `bac2_curriculum`
  - Chunks : {text, metadata{subject, chapter, type, source_pdf}}
  - Index : embeddings sémantiques
- **Taille estimée** : Plusieurs milliers de chunks couvrant tout le programme 2ème Bac
- **Exemple de requête** :
  ```
  Question : "Explique le théorème de Thalès"
  → Embedding → Top-K similar chunks → Contexte pour LLM
  ```

#### 5.3 Format des réponses (LLM fine-tuné)
- **Structure type d'une réponse** :
  1. Reformulation de la question
  2. Rappel du théorème/formule concerné
  3. Démonstration pas-à-pas
  4. Application sur un exemple
  5. Conclusion / vérification
- **Langue** : Française (Maths, Physique) ou Anglaise (English)
- **Style** : Pédagogique, progressif, avec formules LaTeX

#### 5.4 Gestion de la mémoire (MVP)
- **Type** : Session-based (mémoire temporaire)
- **Durée** : Durée de vie de la session Kaggle
- **Contenu** : Historique du chat + documents uploadés
- **Limitation** : Perte des données au redémarrage
- **Évolution post-MVP** : Base de données persistante (Supabase PostgreSQL)

---

### 6. Déploiement et mise en œuvre (1-2 pages)

#### 6.1 Déploiement Backend (Kaggle)
1. Notebook Kaggle avec Dual T4 GPU activé
2. Cell 1 : Clonage du repo + installation des dépendances
3. Cell 2 : Surcharge des fichiers pour quantification 4-bit dual-GPU
4. Cell 3 : Démarrage FastAPI + génération URL Localtunnel
5. URL publique prête pour connexion frontend

#### 6.2 Déploiement Frontend (Vercel)
1. Configuration variable d'environnement `NEXT_PUBLIC_API_URL`
2. `npm install && npm run build`
3. Déploiement via Vercel CLI ou intégration GitHub
4. Site accessible publiquement

#### 6.3 Schéma de communication
```
Élève → https://rafiki.vercel.app/chat
  → Frontend Next.js
    → POST https://xxxx.loca.lt/api/ask {question, subject}
      → FastAPI (Kaggle)
        → Retrieval ChromaDB
        → Prompt + Contexte → LLM (GPU 0)
        → Réponse formatée
    ← Réponse JSON {answer, sources, steps}
  ← Affichage UI avec streaming
```

#### 6.4 Contraintes et limitations du déploiement
- **Kaggle free tier** : Sessions limitées dans le temps (9h max), GPU non garantis
- **Localtunnel** : URL change à chaque redémarrage, latence réseau
- **Quantification 4-bit** : Légère perte de qualité par rapport au modèle full precision
- **Pas de persistance** : Données perdues entre les sessions

---

### 7. Tests et validation (1 page)

#### 7.1 Tests unitaires
- Tests des endpoints API (FastAPI)
- Tests des pipelines d'extraction et chunking
- Tests du système RAG (pertinence des chunks retournés)

#### 7.2 Tests d'intégration
- Test de la communication Frontend ↔ Backend
- Test du pipeline complet : Upload → OCR → RAG → LLM → Réponse
- Test du fallback en cas d'erreur (modèle non chargé, timeout, etc.)

#### 7.3 Validation pédagogique
- Comparaison des réponses générées avec les corrigés officiels
- Évaluation par des professeurs (prévu post-MVP)
- Métriques : pertinence, exactitude, clarté pédagogique

#### 7.4 Résultats des tests
- Phase 1-5 : Tests unitaires passés ✅
- Phase 6 : Tests d'intégration à faire ⬜
- Known issues : Latence élevée, Localtunnel instable, pas de fallback élégant en cas d'erreur GPU

---

### 8. Analyse critique et pistes d'amélioration (1-2 pages)

#### 8.1 Forces du projet
- Architecture innovante 3-serveurs 100% free-tier
- Base de connaissances spécifique au curriculum marocain
- Approche duale RAG + Fine-Tuning pour qualité optimale
- Interface premium et mobile-first
- OCR temps réel intégré

#### 8.2 Faiblesses et limitations actuelles
- **Scope limité** : 3 matières uniquement, 1 niveau
- **Pas de persistance** : Les données utilisateur sont perdues entre les sessions
- **Dépendance Kaggle** : Sessions limitées, indisponibilité possible
- **Latence** : Le pipeline complet peut être lent (OCR + RAG + LLM)
- **Non testé en conditions réelles** : Phase 6 pas encore réalisée
- **Pas d'authentification** : Aucun système de comptes utilisateurs

#### 8.3 Pistes d'amélioration
- **Court terme** :
  - Finaliser Phase 6 (intégration E2E)
  - Ajouter un cache Redis pour réduire la latence
  - Améliorer le système de fallback
- **Moyen terme** :
  - Ajouter les matières arabes (Philosophie, Arabe, Éducation Islamique)
  - Base de données persistante (Supabase)
  - Comptes utilisateurs et historique
  - Génération d'exercices et examens complète
- **Long terme** :
  - Étendre aux autres niveaux (1ère Bac, Tronc Commun, Collège)
  - Application mobile native (React Native / Flutter)
  - Mode hors-ligne avec modèles on-device
  - Communauté de professeurs contributeurs
  - Dashboard analytics pour le suivi des élèves

---

### 9. Conclusion (1 page)

- Récapitulatif du projet et de son importance
- Atteinte des objectifs fixés (MVP couvert à 90%)
- Bilan personnel : apprentissages techniques et méthodologiques
- Impact potentiel : un outil gratuit qui pourrait aider des milliers d'élèves marocains
- Remerciements

---

### 10. Annexes (2-3 pages)

#### Annexe A : Diagramme d'architecture complet
- Version détaillée du diagramme 3-serveurs avec flux de données

#### Annexe B : Exemples de Q&A générées
- Question + réponse générée par le modèle fine-tuné (Maths, Physique, English)

#### Annexe C : Extrait de code
- `extraction_service.py` (OCR)
- `llm_service.py` (Inférence LLM)
- `rag_retriever.py` (Retrieval ChromaDB)

#### Annexe D : Captures d'écran de l'interface
- Landing page
- Chat Q&A avec réponse
- Interface de correction d'exercice
- Cadre Référenciel

#### Annexe E : Dépendances et bibliothèques
```
transformers, bitsandbytes, torch, accelerate, peft
fastapi, uvicorn, pydantic, python-multipart
chromadb, sentence-transformers
PyMuPDF, pillow, qwen-vl-utils
localtunnel, requests, httpx
```

---

## Instructions finales pour le format .docx

1. **Police** : Times New Roman 12pt pour le corps, 14-16pt pour les titres
2. **Interligne** : 1.5
3. **Marges** : 2.5cm (standard)
4. **Numérotation des pages** : Centrée en bas
5. **Images** : Intègre les captures d'écran et diagrammes fournis
6. **Table des matières** : Automatique avec numérotation
7. **Couleurs** : Utilise une palette sobre (bleu foncé #1a365d pour les titres, gris pour les sous-titres)
8. **En-tête** : Rafiki — رفيقي — Rapport de Projet
9. **Pied de page** : [Nom étudiant] | [Année universitaire]

---

## Output

Génère un fichier .docx complet, bien formaté, prêt à être soumis.
