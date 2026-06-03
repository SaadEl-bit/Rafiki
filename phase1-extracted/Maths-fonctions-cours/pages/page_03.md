# Niveau: 2 P.C. + 2 S.V.- COURS dérivation – étude des fonctions

## e. Remarque :

- si f n’est pas dérivable à droite (c.à.d. $\lim_{x \to x_0^+} \frac{f(x) - f(x_0)}{x - x_0} = \pm \infty$) dans ce cas on a demi tangente à droite de $x_0$ parallèle à l’axe des ordonnées.
- si f n’est pas dérivable à gauche (c.à.d. $\lim_{x \to x_0^-} \frac{f(x) - f(x_0)}{x - x_0} = \pm \infty$) dans ce cas on a demi tangente à gauche de $x_0$ parallèle à l’axe des ordonnées.

## f. Exemple : exemple f(x) = $\sqrt{(x+1)(x+2)}$.

- à droite de $x_0 = 1$ on a : $\lim_{x \to 1^+} f(x) = f(1)$ et $\lim_{x \to 1^+} \frac{f(x) - f(1)}{x - 1} = \infty$.
- donc $\left(C_f\right)$ admet demi tangente verticale (parallèle à l’axe des ordonnées) à droite du point $M(1, f(1))$
- à gauche de $x_0 = -1$ on a : $\lim_{x \to -1^-} f(x) = f(-1)$ et $\lim_{x \to -1^-} \frac{f(x) - f(-1)}{x - (-1)} = \infty$.
- donc $\left(C_f\right)$ admet demi tangente verticale (parallèle à l’axe des ordonnées) à gauche du point $M(-1, f(-1))$

## g. Approximation affine d’une fonction dérivable en un point.

## II. Dérivabilité sur un intervalle – fonction dérivée première – dérivée – dérivée nème d’une fonction :

### A. Dérivabilité sur un intervalle :

- f est une fonction dérivable sur $I = [a, b]$ si et seulement si f est dérivable en tout point $x_0$ de $I$.
- f est une fonction dérivable sur $[a, b]$ si et seulement si f est dérivable sur $I = [a, b]$ et f est dérivable à droite du point a.
- f est dérivable sur $[a, b]$ $\Leftrightarrow$ f est dérivable sur $[a, b]$ et f est dérivable à gauche de b.
- f est dérivable sur $[a, b]$ $\Leftrightarrow$ f est dérivable sur $[a, b]$ et f est dérivable à droite de a et à gauche de b.

### B. La fonction dérivée première d’une fonction – la fonction dérivée seconde – dérivée nème d’une fonction :

#### a. Définition :

- f est une fonction dérivable sur un intervalle I.
- La fonction g qui relie chaque élément x de I par le nombre $f'(x)$ s’appelle la fonction dérivée de f et on note : $g = f'$.
- On note : $g : \mathbb{R} \to \mathbb{R}$, $x \to g(x) = f'(x)$.
- g s’appelle la fonction dérivée de f on note : $g = f'$.
- La fonction dérivée de $f'$ sur I s’appelle la fonction dérivée seconde (dérivée d’ordre 2) on note $f''$ ou $f^{(2)}$.
- En général : la dérivée d’ordre n de f est la fonction dérivée de $f^{(n-1)}(x)$ (la dérivée de la fonction dérivée d’ordre n-1) et on note $f^{(n)}(x) = \left(f^{(n-1)}\right)'(x)$.

[Diagram: graphique de la fonction f(x) = $\sqrt{(x+1)(x+2)}$ avec les points de tangente verticale à droite et gauche de x0 = 1 et x0 = -1]