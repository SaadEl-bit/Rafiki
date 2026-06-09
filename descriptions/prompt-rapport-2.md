# Prompt pour la création du rapport du projet Rafiki

**Copiez et collez le texte ci-dessous et envoyez-le à Claude en joignant vos fichiers `Project-Description.md` et `README.md`.**

---

**[DÉBUT DU PROMPT]**

Agis en tant qu'Ingénieur Logiciel et Rédacteur Technique expert. Je dois présenter mon projet d'étude intitulé **"Rafiki — رفيقي — Moroccan Adaptive AI Tutor Platform"** à mon professeur pour validation et évaluation.

Je te fournis en pièce jointe les fichiers de documentation de mon projet (`Project-Description.md` et `README.md`). Ton objectif est de rédiger un **rapport de projet complet, détaillé et structuré**, de niveau académique et professionnel (en français), qui explique le projet de A à Z. Le but est que mon professeur comprenne parfaitement la vision, la complexité technique, l'architecture, les fonctionnalités et les étapes de réalisation de mon projet.

À la fin de ton analyse, tu devras générer le contenu textuel complet du rapport pour que je puisse le copier-coller dans Microsoft Word (ou me fournir le code Python complet utilisant la librairie `python-docx` pour générer le document `.docx` automatiquement avec la bonne mise en page).

### 📋 Table des Matières Exigée pour le Rapport :

Veuillez structurer le rapport exactement selon ce plan détaillé :

**1. Introduction Générale**
- Contexte éducatif (Le besoin d'un tuteur IA interactif et adapté au programme scolaire marocain).
- Problématique et public cible (Élèves de 2ème Baccalauréat).
- Objectifs principaux et définition du MVP (Minimum Viable Product).

**2. Vision et Fonctionnalités Clés du Projet**
- Présentation des matières ciblées (Mathématiques, Physique-Chimie, Anglais).
- Fonctionnalités principales de l'IA (Chat Q&A avec RAG, Correction d'exercices personnalisés étape par étape).
- Traitement de l'information (OCR en direct via des modèles de Vision).
- Modèle de gestion des données (Base de connaissances pré-chargée globale vs. Mémoire de session RAG temporaire pour les PDF uploadés par les étudiants).

**3. Architecture Technique et Déploiement**
- Explication approfondie de l'approche "3-Server Split" et pourquoi elle a été choisie (scalabilité, coût gratuit pour le MVP).
- **Couche Frontend :** Vercel (Next.js 16, App Router, UI premium avec Tailwind CSS et templates Stitch).
- **Couche Backend & Processing IA :** Environnement Kaggle Notebook (FastAPI, utilisation de Dual T4 GPUs avec quantification 4-bit pour éviter les problèmes de mémoire OOM, utilisation de Localtunnel).
- **Couche Stockage :** HuggingFace (Hébergement des modèles fine-tunés Qwen2.5 et de l'index ChromaDB).

**4. Les Étapes de Réalisation (MVP Build Roadmap)**
*Détailler comment le projet a été construit techniquement, phase par phase :*
- Phase 1 : Pipeline d'extraction des PDFs (Création des chunks Markdown).
- Phase 2 : Génération de la base de connaissances sémantique (RAG via ChromaDB).
- Phase 3 : Fine-Tuning du LLM (Utilisation de Qwen2.5-1.5B avec LoRA pour adopter le style d'un professeur marocain).
- Phase 4 : Développement de l'API Backend FastAPI (Endpoints d'upload, de correction et de Q&A avec OCR en direct).
- Phase 5 : Développement de l'interface utilisateur Next.js.
- Phase 6 : Intégration complète (End-to-End).

**5. Organisation et Structure du Code**
- Présentation de l'arborescence du projet (Dossiers `frontend/`, `src/`, `kaggle/`, `Document-Data-Set/`).
- Explication de la séparation des responsabilités entre les différentes briques logicielles (Frontend indépendant, Backend axé sur le calcul GPU).

**6. Conclusion et Perspectives**
- Bilan des réalisations techniques du MVP.
- Améliorations futures planifiées (Ajout de bases de données persistantes comme Supabase pour gérer les sessions utilisateurs, ajout des matières arabophones, génération d'examens automatisée).

### 🎯 Instructions strictes de rédaction :
- **Ton :** Académique, rigoureux, professionnel et convaincant. Le professeur doit sentir l'ampleur du travail technique et d'ingénierie.
- **Langue :** Français impeccable.
- **Détails techniques :** Utilise le vocabulaire technique adéquat (RAG, LoRA Fine-tuning, Dual GPU, Quantization 4-bit, ChromaDB, FastAPI, Next.js).
- **Format de sortie :** Rédige le contenu complet du rapport. Utilise une hiérarchie de titres très claire (H1, H2, H3), des listes à puces et mets en gras les concepts clés pour faciliter la lecture. Le rendu doit être structuré de sorte que je n'ai plus qu'à le mettre dans un document Word.

**[FIN DU PROMPT]**
