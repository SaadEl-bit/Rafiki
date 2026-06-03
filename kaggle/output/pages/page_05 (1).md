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