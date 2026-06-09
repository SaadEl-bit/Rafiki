# Plan de Présentation : Rafiki — رفيقي — Moroccan Adaptive AI Tutor

> **Public cible :** Professeur & camarades de classe (présentation en classe)
> **Durée :** ~15–20 minutes (ajustable)
> **Ton :** Professionnel, technique mais accessible, présenter un vrai produit
> **Objectif :** Démontrer un MVP complet d'ingénierie IA — de l'extraction de données à l'application full-stack déployée

---

## Aperçu du Flux de Présentation (13 Diapositives)

| # | Diapositive | Temps | Type |
|---|---|---|---|
| 1 | **Titre + Accroche** | 1 min | Ouverture |
| 2 | **Le Problème** | 1.5 min | Motivation |
| 3 | **Notre Solution — Rafiki** | 1.5 min | Vue d'ensemble |
| 4 | **Fonctionnalités Clés** | 2 min | Aperçu avant la démo |
| 5 | **Démo en Direct** | 3 min | Cœur de la présentation |
| 6 | **Architecture Technique (3 Serveurs)** | 2 min | Analyse approfondie |
| 7 | **Le RAG en Détail** | 1.5 min | Explication du concept clé |
| 8 | **Les Phases de Réalisation** | 2 min | Processus & effort |
| 9 | **Technologies Utilisées** | 1 min | Récapitulatif de la stack |
| 10 | **Défis & Apprentissages** | 1.5 min | Côté humain |
| 11 | **Roadmap Future** | 1 min | Vision |
| 12 | **Conclusion** | 0.5 min | Clôture |
| 13 | **Questions / Réponses** | ~2 min | Interaction |

---

## Plan Diapositive par Diapositive

---

### Diapositive 1 — Titre + Accroche

**Contenu à afficher :**
- Nom du projet : **Rafiki — رفيقي**
- Tagline : *"رفيقك في الدراسة — Ton compagnon pour le Bac"*
- Ton nom et ta classe
- Diapositive épurée et minimale — laisse le nom et la tagline respirer

**Comment présenter :**
- Commence par une question accrocheuse (rhétorique ou directe) :
  > *"Combien d'entre vous ont déjà passé des heures à chercher un seul théorème de maths entre les PDF et YouTube ?"*
- Puis enchaîne : *"C'est exactement le problème que j'ai décidé de résoudre."*
- Lis la tagline en darija puis en français — ça désarme l'audience

---

### Diapositive 2 — Le Problème

**Contenu à afficher :**
- Un scénario familier : élève de 2ème Bac, 7+ matières, PDFs en pagaille
- Points clés des difficultés :
  - **Ressources éparpillées** — PDFs, YouTube, révisions multi-sources
  - **Aucune aide personnalisée** — le prof ne peut pas aider 40+ élèves individuellement
  - **Temps perdu à chercher** au lieu d'étudier
  - **Exercices sans correction** — acheter des corrigés ou attendre le cours
