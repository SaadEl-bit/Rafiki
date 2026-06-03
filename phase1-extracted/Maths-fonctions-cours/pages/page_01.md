# Niveau: 2 P.C. + 2 S.V.- COURS

## dérivation – étude des fonctions

### I. Dérivabilité d’une fonction en un point $x_0$ – dérivabilité à droite et à gauche en un point $x_0$ :

#### A. Dérivabilité :

##### a. Définitions :

Soit une fonction $f$ tel que son domaine de définition contient un intervalle ouvert $I$ et $x_0 \in I$.

- $f$ est dérivable au point $x_0$ $\Leftrightarrow \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0} = \ell \in \mathbb{R}$. $\lim_{h \to 0} \frac{f(x_0 + h) - f(x_0)}{h} = \ell \in \mathbb{R}$, $\ell = f'(x_0)$ s'appelle le nombre dérivé de $f$ en $x_0$.

- $f$ est dérivable à droite de $x_0$ $\Leftrightarrow \lim_{x \to x_0^+} \frac{f(x) - f(x_0)}{x - x_0} = \ell \in \mathbb{R}$. $\lim_{h \to 0^+} \frac{f(x_0 + h) - f(x_0)}{h} = \ell \in \mathbb{R}$, $\ell = f'_r(x_0)$ s'appelle le nombre dérivé à gauche de $f$ en $x_0$.

- $f$ est dérivable à gauche de $x_0$ $\Leftrightarrow \lim_{x \to x_0^-} \frac{f(x) - f(x_0)}{x - x_0} = \ell \in \mathbb{R}$. $\lim_{h \to 0^-} \frac{f(x_0 + h) - f(x_0)}{h} = \ell \in \mathbb{R}$, $\ell = f'_g(x_0)$ s'appelle le nombre dérivé à gauche de $f$ en $x_0$.

##### b. Propriété :

Soit une fonction $f$.

- $f$ est dérivable au point $x_0$ $\Leftrightarrow f$ est dérivable à droite et à gauche et $f'_r(x_0) = f'_g(x_0)$.

##### B. Interprétation géométrique des nombres dérivés $f'(x_0)$ et $f'_r(x_0)$ et $f'_g(x_0)$

##### a. Interprétation géométrique du nombre dérivé $f'(x_0)$ :

- $f$ est une fonction dérivable au point $x_0$.
- $(C_f)$ sa courbe représentative dans un repère $\left(\mathbf{O}, \mathbf{i}, \mathbf{j}\right)$.

- Le nombre dérivé $f'(x_0)$ est le coefficient directeur de la droite tangente $(T)$ à la courbe $(C_f)$ de $f$ au point $A\left(x_0, f(x_0)\right)$ (le point $x_0$).

- Equation cartésienne de la tangente $(T)$ à la courbe $(C_f)$ de $f$ au point $A\left(x_0, f(x_0)\right)$ est $(T): y = (x - x_0)f'(x_0) + f(x_0)$.

- Si $f'(x_0) = 0$ alors la tangente est parallèle à l'axe des abscisses.

##### b. Exemple :

1. Trouver équation de la tangente $(T)$ à la courbe $(C_f)$ de $f$ au point $x_0 = 1$ avec $f(x) = 2x^2$.

L'équation est $(T): y = (x - 1)f'(1) + f(1)$ ou $(T): y = (x - 1) \times 4 + 2$.