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