- Optionnel : une image en split (élève frustré vs. élève serein avec l'IA)

**Comment présenter :**
- Parle d'expérience — c'est un problème que tous les camarades reconnaissent
- Reste court et concret, ne t'attarde pas trop

---

### Diapositive 3 — Notre Solution : Rafiki

**Contenu à afficher :**
- Phrase d'accroche : *"Un tuteur IA adaptatif qui répond aux questions du programme instantanément, corrige des exercices et comprend vos documents uploadés — en français ou en anglais."*
- 3 propositions de valeur maximum (visuellement) :
  - **Pré-chargé avec tout le programme 2Bac** — poser une question immédiatement, sans configuration
  - **Réponses basées sur les cours officiels** (RAG) — pas d'hallucinations
  - **Fonctionne en français & anglais** — correspond aux matières enseignées
- Mentionner : cible **Mathématiques, Physique-Chimie, English**

**Comment présenter :**
- Transition depuis le problème : *"Alors j'ai construit une solution."*
- Insiste sur **l'immédiateté** — "Un élève ouvre l'app et peut poser une question tout de suite"
- Insiste sur le **ancré dans le programme** — c'est ce qui rend l'outil fiable

---

### Diapositive 4 — Fonctionnalités Clés (avec Statut)

**Contenu à afficher :**
- Un tableau propre ou une grille d'icônes :

| Fonctionnalité | Statut | Description |
|---|---|---|
| 💬 Chat Q&A | ✅ Opérationnel | Poser une question → réponse étape par étape avec RAG |
| ✍️ Correction d'exercices | ✅ Opérationnel | Uploader un exercice → l'IA corrige comme un professeur |
| 📤 Upload & OCR en direct | ✅ Opérationnel | Uploader PDF/images → texte extrait dans la session |
| 📚 Cadre Référenciel (الإطار المرجعي) | 🔶 UI prête | Voir les objectifs pédagogiques officiels |
| 📝 Générateurs (Examen, Résumé, etc.) | 🔶 UI prête | Placeholder — connexion IA post-MVP |

**Comment présenter :**
- Explique rapidement chaque fonctionnalité (5–10 sec chacune)
- Pour les 🔶 : *"L'interface est construite, la logique IA sera ajoutée dans la prochaine version"*
- Crée de l'attente pour la démo

---

### Diapositive 5 — Démo en Direct (Le Cœur)

**Contenu à afficher :**
- **C'est la diapositive la plus importante** — montre l'application en action
- Prépare **3 scénarios** (pas d'improvisation, le WiFi peut lâcher) :
  1. **Chat Q&A :** Demander *"Comment calculer la dérivée d'un polynôme ?"* — montre la réponse étape par étape avec formules LaTeX
  2. **Correction d'exercice :** Uploader un PDF d'exercice → montre l'extraction OCR → montre la correction IA étape par étape
  3. **OCR en direct :** Uploader un document quelconque → montre le texte extrait dans le chat

**Comment présenter (CRITIQUE) :**
- **Prépare des captures d'écran / vidéo de secours** au cas où l'API serait lente (cold start sur le free tier)
- Explique ce qui se passe sous le capot pendant chaque action :
  - *"Je clique sur Demander — la question part vers le backend FastAPI, qui récupère la leçon correspondante dans ChromaDB, puis l'envoie au LLM fine-tuné sur HuggingFace..."*
- Garde un rythme naturel — laisse le temps de réponse de l'IA te donner de l'espace pour expliquer

---

### Diapositive 6 — Architecture Technique (3 Serveurs)

**Contenu à afficher :**
- Le diagramme d'architecture depuis `Project-Description.md` :

```
Navigateur de l'élève
       │ HTTPS
       ▼
┌─────────────────────────────────┐
│  VERCEL — Frontend              │
│  Next.js 16 + Tailwind CSS      │
│  Landing, Chat, Correction      │
└──────────┬──────────────────────┘
           │ POST /api/ask, /api/upload, /api/correct
           ▼
┌─────────────────────────────────┐
│  RAILWAY — Backend              │
│  FastAPI (Python)               │
│  RAGRetrieval + Service OCR     │
└──────────┬──────────────────────┘
           │ API HuggingFace Inference
           ▼
┌─────────────────────────────────┐
│  HUGGINGFACE — Couche IA        │
│  Qwen2.5-1.5B (Texte)          │
│  Qwen2.5-VL-7B (Vision)        │
│  ChromaDB (Base Vectorielle)    │
└─────────────────────────────────┘
```

- Puis un **tableau des composants** :

| Composant | Rôle |
|---|---|
| **Frontend (Vercel)** | Interface élève — Next.js 16, Tailwind, templates premium |
| **Backend (Railway)** | Orchestrateur — FastAPI, RAG retrieval, extraction OCR |
| **IA + Données (HuggingFace)** | LLM + Modèle Vision + Index vectoriel ChromaDB |

**Comment présenter :**
- C'est la diapositive la plus technique — parcours-la **du haut vers le bas**
- Commence par le navigateur, trace une requête qui descend dans la stack
- Insiste sur le fait que chaque couche tourne sur son propre **hébergement gratuit** — ça montre de la débrouillardise
- Explique pourquoi 3 serveurs : *"Séparation des responsabilités — l'UI ne se soucie pas de l'IA, le backend ne se soucie pas du design"*

---

### Diapositive 7 — Le RAG en Détail

**Contenu à afficher :**
- Diagramme de flux simple :

```
Question de l'élève
     │
     ▼
[1] Transformer la question → vecteur
     │
     ▼
[2] Chercher dans ChromaDB (morceaux du programme)
     │
     ▼
[3] Récupérer les 3–5 morceaux les plus pertinents
     │
     ▼
[4] Envoyer la question + les morceaux au LLM
     │
     ▼
[5] Le LLM génère une réponse basée sur ces morceaux
```

- Encadré : **"RAG = Retrieval-Augmented Generation"**
  - Retrieval = récupérer les leçons pertinentes du programme
  - Generation = le LLM rédige la réponse en utilisant uniquement ce contexte
- Mentionner : Il y a aussi un **RAG de session éphémère** — les documents uploadés s'ajoutent temporairement

**Comment présenter :**
- C'est ton moment "profondeur technique" — montre que tu comprends le concept IA
- Utilise une analogie : *"Le RAG, c'est comme donner à un élève les pages exactes du manuel avant un examen — il ne peut répondre qu'à partir de ces pages"*
- Pourquoi le RAG ? *"Le modèle ne devine pas — il répond à partir du programme officiel"*

---

### Diapositive 8 — Les Phases de Réalisation (Le Parcours)

**Contenu à afficher :**
- Timeline ou liste étape par étape :

| Phase | Ce qui a été construit | Statut |
|---|---|---|
| **Phase 1** | Pipeline d'extraction PDF — PDF bruts → Markdown structuré | ✅ |
| **Phase 2** | Base de connaissances RAG — Index vectoriel ChromaDB | ✅ |
| **Phase 3** | Fine-Tuning — Qwen2.5 adapté avec LoRA sur 277 triplets Q&A | ✅ |
| **Phase 4** | Backend FastAPI — Endpoints RAG + LLM + OCR | ✅ |
| **Phase 5** | Frontend Next.js — Dashboard élève avec design premium | ✅ |
| **Phase 6** | Intégration complète — Test E2E (Frontend ↔ Backend) | 🔄 À venir |

**Comment présenter :**
- Présente ça comme un **parcours d'ingénierie**, pas juste une checklist
- Insiste sur la progression :
  - *"J'ai commencé avec des PDFs bruts et j'ai fini avec une app full-stack déployée"*
- La Phase 3 est impressionnante : *"J'ai fine-tuné un LLM de 1.5 milliard de paramètres sur un dataset Q&A que j'ai construit moi-même"*
- La Phase 6 montre de l'honnêteté sur ce qui n'est pas encore fait — ça dénote de la maturité

---

### Diapositive 9 — Technologies Utilisées

**Contenu à afficher :**
- Disposition en badges ou liste groupée :

| Catégorie | Technologies |
|---|---|
| **Frontend** | Next.js 16, React 19, Tailwind CSS, JavaScript |
| **Backend** | Python 3.11, FastAPI, Uvicorn, PyMuPDF, Pillow |
| **IA / ML** | Qwen2.5-1.5B-Instruct (texte), Qwen2.5-VL-7B (vision), LoRA |
| **Données / Stockage** | ChromaDB (BD vectorielle), Sentence Transformers (embeddings) |
| **Infrastructure** | Vercel (hébergement), Railway (backend), HuggingFace (API IA), Kaggle (GPU) |

**Comment présenter :**
- *"Voici la stack que j'ai choisie et pourquoi"* — justifie brièvement chaque choix
- Mentionne que tout est en **free-tier** : *"Zéro coût pour déployer — un vrai produit, sans budget"*

---

### Diapositive 10 — Défis & Apprentissages

**Contenu à afficher :**
- 3–4 défis rencontrés honnêtement :

| Défi | Solution |
|---|---|
| **Petit LLM qui hallucine** | Ajout du RAG — modèle forcé de répondre à partir du contexte du programme |
| **Cold start sur le free tier** | Railway et HF s'endorment après inactivité → première requête lente |
| **Qualité OCR sur PDFs scannés** | Passage d'un OCR simple à Qwen2.5-VL Vision LLM pour une meilleure extraction |
| **Pas de stockage persistant (MVP)** | Utilisation de ChromaDB éphémère par session — temporaire mais scalable ensuite |

**Comment présenter :**
- Sois humble — *"Tout n'a pas fonctionné du premier coup"*
- Montre que tu as appris de chaque échec
- C'est la diapositive la plus "humaine" — les camarades se connecteront à ces difficultés

---

### Diapositive 11 — Roadmap Future

**Contenu à afficher :**
- Liste courte des projets post-MVP :
  - **Stockage persistant** (Supabase / PostgreSQL) — comptes utilisateurs & historique
  - **Matières arabes** — Philosophie, Arabe, Éducation Islamique
  - **Génération d'exercices** — l'IA crée des exercices personnalisés à la demande
  - **Génération & correction d'examens** — simulation d'examen complète
  - **Application mobile** — React Native ou Flutter
- Mentionner : **La Phase 6 (Intégration)** est la prochaine étape immédiate

**Comment présenter :**
- *"Le MVP est construit. Voici où ça va ensuite."*
- Reste bref — 30 secondes — *"J'ai une vision claire pour le produit complet"*

---

### Diapositive 12 — Conclusion

**Contenu à afficher :**
- Nom du projet + tagline à nouveau
- Phase clé à retenir : *"Un tuteur IA qui comprend le programme marocain — construit de zéro, déployé gratuitement, prêt à l'emploi."*
- Ton nom + remerciements
- Invitation : *"Des questions ?"*

**Comment présenter :**
- Résumé rapide (15 secondes) : *"Problème → tuteur IA → architecture 3 serveurs → produit fonctionnel"*
- Puis ouvre la parole pour les questions

---

### Diapositive 13 — Questions / Réponses

**Contenu à afficher :**
- Une diapositive simple avec :
  - Le nom du projet et le mot **"Questions ?"**
  - Tes coordonnées (optionnel) : lien GitHub ou email
  - Lien vers le projet en ligne si déployé

**Comment présenter :**
- Prépare-toi à ces questions probables :
  - *"En quoi c'est différent de ChatGPT ?"* → Le RAG ancre les réponses dans le programme 2Bac ; ChatGPT est général. Fine-tuné sur le style du programme marocain.
  - *"C'est gratuit ?"* → Oui, hébergement free-tier, aucun paiement pour l'élève.
  - *"Je peux l'utiliser maintenant ?"* → Si le déploiement est actif, oui avec l'URL. Si encore en Phase 6, "Presque — la Phase 6 est le test d'intégration."
  - *"Combien de temps ça a pris ?"* → Résume la timeline depuis le status log (3 juin – 8 juin).
  - *"Pourquoi trois serveurs ?"* → Séparation des responsabilités, chaque couche utilise le free tier de sa plateforme.
  - *"C'est quoi le RAG ?"* → Simplifié : "Il cherche la réponse dans le manuel, puis demande à l'IA de l'expliquer."

---

## Notes de Présentation

### Recommandations de Timing
| Segment | Minutes |
|---|---|
| Diapos 1–4 (Contexte & Fonctionnalités) | ~4 min |
| Diapositive 5 (Démo) | ~3 min |
| Diapos 6–7 (Architecture & RAG) | ~3.5 min |
| Diapos 8–10 (Parcours & Tech) | ~4.5 min |
| Diapos 11–13 (Futur & Clôture) | ~2 min |
| **Total cœur** | **~17 min** |
| Q&A | ~2–3 min |

### Checklist de Préparation pour la Démo
- [ ] Préparer **3 requêtes qui fonctionnent** (les tester avant)
- [ ] Prendre des **captures d'écran / enregistrement vidéo** de secours (cold start peut prendre 30–60s sur free tier)
- [ ] Garder une **version locale** qui tourne en backup (backend sur `localhost:8000`, frontend sur `localhost:3000`)
- [ ] Tester sur la **résolution du projecteur** si possible
- [ ] Zoom du navigateur réglé pour une taille confortable

### Conseils pour la Présentation
- **Accroche-les tôt** — commence par le problème familier (Diapos 1–2)
- **La démo est la star** — laisse l'app parler d'elle-même
- **Utilise le tableau blanc** pour le RAG si le diagramme semble trop dense
- **Parle aux camarades, pas au prof** — ce sont les utilisateurs cibles
- **Admets honnêtement les limites** — ça montre de la maturité (cold start, Phase 6 pas terminée)
- **Termine par un appel à l'action** — demande-leur de tester, de donner leur avis

---

*Bonne chance pour ta présentation !*
