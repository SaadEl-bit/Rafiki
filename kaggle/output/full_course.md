<!-- Page 1 -->

```markdown
# Chapter 1
## Calcul de probabilité

### 1.1 Terminologie

#### 1.1.1 Expérience aléatoire et ensemble fondamental

**Définition 1.** Une expérience aléatoire ξ est une expérience qui, bien que répétée dans des conditions apparemment identiques, peut produire des résultats différents. L'ensemble des résultats possibles d'une expérience aléatoire ξ s'appelle l'ensemble fondamental (ou univers ou espace des résultats) et est noté Ω. Ses éléments sont appelés résultats ou événements élémentaires.

**Exemple 1.** On lance une pièce de monnaie. On a :

$\Omega = \{P, F\}$

Lancer la pièce est une expérience aléatoire.

#### 1.1.2 Événements aléatoires

**Définition 2.** Un événement aléatoire est un événement qui peut ou ne se réaliser au cours d'une expérience aléatoire. C'est un ensemble d'éventualités que l'on note souvent par A. C'est donc aussi une partie de Ω, soit $A \in \mathcal{P}(\Omega)$.

**Exemple 2.** Jet de dé : expérience aléatoire. Univers :

$\Omega = \{1, 2, 3, 4, 5, 6\}$

Éventualités : $\{1\}, \{2\}, \{3\}, \{4\}, \{5\}, \{6\}$. Événement A : tomber sur un nombre pair, soit :

$A = \{2, 4, 6\}$

#### 1.1.3 Algèbre des événements

- **Événement contraire $\bar{A}$** : $\bar{A}$ se réalise si et seulement si $A$ n'est pas réalisable.

- **Événement $A \cap B$** : $A \cap B$ est réalisé si et seulement si $A$ et $B$ sont simultanément réalisés.

- Si $A \cap B = \emptyset$, c'est-à-dire que la réalisation simultanée des événements $A$ et $B$ est impossible, les événements $A$ et $B$ sont dits incompatibles.
```


---


<!-- Page 2 -->

```markdown
# CHAPTER 1. CALCUL DE PROBABILITÉ

- **Événement A ∪ B :** A ∪ B est réalisé si et seulement si l’un au moins des événements A ou B est réalisé.
- **Événement A ⊆ B :** A ⊆ B signiﬁe que dans tous les cas où B est réalisé, A est aussi réalisé.

On arrive au point essentiel qui est de définir la probabilité d’un événement A (A ⊆ Ω), qui doit mesurer la chance que l’événement A a de se réaliser lors de l’expérience. La complexité de la définition dépend de celle de Ω : Ω peut être fini, infini dénombrable, ou infini non dénombrable.

## 1.2 Probabilité dans le cas général

**Définition 3.** Soit Ω un univers, P(Ω) (l'ensemble des parties de Ω) et A ⊆ P(Ω). On appelle probabilité P sur (Ω, A) une application :

$$
P : A \to [0,1]
$$

$$
\omega \mapsto P(\omega)
$$

telle que :

- $P(\Omega) = 1$
- Si A et B sont deux événements incompatibles (c'est-à-dire $A \cap B = \emptyset$), alors :
  $$
  P(A \cup B) = P(A) + P(B)
  $$

Le triplet $(\Omega, P(\Omega), P)$ est appelé espace probabilisé.

**Propriété 1.**
- $P(\bar{A}) = 1 - P(A)$
- Pour tout $A \in P(\Omega)$, $0 \leq P(A) \leq 1$
- $P(\emptyset) = 0$
- Si $A \subseteq B$, alors $P(A) \leq P(B)$
- $P(A \cup B) = P(A) + P(B) - P(A \cap B)$

## 1.2.1 Probabilité uniforme sur Ω

**Définition 4.** Lorsque Ω est de cardinal fini et que l'on affecte la même probabilité à chaque événement élémentaire, on dit qu'on choisit une probabilité P uniforme, aussi appelée équiprobabilité. On a alors :

- Pour tout $\omega \in \Omega$, $P(\omega) = \frac{1}{\text{Card}(\Omega)}$.
- Pour tout événement $E$, $P(E) = \frac{\text{Card}(E)}{\text{Card}(\Omega)} = \frac{\text{nombre de cas favorables}}{\text{nombre de cas possibles}}$.

```


