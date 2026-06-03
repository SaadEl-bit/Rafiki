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