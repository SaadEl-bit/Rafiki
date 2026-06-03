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