---


<!-- Page 3 -->

```markdown
6
CHAPTER 1. CALCUL DE PROBABILIT´E
Principe `a suivre pour r´esoudre un exercice en probabilit´e:
1. D´eﬁnir l’exp´erience al´eatoire E et trouver l’univers Ω. C’est la phase la plus importante.
2. Chercher le cardinal de Ω: Card(Ω).
3. D´eﬁnir l’´ev´enement dont on veut calculer la probabilit´e en lui attribuant un nom, par exemple
A.
4. Chercher le cardinal de A en s’appuyant sur le d´enombrement.
5. Appliquer la formule de probabilit´es pour r´epondre aux questions.
**Exemple 3.** Une urne contient 7 boules blanches et 5 boules noires. On tire 3 boules de l’urne simultanément et sans remise. Quelle est la probabilité d’avoir 3 boules blanches ?
L’expérience aléatoire ξ est de tirer 3 boules de l’urne contenant au total 12 boules sans remise et sans ordre.
Ω = Ensemble de toutes les éventualités possibles, c’est-à-dire tirer 3 boules parmi 12. Comme le tirage se fait sans remise, le cardinal de Ω est donc $C_3^{12}$.
Soit E l’événement " avoir 3 boules blanches ". On a :
Card(E) = le choix de 3 boules parmi 7, c’est $C_7^3$.
Finalement, la probabilité $P(E)$ est :
$$
P(E) = \frac{\text{Card}(E)}{\text{Card}(\Omega)} = \frac{C_7^3}{C_{12}^3}.
$$
## 1.2.2 Probabilité conditionnelle

**Définition 5.** Soit $(\Omega, \mathcal{P}(\Omega), P)$ un espace probabilisé fini et A un événement donné tel que $P(A) \ne 0$, et B un événement quelconque. On appelle probabilité conditionnelle de B sachant que A est réalisé le nombre :
$$
P(B \mid A) = \frac{P(A \cap B)}{P(A)}.
$$
**Exemple 4.** On tire au hasard une carte parmi 10 (numérotées de 1 à 10). Soit S l’événement " le numéro tiré est multiple de 3 " : $E = \{3,6,9\}$, donc $\text{Card}(E) = 3$ et $P(E) = \frac{3}{10}$.
- $F$ l’événement " le numéro tiré est supérieur ou égal à 7 " : $F = \{7,8,9,10\}$, donc $P(F) = \frac{4}{10}$.
```


---


<!-- Page 4 -->

```markdown
# CHAPTER 1. CALCUL DE PROBABILITÉ

On a $E \cap F = \{9\}$, donc $P(E \cap F) = \frac{1}{10}$.

La probabilité conditionnelle $P(E | F)$ est :
$$
P(E | F) = \frac{P(E \cap F)}{P(F)} = \frac{\frac{1}{10}}{\frac{4}{10}} = \frac{1}{4}.
$$

**Remarque 1.**
1. L’événement contraire de $A | B$ est $A | B$.
2. Cas particulier : si $A \subset B$, alors $P(A) \leq P(B)$ et $P(A \cap B) = P(A)$, d’où
$$
P(A | B) = \frac{P(A \cap B)}{P(B)} = \frac{P(A)}{P(B)}.
$$

## Formules des probabilités composées

Si $A$ et $B$ sont tels que $P(A) > 0$ et $P(B) > 0$, on peut écrire :
$$
P(A | B) = \frac{P(A \cap B)}{P(B)} \Longrightarrow P(A \cap B) = P(A | B) \cdot P(B).
$$
De même :
$$
P(B | A) = \frac{P(A \cap B)}{P(A)} \Longrightarrow P(A \cap B) = P(B | A) \cdot P(A).
$$

- $A$: l’événement dont on cherche à prévoir la probabilité.
- $B$: l’élément additionnel qui aide à prévoir la probabilité de $A$.
- $P(A)$: c’est la probabilité a priori.
- $P(A | B)$: probabilité à posteriori de $A$ sachant $B$.
- $P(B)$: à calculer par la formule des probabilités totales.
- $P(B | A)$: fiabilité informationnelle de $B$ par rapport à $A$.

## Formules des probabilités totales

**Propriété 2.** Soit $\Omega$ un univers muni d'une probabilité $P$. Si des parties $B_1, B_2, \ldots, B_n$ constituent une partition de $\Omega$ (c’est-à-dire $B_i \cap B_j = \emptyset$ pour $i \neq j$ et $B_1 \cup B_2 \cup \cdots \cup B_n = \Omega$), alors pour tout élément $A$ on a :
$$
P(A) = \sum_{k=1}^{n} P(A \cap B_k) = \sum_{k=1}^{n} P(A | B_k) \cdot P(B_k).
$$

**Théorème 1.** (de Bayes) Soit $\{B_i, i=1, \ldots, n\}$ tel que $\bigcup_{k=1}^{n} B_k = \Omega$ et $B_i \cap B_j = \emptyset$ pour tout $i \neq j$ avec $P(B_i) > 0$. Soit $A \in \mathcal{P}(\Omega)$, on a :
$$
P(B_k | A) = \frac{P(A | B_k) \cdot P(B_k)}{\sum_{i=1}^{n} P(A | B_i) \cdot P(B_i)}.
$$

```


---


<!-- Page 5 -->

```markdown
8
CHAPTER 1.
CALCUL DE PROBABILIT´E

**Exemple 5.** Chez une banque, 20% des employés ont un diplôme en Finance ; parmi ceux-ci, 70% ont des postes de cadre. En revanche, parmi ceux qui n’ont pas de diplôme en finance, 15% occupent un poste de cadre. Si un cadre de cette banque est sélectionné au hasard, quelle est la probabilité qu’il soit un diplôme de finance ?

Les employés sont divisés en deux catégories disjointes :
- $B_1$: employé ayant un diplôme en finance.
- $B_2$: employé n’ayant pas de diplôme en finance.

D’après l’information initiale : $P(B_1) = 0.2$ et $P(B_2) = 0.8$ (car $1 - P(B_1)$).

Notons par $A$ l’événement "l’employé choisi est un cadre". On sait que :

$$
P(A | B_1) = 0.7
$$

$$
P(A | B_2) = 0.15
$$

On cherche à déterminer, pour un événement observé "l’employé choisi est un cadre", la probabilité qu’il soit diplômé en finance en soit l’origine :

$$
P(B_1 | A) = P(l'employé soit diplômé en finance sachant qu’il est cadre).
$$

Par la formule de Bayes pour le cas $n=2$, on a :

$$
P(B_1 | A) = \frac{P(A | B_1) \cdot P(B_1)}{P(A | B_1) \cdot P(B_1) + P(A | B_2) \cdot P(B_2)} = \frac{0.2 \times 0.7}{0.2 \times 0.7 + 0.8 \times 0.15} = 0.5384.
$$

**Indépendance d’événements**

**Définition 6.** On dit que deux événements $A$ et $B$ (de probabilité non nulle) sont indépendants lorsque la réalisation de l’un n’a pas d’influence sur la probabilité de la réalisation de l’autre, c’est-à-dire $P(B | A) = P(B)$ et $P(A | B) = P(A)$.

**Théorème 2.** (Critère d’indépendance) Deux événements $A$ et $B$ sont indépendants si et seulement si :

$$
P(A \cap B) = P(A) \cdot P(B).
$$

**Proof:** [Proof omitted]

**Exercise 5:** [Exercise omitted]
```


---

