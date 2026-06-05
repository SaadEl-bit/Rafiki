<!-- Page 1 -->

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


---


<!-- Page 2 -->

# Niveau: 2 P.C. + 2 S.V.- COURS

## dérivation – étude des fonctions

### D’où le coefficient directeur est m = 4 et vecteur directeur est : $\vec{u}(1,4) = \vec{i} + 4\vec{j}$

### A partir du point A $(1,f(1))$ avec $f(1) = 2$

- On construit le point B tel que $\vec{AB} = \vec{i}$ et on construit le point C tel que : $\vec{BC} = 4\vec{j}$.
- D’où la droite $(AC)$ est la tangente $(T)$ au point $A$.
- Pour tracer la tangente il suffit de tracer un segment dans les extrémités on met des flèches son milieu est $A$.

### c. Interprétation géométrique des nombres dérivés $f'_x(x_0)$ et $f''_x(x_0)$ :

- **Si $f$ est dérivable à droite de $x_0$ on a une demi-tangente à droite de $x_0$ de coefficient directeur $f'_x(x_0)$**.
- **équation du demi tangent à droite de $-x_0$ est** $\left(T_{x_0}\right): y = \left(x - x_0\right)f'_x(x_0) + f(x_0)$ avec $x \geq x_0$.
- **Si $f$ est dérivable à gauche de $x_0$ on a une demi-tangente à droite de $x_0$ de coefficient directeur $f'_x(x_0)$**.
- **équation du demi tangent à gauche de $-x_0$ est** $\left(T_{x_0}\right): y = \left(x - x_0\right)f'_x(x_0) + f(x_0)$ avec $x \leq x_0$.
- **Si $f'_x(x_0) \neq f'_x(x_0)$ donc $f$ n’est pas dérivable en $x_0$ et le point $A(x_0, f(x_0))$ est appelé point anguleux**.

### d. Exemple :

soit $f(x) = (x+3)^3 + 2$ ; $x \geq -2$ on a $f'_d(-2) = 3$ et $f'_g(-2) = -2$

- **équation du demi tangent à droite de $-2$ est** $\left(T_{x_0}\right): y = (x + 2)f'_x(-2) + f(-2)$ avec $x \geq x_0$.
- **équation du demi tangent à gauche de $-2$ est** $\left(T_{x_0}\right): y = (x + 2)f'_x(-2) + f(-2)$ avec $x \leq x_0$.

[Diagram: Demi tangent à droite de -2]
[Diagram: Demi tangent à gauche de -2]
[Diagram: Demi tangent en -2 le point A (-2,3) est un point anguleux]


---


<!-- Page 3 -->

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


---


<!-- Page 4 -->

# Niveau: 2 P.C. + 2 S.V.- COURS

## dérivation – étude des fonctions

### III. Les opérations sur les fonctions dérivables :

#### a. Propriété :

Soient $f$ et $g$ deux fonctions dérivables sur $I$. on a :

- La fonction $f+g$ est dérivable sur $I$ et $\left(f+g\right)'(x)=f'(x)+g'(x)$.
- La fonction $af$ est dérivable sur $I$ et $\left(af\right)'(x)=a f'(x)$ avec $\alpha \in \mathbb{R}$.
- La fonction $f \times g$ est dérivable sur $I$ et $\left(fg\right)'(x)=f'(x)g(x)+f(x)g'(x)$.
- La fonction $\frac{f}{g}$ est dérivable sur $I$ $\forall x \in I, g(x) \ne 0$ et $\left(\frac{1}{g}\right)'(x) = -\frac{g'(x)}{g^2(x)}$.
- La fonction $\frac{f}{g}$ est dérivable sur $I$ $\forall x \in I, g(x) \ne 0$ et $\left(\frac{f}{g}\right)'(x) = \frac{f'(x)g(x)-f(x)g'(x)}{g^2(x)}$.

### IV. Dérivabilité des fonctions : polynomiales – rationnelles – $f^{(n)}$ – fonctions trigonométriques :

#### a. Propriété :

- Toute fonction polynomiale est dérivable sur son ensemble de définition $D_f = \mathbb{R}$ et $\left(ax^n\right)' = nax^{n-1}$ et $n \in \mathbb{N}$.
- Toute fonction rationnelle est dérivable sur son ensemble de définition $D_f$.
- $f$ est une fonction dérivable sur un intervalle $I$.

    - La fonction $f^n$ avec $n \in \mathbb{N}^*$ est dérivable sur $I$ et on a : $\left(f^n\right)'(x) = nf^{n-1}(x) f'(x)$.
    - Si pour tout $x$ de $I$, $f(x) \ne 0$ on a la fonction $f^n(x)$ avec $p \in \mathbb{Z}^*$ est dérivable sur $I$ et $\left(f^n\right)'(x) = pf^{n-1}(x) f'(x)$.
- La fonction $f(x) = \cos(x)$ est dérivable sur $\mathbb{R}$ avec $f'(x) = (\cos(x))' = -\sin(x)$.
- La fonction $f(x) = \sin(x)$ est dérivable sur $\mathbb{R}$ avec $f'(x) = (\sin(x))' = \cos(x)$.
- La fonction $f(x) = \tan(x)$ est dérivable sur $\mathbb{R} \setminus \left\{\frac{\pi}{2} + k\pi \mid k \in \mathbb{Z}\right\}$ avec $f'(x) = (\tan(x))' = 1 + \tan^2(x)$ ou encore $f'(x) = (\tan(x))' = -\frac{1}{\cos^2(x)}$.

#### b. Exemple : Calculer $g'(x)$ pour $g(x) = (-2x^4 + 5x^2 + x - 3)^7$.

On a : $g'(x) = \left[(-2x^4 + 5x^2 + x - 3)^7\right]'$.

$$
= 7(-2x^4 + 5x^2 + x - 3)^6 \cdot (-8x^3 + 10x + 1)
$$


---


<!-- Page 5 -->

# VII. Dérivabilité de la composée de deux fonctions :

## a. Théorème :

f dérivable en $ x_0 $ et g est dérivable en $ f(x_0) $ alors la fonction $ g \circ f $ est dérivable en $ x_0 $ et on a :

$$
(g \circ f)'(x_0) = f'(x_0) \times g'(f(x_0)).
$$

## b. Application :

- $ \left( \sqrt{f(x)} \right)' = \frac{f'(x)}{2\sqrt{f(x)}} $ ; $ x \in D_f $ et $ f(x) > 0 $.
- $ (\sin(ax + b))' = a \times \cos(ax + b) $ ; sur $ \mathbb{R} $.
- $ (\cos(ax + b))' = -a \times \sin(ax + b) $ ; sur $ \mathbb{R} $.
- $ (\tan(ax + b))' = a \times \left[ 1 + \tan^2(ax + b) \right] $ avec $ ax + b \neq \frac{\pi}{2} + k\pi $ ; $ k \in \mathbb{Z} $.

## V. La fonction dérivée de la fonction réciproque :

### a. Théorème :

Sont une fonction continue et strictement monotone sur I et $ f(1) = J $, $ f^{-1} $ est la fonction réciproque de la fonction $ \left( x_0 \in I \right) $; $ x_0 \to f(x_0) = y_0 $; $ (y_0 \in J) $

f est dérivable en $ x_0 $ alors la fonction $ f^{-1} $ est dérivable en $ y_0 = f(x_0) $ et $ \left( f^{-1} \right)'(f(x_0)) = \frac{1}{f'(x_0)} $

ou encore $ \left( f^{-1} \right)'(y_0) = \frac{1}{f'(f^{-1}(y_0))} $.

### b. Applications :

| $ n \in \mathbb{N}^* $ et $ r \in \mathbb{Q}^* $ et $ f $ est une fonction strictement positive et dérivable sur I | $ g'(x) = \left( \sqrt{x} \right)' = \left( x \right)^{1/2} $ ; $ \frac{1}{n} x^{1/2 - 1} $ ; $ n \in \mathbb{N}^* $ | $ g'(x) = \left( \sqrt{f(x)} \right)' = \left( f(x) \right)^{1/2} $ ; $ \frac{1}{n} f'(x) \times f(x)^{1/2 - 1} $ |
|---|---|---|
| $ g'(x) = (x^r)' = r x^{r-1} $ ; $ r \in \mathbb{Q}^* $ | $ \left[ f(x) \right]' = r x f'(x) \times f(x)^{r-1} $ ; $ r \in \mathbb{Q}^* $ |

### Exemple :

1. Calculer la fonction dérivée $ f' $ de $ f $.

$ f(x) = \sqrt{x} $ et $ f(x) = \sqrt{x^2 + 1} $ et $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
- $ f(x) = \sqrt{x^2 + 1} $

On a :

- $ f(x) = \sqrt{x} $
-


---


<!-- Page 6 -->

# Niveau: 2 P.C. + 2 S.V.- COURS

## dérivation – étude des fonctions

### Tableau des fonctions dérivées des fonctions usuelles :

| La fonction f | D_f | Domaine de définition de f | La fonction dérivée f' | D_f' | Domaine de définition de f' |
|---|---|---|---|---|---|
| f(x) = a | D_f = R | D_f = R | f'(x) = 0 | D_f' = R | D_f' = R |
| f(x) = x | D_f = R | D_f = R | f'(x) = 1 | D_f' = R | D_f' = R |
| f(x) = x^n | D_f = R, n ∈ N \ {1} | D_f = R | f'(x) = nx^(n-1) | D_f' = R | D_f' = R |
| n ∈ Z \ {1} ; f(x) = x^n | D_f = R | D_f = R | f'(x) = nx^(n-1) | D_f' = R | D_f' = R |
| f(x) = √x | D_f = [0, +∞[ | D_f = [0, +∞[ | f'(x) = 1/(2√x) | D_f' = ]0, +∞[ | D_f' = ]0, +∞[ |
| f(x) = 1/x | D_f = R^* | D_f = R^* | f'(x) = -1/x^2 | D_f' = R^* | D_f' = R^* |
| f(x) = sin x | D_f = R | D_f = R | f'(x) = cos x | D_f' = R | D_f' = R |
| f(x) = cos x | D_f = R | D_f = R | f'(x) = -sin x | D_f' = R | D_f' = R |
| f(x) = tan x | x ≠ π/2 + kπ ; k ∈ Z | x ≠ π/2 + kπ | f'(x) = 1 + tan²x | x ≠ π/2 + kπ | x ≠ π/2 + kπ |
| f(x) = √g(x) | x ∈ D_g / g(x) ≥ 0 | x ∈ D_g / g(x) ≥ 0 | f'(x) = g'(x)/(2√g(x)) | x ∈ D_g / g(x) > 0 | x ∈ D_g / g(x) > 0 |
| f(x) = a | D_f = R | D_f = R | f'(x) = 0 | D_f' = R | D_f' = R |
| f(x) = x | D_f = R | D_f = R | f'(x) = 1 | D_f' = R | D_f' = R |
| n ∈ N \ {1} ; f(x) = x^n | D_f = R | D_f = R | f'(x) = nx^(n-1) | D_f' = R | D_f' = R |
| n ∈ Z \ {1} ; f(x) = x^n | D_f = R | D_f = R | f'(x) = nx^(n-1) | D_f' = R | D_f' = R |

### Applications de la fonction dérivée première :

- dans le reste de ce chapitre f est une fonction numérique de la variable réelle x.
- (C_r) est sa courbe représentative dans un repère orthonormé (O, i, j).

### Remarque :

- **Définition :** La fonction f(x) = a est une fonction constante.
- **Théorème :** La dérivée d'une fonction constante est nulle.
- **Démonstration :** Soit f(x) = a, alors f'(x) = 0.
- **Exemple X :** La fonction f(x) = x est une fonction linéaire.
- **Exercice X :** Calculer la dérivée de f(x) = x².
- **Propriété :** La dérivée d'une fonction linéaire est une constante.
- **Remarque :** La dérivée d'une fonction constante est nulle.

### Exemple X :

- **Exemple 1 :** Calculer la dérivée de f(x) = x².
- **Calcul :** f'(x) = 2x.
- **Conclusion :** La dérivée de f(x) = x² est f'(x) = 2x.

### Exercice X :

- **Exercice 1 :** Calculer la dérivée de f(x) = x³.
- **Calcul :** f'(x) = 3x².
- **Conclusion :** La dérivée de f(x) = x³ est f'(x) = 3x².

### Propriété :

- **Propriété 1 :** La dérivée d'une fonction constante est nulle.
- **Propriété 2 :** La dérivée d'une fonction linéaire est une constante.
- **Propriété 3 :** La dérivée d'une fonction polynomiale est une fonction polynomiale de degré réduit de 1.

### Remarque :

- **Remarque 1 :** La dérivée d'une fonction constante est nulle.
- **Remarque 2 :** La dérivée d'une fonction linéaire est une constante.
- **Remarque 3 :** La dérivée d'une fonction polynomiale est une fonction polynomiale de degré réduit de 1.

### Tableau des fonctions dérivées des fonctions usuelles :

| La fonction f | D_f | Domaine de définition de f | La fonction dérivée f' | D_f' | Domaine de définition de f' |
|---|---|---|---|---|---|
| f(x) = a | D_f = R | D_f = R | f'(x) = 0 | D_f' = R | D_f' = R |
| f(x) = x | D_f = R | D_f = R | f'(x) = 1 | D_f' = R | D_f' = R |
| f(x) = x^n | D_f = R, n ∈ N \ {1} | D_f = R | f'(x) = nx^(n-1) | D_f' = R | D_f' = R |
| n ∈ Z \ {1} ; f(x) = x^n | D_f = R | D_f = R | f'(x) = nx^(n-1) | D_f' = R | D_f' = R |
| f(x) = √x | D_f = [0, +∞[ | D_f = [0, +∞[ | f'(x) = 1/(2√x) | D_f' = ]0, +∞[ | D_f' = ]0, +∞[ |
| f(x) = 1/x | D_f = R^* | D_f = R^* | f'(x) = -1/x^2 | D_f' = R^* | D_f' = R^* |
| f(x) = sin x | D_f = R | D_f = R | f'(x) = cos x | D_f' = R | D_f' = R |
| f(x) = cos x | D_f = R | D_f = R | f'(x) = -sin x | D_f' = R | D_f' = R |
| f(x) = tan x | x ≠ π/2 + kπ ; k ∈ Z | x ≠ π/2 + kπ | f'(x) = 1 + tan²x | x ≠ π/2 + kπ | x ≠ π/2 + kπ |
| f(x) = √g(x) | x ∈ D_g / g(x) ≥ 0 | x ∈ D_g / g(x) ≥ 0 | f'(x) = g'(x)/(2√g(x)) | x ∈ D_g / g(x) > 0 | x ∈ D_g / g(x) > 0 |
| f(x) = a | D_f = R | D_f = R | f'(x) = 0 | D_f' = R | D_f' = R |
| f(x) = x | D_f = R | D_f = R | f'(x) = 1 | D_f' = R | D_f' = R |
| n ∈ N \ {1} ; f(x) = x^n | D_f = R | D_f = R | f'(x) = nx^(n-1) | D_f' = R | D_f' = R |
| n ∈ Z \ {1} ; f(x) = x^n | D_f = R | D_f = R | f'(x) = nx^(n-1) | D_f' = R | D_f' = R |

### Applications de la fonction dérivée première :

- dans le reste de ce chapitre f est une fonction numérique de


---


<!-- Page 7 -->

# Niveau: 2 P.C. + 2 S.V.- COURS

## dérivation – étude des fonctions

### A. La monotonie d’une fonction et le signe de sa fonction dérivée :

#### a. Propriété :

f est une fonction dérivée sur un intervalle I.

- Si la fonction dérivée f' est strictement positive sur I alors la fonction f est strictement croissante sur I.
  (même si f' s'annule en un points fini de I ne change pas la monotonie de f )

- Si la fonction dérivée f' est strictement négative sur I alors la fonction f est strictement décroissante sur I.
  (même si f' s'annule en un points fini de I ne change pas la monotonie de f )

- Si la fonction f' est nulle sur I (sur I tout entier) alors f est constante.

#### b. Exemple :

Étudier les variations de f sur R avec f(x) = (2x + 4)².

- On calcule f' :
  f'(x) = [ (2x + 4)² ]'
  f'(x) = 2(2x + 4)(2x + 4)' = 2 × 2(2x + 4) = 8x + 16

- Signe de f' :
  On a f'(x) ≥ 0 ⇔ 8x + 16 ≥ 0
  ⇔ x ≥ -2

  Donc : f' est positif sur [-2, +∞[ et négatif sur [-∞, -2].

- Tableau de variation de f :

| x | -∞ | -2 | +∞ |
|---|----|----|----|
| f' | - | 0 | + |
| f | | | |

[Diagram: La fonction f(x) = 2x³]

### B. Extremums d'une fonction dérivable :

#### a. Propriété :

f est une fonction dérivée sur un intervalle ouvert I, a est un élément de I.

Si f est dérivable au point a et admet un extremum au point a alors f'(a) = 0.

Remarque : Si f'(a) = 0 ne signifie pas que f(a) est un extremum de la fonction f.

#### b. Exemple :

f(x) = 2x³ on a f'(x) = 6x² d'où f'(0) = 0 mais f(0) n'est pas un extremum de la fonction f.

[Diagram: La fonction f(x) = 2x³]


---


<!-- Page 8 -->

# Niveau: 2 P.C. + 2 S.V.- COURS dérivation – étude des fonctions

## c. Propriété :

f est une fonction dérivée sur un intervalle ouvert I, a est un élément de I.

Si f' s'annule au point a et f' change de signe au voisinage de a alors f(a) est un extremum de la fonction f

## VII. Applications de la fonction dérivée deuxième :

### A. Position relative de la tangente et la courbe – la concavité :

#### a. Propriété et définition :

f est une fonction deux fois dérivable sur un intervalle I.

∀x ∈ I : f''(x) > 0 (la fonction dérivée secondaire) alors :

- La courbe (Cₜ) de f est située au dessus des tangentes des points x tel que x ∈ I.

Dans ce cas on dit que la courbe (Cₜ) de f est concave (ou sa concavité est dans le sens des ordonnées positives), on note

∀x ∈ I : f''(x) < 0 (la fonction dérivée secondaire) alors :

- La courbe (Cₜ) de f est située au dessous des tangentes des x ∈ I.

Dans ce cas on dit que la courbe (Cₜ) de f est concave (ou sa concavité est dans le sens des ordonnées négatives), on note

#### b. Exemple :

**Exemple 1 :**

La figure ci-contre représente la courbe d'une fonction f.

- Sur l'intervalle ]-∞, +∞[ : la courbe (Cₜ) de f est convexe. (ou sa concavité est dans le sens des ordonnées positives).
- Sur l'intervalle ]-∞, 0[ : la courbe (Cₜ) de f est concave. (ou sa concavité est dans le sens des ordonnées négatives).

**Exemple 2 :**

Le tableau ci-contre représente le signe de la fonction dérivée secondaire de f et la concavité de la courbe (Cₜ) de f

| x | -∞ | -5 | -1 | 2 | +∞ |
|---|----|----|----|---|----|
| f''(x) | - | 0 | + | - | 0 | + |
| Concavité de (Cₜ) | \u2713 | \u2713 | \u2713 | \u2713 | \u2713 |

[Diagram: A graph showing the function f(x) with its derivative and second derivative, illustrating the concavity and convexity of the curve. The graph has a parabolic shape with a minimum at x = -1, and the second derivative is positive on the left of x = -1 and negative on the right.]

- 8 -


---


<!-- Page 9 -->

# Niveau: 2 P.C. + 2 S.V.- COURS

## dérivation – étude des fonctions

### B. Points d’inflexions :

#### a. Propriété et définition :

f est une fonction dérivable deux fois sur un intervalle ouvert I et $ x_0 \in I $.

Si la fonction dérivée seconde $ f'' $ s'annule en $ x_0 $ et $ f'' $ change de signe au voisinage de $ x_0 $ alors le point d'abscisse $ A(x_0, f(x_0)) $ est un point d'inflexion au courbe $ (C_f) $ ; dans ce cas la tangente au point $ A(x_0, f(x_0)) $ coupe (ou traverse) la courbe.

#### b. Exemple :

**Exemple 1 :**

- Soit la fonction $ f $ définie par : $ f(x) = \frac{x}{\sqrt{x^2 + 1}} $.
- $ (C_f) $ est sa courbe représentative dans un repère orthonormé $ (O, i, j) $.

**Exemple 2 :**

Le tableau suivant représente le signe de la fonction dérivée seconde de $ f $ et la concavité de la courbe $ (C_f) $ de $ f $

| x | -∞ | -5 | -1 | 2 | +∞ |
|---|----|----|----|----|----|
| f"(x) | - | 0 | + | - | 0 | - |
| Concavité de $ (C_f) $ | - | - | + | - | - |

- Le point d'abscisse $ x_0 = -5 $ est un point d'inflexion au courbe $ (C_f) $ de car $ f''(-5) = 0 $ et $ f' $ change de signe au voisinage de $ x_0 = -5 $.
- Le point d'abscisse $ x_1 = 2 $ n'est pas un point d'inflexion au courbe $ (C_f) $ de $ f $ car $ f'' $ change de signe au voisinage de $ x_1 = 2 $.

### VIII. Centre de symétrie – axe de symétrie de la courbe d'une fonction :

#### A. Centre de symétrie de la courbe d'une fonction :

Soit $ (C_f) $ la courbe représentative d'une fonction définie sur $ D $ dans un plan $ (P) $ est rapporté à un repère orthonormé $ (O, i, j) $.

Le point $ I(a, b) $ est centre de symétrie au courbe $ (C_f) $ $ \Leftrightarrow $

$$
\begin{cases}
\forall x \in D_r : 2a - x \in D_r \\
\forall x \in D_r : f(2a - x) + f(x) = 2b
\end{cases}
$$

[Diagram: A graph showing a function's curve with a point marked at (x, y) and a dashed line indicating a symmetry axis. The graph includes a table of values for x and f(x), and a point labeled A(x₀, f(x₀)) with a tangent line. The graph also shows the curve (C_f) and the point I(a, b) as the center of symmetry.]

#### Propriété :

Soit $ (C_f) $ la courbe représentative d'une fonction définie sur $ D $ dans un plan $ (P) $ est rapporté à un repère orthonormé $ (O, i, j) $.

Le point $ I(a, b) $ est centre de symétrie au courbe $ (C_f) $ $ \Leftrightarrow $

$$
\begin{cases}
\forall x \in D_r : 2a - x \in D_r \\
\forall x \in D_r : f(2a - x) + f(x) = 2b
\end{cases}
$$


---


<!-- Page 10 -->

# Niveau: 2 P.C. + 2 S.V.- COURS

## dérivation – étude des fonctions

### page 10

### b. Exemple :

[Diagram: A graph showing a function f(x) with its graph C_f, a vertical line x=1, and a line y=x+1. The graph has a point M on the line y=x+1 and a point M' on the graph C_f. The line x=1 is shown as a vertical line, and the point M' is the reflection of M across this line. The graph of f(x) is a parabola, and the point M is the vertex of the parabola.]

### B. axe de symétrie de la courbe d’une fonction :

#### a. Propriété :

**Soit** $\left(C_{f}\right)$ **la courbe représentative d’une fonction définie sur** $D_{f}$ **dans un plan** $\left(P\right)$ **est rapporté à un repère orthonormé** $\left(O,i,j\right)$.

**La droite d’équation** $D:x=a$ **est axe de symétrie au courbe** $\left(C_{f}\right)$ $\Longleftrightarrow$ $\left\{\begin{array}{l}\forall x\in D_{f} \ ; \ 2a-x\in D_{f} \\ \forall x\in D_{f} \ ; \ f(2a-x)=f(x)\end{array}\right.$

#### b. Exemple :

[Diagram: A graph showing a function f(x) with its graph C_f, a vertical line x=a, and a point M on the graph. The graph has a point M' on the graph C_f. The line x=a is shown as a vertical line, and the point M' is the reflection of M across this line. The graph of f(x) is a parabola, and the point M is the vertex of the parabola.]

### IX. Branches infinies d’une fonction :

#### A. Branches infinies :

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


---


<!-- Page 11 -->

# Niveau: 2 P.C. + 2 S.V.- COURS

## dérivation – étude des fonctions

### a. Définition :

Soit $\left(C_f\right)$ la courbe représentative d'une fonction définie sur $D_f$ dans un plan $(P)$ est rapporté à un repère $\left(O,i,j\right)$.

Si au moins une des coordonnées d’un point $M$ de la courbe de $\left(C_f\right)$ tend vers l'infinie on dit que la courbe $\left(C_f\right)$ admet une branche infinie.

### B. Asymptote verticale :

#### a. Définition :

Soit $\left(C_f\right)$ la courbe représentative d'une fonction définie sur $D_f$ dans un plan $(P)$ est rapporté à un repère $\left(O,i,j\right)$.

Si $\lim_{x \to a} f(x) = \pm \infty$ et $\lim_{x \to a} f(x) = \pm \infty$ alors la droite d'équation $x = a$ est une asymptote verticale à $\left(C_f\right)$ (à droite de $a$ ou à gauche de $a$).

#### b. Exemple :

Exemple : asymptote verticale d'équation $x = 1$.

[Diagram: A graph showing a curve with a vertical asymptote at $x = 1$, with the curve approaching the line $x = 1$ as $x$ approaches 1 from the left and right.]

### C. Asymptote horizontale

#### a. Définition :

Soit $\left(C_f\right)$ la courbe représentative d'une fonction définie sur $D_f$ (tel que $\left[a, +\infty\right] \subset D_f$ ou $\left]-\infty, a\right] \subset D_f$) dans un plan $(P)$ est rapporté à un repère $\left(O,i,j\right)$.

Si $\lim_{x \to \pm \infty} f(x) = b$ (ou $\lim_{x \to \pm \infty} f(x) = c$) alors la droite d'équation $y = b$ (ou $y = c$) est une asymptote horizontale à $\left(C_f\right)$ au voisinage de $\pm \infty$.

#### b. Exemple :

Asymptote horizontale d'équation $y = 2$ au voisinage de $\pm \infty$.

[Diagram: A graph showing a curve with a horizontal asymptote at $y = 2$, with the curve approaching the line $y = 2$ as $x$ approaches $\pm \infty$.]


---


<!-- Page 12 -->

# Niveau: 2 P.C. + 2 S.V.- COURS dérivation – étude des fonctions page 12

## D. Asymptote oblique :

### a. Définition :

- Soit $\left(C_{r}\right)$ la courbe représentative d'une fonction définie sur $D_{r}$ (tel que $\left[a, +\infty\right] \subset D_{r}$ ou $\left]-\infty, a\right] \subset D_{r}$ dans un plan $(P)$ est rapporté à un repère $\left(O, i, j\right)$.
- $a \in \mathbb{R}$ ( $a \neq 0$ et $a \neq \pm \infty$) et $b \in \mathbb{R}$
- Si $\lim_{x \to \pm \infty} \left(f(x) - (ax + b)\right) = 0$ alors la droite d'équation $y = ax + b$ est une asymptote oblique à $\left(C_{r}\right)$ au voisinage de $\pm \infty$.

### b. Exemple :

Soit $f(x) = x + 3 - \frac{(x + 7)}{(x - 1)}$.

[Diagram: A graph showing two curves, one labeled $y = x + 4$ and another labeled $y = x + 3$, with a dashed line representing the asymptote $y = x + 3$. The graph of $f(x)$ is shown with a vertical asymptote at $x = 1$.]

$\left(C_{r}\right)$ admet une asymptote oblique la droite d'équation $y = x + 3$ au voisinage de $\pm \infty$.

### c. Propriété :

Si la droite d'équation $y = ax + b$ est une asymptote oblique à $\left(C_{r}\right)$ au voisinage de $\pm \infty$, donc pour déterminer $a$ et $b$ on calcule les limites suivantes :

- Pour déterminer $a$ on calcule : $\lim_{x \to \pm \infty} \frac{f(x)}{x} = a \in \mathbb{R}^*$ (c.a.d. $a \neq 0$ et $a \neq \pm \infty$), donc on a deux cas particuliers.
- Pour déterminer $a$ on calcule : $\lim_{x \to \pm \infty} \left(f(x) - ax\right) = b \in \mathbb{R}$ (c.a.d. $b \neq \pm \infty$), donc on a la troisième cas particulière.

### Les cas particuliers :

- **1$^{er}$ cas particulier :** $a = \pm \infty$ on dit que $\left(C_{r}\right)$ admet une branche parabolique de direction (B.P.D.) l'axe des ordonnées.
- **2$^{e}$ cas particulier :** $a = 0$ on dit que $\left(C_{r}\right)$ admet une branche parabolique de direction (B.P.D.) l'axe des abscisses.
- **3$^{e}$ cas particulier :** $b = \pm \infty$ avec $a \in \mathbb{R}^*$, on dit que $\left(C_{r}\right)$ admet une branche parabolique de direction (B.P.D.) la droite d'équation $y = ax$.


---


<!-- Page 13 -->

# Niveau: 2 P.C. + 2 S.V.- COURS

## dérivation – étude des fonctions

### les cas particuliers ( Remarque : B.P.D= branche parabolique de direction )

#### cas particulier 1 : a = ±∞

$\left(\begin{array}{c} C_{a} \end{array}\right)$ admet une B.P.D l’axe des ordonnées

Exemple: $f(x) = x^3$

[Diagram: A graph of the function $f(x) = x^3$ with a vertical asymptote at $x = 0$, showing the curve approaching infinity as $x$ approaches $0$ from the right and negative infinity from the left.]

#### cas particulier 2 : a = 0

$\left(\begin{array}{c} C_{a} \end{array}\right)$ admet une B.P.D l’axe des abscisses

Exemple: $f(x) = \sqrt{x}$

[Diagram: A graph of the function $f(x) = \sqrt{x}$ with a horizontal asymptote at $y = 0$, showing the curve approaching the x-axis as $x$ approaches $0$ from the right.]

#### cas particulier 3 : a ∈ ℝ* et b = ±∞

$\left(\begin{array}{c} C_{a} \end{array}\right)$ admet une B.P.D la droite

Exemple: $f(x) = x + \sqrt{x - 3}$

[Diagram: A graph of the function $f(x) = x + \sqrt{x - 3}$ with a vertical asymptote at $x = 3$, showing the curve approaching infinity as $x$ approaches $3$ from the right.]

### Approximation affine d'une fonction dérivable en un point. (complément)

#### Définition :

$f$ est une fonction dérivable au point $a$

- La fonction $u$ tel que: $u : x \to f(x) + (x - a)f'(a)$ (ou encore $(x - a)h$); $v : h \to f(a) + hf'(a)$) est appelée la fonction affine tangente à la fonction $f$ au point $a$.

- Quand $x$ est très proche de $a$ le nombre $f(a) + (x - a)f'(a)$ est une approximation affine de $f(x)$ au voisinage de $a$ on écrit : $f(x) \approx f(a) + (x - a)f'(a)$.

- Or encore le nombre $f(a) + hf'(a)$ est approximation affine de $f(a + h)$ au voisinage de zéro on écrit $f(a + h) \approx f(a) + hf'(a)$ avec $x - a = h$.

### Exemple :

#### Exemple 1 :

Trouver une approximation affine du nombre $f(1 + h)$ avec $f(x) = x^2$ et $a = 1$.

**Correction :**

$f$ est une fonction dérivable au point 1 avec $f'(1) = 2$ approximation affine de $f(1 + h)$ est :

$f(1 + h) \approx f'(1) + f(1) \approx 2h + 1$

Conclusion: $f(1 + h) = (1 + h)^2 \approx 2h + 1$.

**Application du résultat :**

On prend $h = 0,001$ d'où : $f(1 + 0,001) = f(1 + 0,001) \approx 2 \times 0,001 + 1$ donc $f(1 + 0,001) \approx 1,002$.

On vérifie : $f(1,001) = (1,001)^2 = 1,002001$ donc $1,002 \approx 1,002001$.

### Propriété :

- La fonction $u$ tel que: $u : x \to f(x) + (x - a)f'(a)$ (ou encore $(x - a)h$); $v : h \to f(a) + hf'(a)$) est appelée la fonction affine tangente à la fonction $f$ au point $a$.

- Quand $x$ est très proche de $a$ le nombre $f(a) + (x - a)f'(a)$ est une approximation affine de $f(x)$ au voisinage de $a$ on écrit : $f(x) \approx f(a) + (x - a)f'(a)$.

- Or encore le nombre $f(a) + hf'(a)$ est approximation affine de $f(a + h)$ au voisinage de zéro on écrit $f(a + h) \approx f(a) + hf'(a)$ avec $x - a = h$.

### Remarque :

- $f$ est une fonction dérivable au point $a$

- La fonction $u$ tel que: $u : x \to f(x) + (x - a)f'(a)$ (ou encore $(x - a)h$); $v : h \to f(a) + hf'(a)$) est appelée la fonction affine tangente à la fonction $f$ au point $a$.

- Quand $x$ est très proche de $a$ le nombre $f(a) + (x - a)f'(a)$ est une approximation affine de $f(x)$ au voisinage de $a$ on écrit : $f(x) \approx f(a) + (x - a)f'(a)$.

- Or encore le nombre $f(a) + hf'(a)$ est approximation affine de $f(a + h)$ au voisinage de zéro on écrit $f(a + h) \approx f(a) + hf'(a)$ avec $x - a = h$.

### Exemple :

#### Exemple 1 :

Trouver une approximation affine du nombre $f(1 + h)$ avec $f(x) = x^2$ et $a = 1$.

**Correction :**

$f$ est une fonction dérivable au point 1 avec $f'(1) = 2$ approximation affine de $f(1 + h)$ est :

$f(1 + h) \approx f'(1) + f(1) \approx 2h + 1$

Conclusion: $f(1 + h) = (1 + h)^2 \approx 2h + 1$.

**Application du résultat :**

On prend $h = 0,001$ d'où : $f(1 + 0,001) = f(1 + 0,001) \approx 2 \times 0,001 + 1$ donc $f(1 + 0,001) \approx 1,002$.

On vérifie : $f(1,001) = (1,001)^2 = 1,002001$ donc $1,002 \approx 1,002001$.

### Exercice :

#### Exercice 1 :

Trouver une approximation affine du nombre $f(1 + h)$ avec $f(x) = x^2$ et $a = 1$.

**Correction :**

$f$ est une fonction dérivable au point 1 avec $f'(1) = 2$ approximation affine de $f(1 + h)$ est :

$f(1 + h) \approx f'(1) + f(1) \approx 2h + 1$

Conclusion: $f(1 + h) = (1 + h)^2 \approx 2h + 1$.

**Application du résultat :**

On prend $h = 0,001$ d'où : $f(1 + 0,001) = f(1 + 0,001) \approx 2 \times 0,001 + 1$ donc $f(1 + 0,001) \approx 1,002$.

On vérifie : $f(1,001) = (1,001)^2 = 1,002001$ donc $1,002 \approx 1,002001$.

### Propriété :

- La fonction $u$ tel que: $u : x \to f(x) + (x - a)f'(a)$ (ou encore $(x - a)h$); $v : h \to f(a) + hf'(a)$) est appelée la fonction affine tangente à la fonction $f$ au point $a$.

- Quand $x$ est très proche de $a$ le nombre $f(a) + (x - a)f'(a)$ est une approximation affine de $f(x)$ au voisinage de $a$ on écrit : $f(x) \approx f(a) + (x - a)f'(a)$.

- Or encore le nombre $f(a) + hf'(a)$ est approximation affine de $f(a + h)$ au voisinage de zéro on écrit $f(a + h) \approx f(a) + hf'(


---


<!-- Page 14 -->

# Niveau: 2 P.C. + 2 S.V.- COURS

## dérivation – étude des fonctions

### Technique de calcule : $\left(1+h\right)^2$ avec h très proche de zéro on calcule $2h+1$.

### Exemple 2 :

#### 1. Trouver une approximation affine du nombre $\sqrt{9,002}$.

**Correction :**

On pose $f(x) = \sqrt{x}$ et $a = 9$ et $h = 0,002$ d’où $\sqrt{9,002} = f(9 + 0,002)$.

On calcule le nombre dérivé de $f$ en 9 on a :

$$
\lim_{h \to 0} \frac{f(9+h) - f(9)}{h} = \lim_{x \to 9} \frac{f(x) - f(9)}{x - 9} = \lim_{x \to 9} \frac{\sqrt{x} - 3}{x - 9} = \lim_{x \to 9} \frac{\sqrt{x} - 3}{\left(\sqrt{x} - 3\right)\left(\sqrt{x} + 3\right)} = \lim_{x \to 9} \frac{1}{\sqrt{x} + 3} = \frac{1}{6} \in \mathbb{R}
$$

D’où: $f$ est dérivable au point 9 et le nombre dérivé en 9 est $f'(9) = \frac{1}{6}$.

On trouve une approximation affine du nombre $\sqrt{9,002}$.

On a: $f(a + h) \approx f(a) + h f'(a)$ d’où $f(9 + 0,002) \approx f(9) + 0,002 \times f'(9)$.

Donc: $f(9 + 0,002) \approx \sqrt{9} + 0,002 \times \frac{1}{6} = \frac{9}{6} + \frac{1}{6} \times 0,002 = 1,5 + 0,000333333$.

Par suite $f(9 + 0,002) \approx 3,000333333$.

On calcule $f(9 + 0,002) \approx 3,000333333$ la calculatrice donne: $\sqrt{9,002} \approx 3,000333315$ d’où la précision est $3 \times 10^{-8}$.

### Remarque :

- Pour la fonction $f(x) = x^2$ et $a = 1$ on a: $f(1 + h) = (1 + h)^2 \approx 1 + 2h$.
- Pour la fonction $f(x) = x^3$ et $a = 1$ on a: $f(1 + h) = (1 + h)^3 \approx 1 + 3h$.
- Pour la fonction $f(x) = \sqrt{x}$ et $a = 1$ on a: $f(1 + h) = \sqrt{1 + h} \approx 1 + \frac{h}{2}$.
- Pour la fonction $f(x) = \frac{1}{x}$ et $a = 1$ on a: $f(1 + h) = \frac{1}{1 + h} \approx 1 - h$.

### XI. Résumé des branches infinies :

- **Définition :**
  $f(x) = x^2$ et $a = 1$ on a: $f(1 + h) = (1 + h)^2 \approx 1 + 2h$.

- **Théorème :**
  $f(x) = x^3$ et $a = 1$ on a: $f(1 + h) = (1 + h)^3 \approx 1 + 3h$.

- **Démonstration :**
  $f(x) = \sqrt{x}$ et $a = 1$ on a: $f(1 + h) = \sqrt{1 + h} \approx 1 + \frac{h}{2}$.

- **Exemple X :**
  $f(x) = \frac{1}{x}$ et $a = 1$ on a: $f(1 + h) = \frac{1}{1 + h} \approx 1 - h$.

- **Propriété :**
  $f(x) = x^2$ et $a = 1$ on a: $f(1 + h) = (1 + h)^2 \approx 1 + 2h$.

- **Remarque :**
  $f(x) = x^3$ et $a = 1$ on a: $f(1 + h) = (1 + h)^3 \approx 1 + 3h$.

- **Remarque :**
  $f(x) = \sqrt{x}$ et $a = 1$ on a: $f(1 + h) = \sqrt{1 + h} \approx 1 + \frac{h}{2}$.

- **Remarque :**
  $f(x) = \frac{1}{x}$ et $a = 1$ on a: $f(1 + h) = \frac{1}{1 + h} \approx 1 - h$.

- **Remarque :**
  $f(x) = x^2$ et $a = 1$ on a: $f(1 + h) = (1 + h)^2 \approx 1 + 2h$.

- **Remarque :**
  $f(x) = x^3$ et $a = 1$ on a: $f(1 + h) = (1 + h)^3 \approx 1 + 3h$.

- **Remarque :**
  $f(x) = \sqrt{x}$ et $a = 1$ on a: $f(1 + h) = \sqrt{1 + h} \approx 1 + \frac{h}{2}$.

- **Remarque :**
  $f(x) = \frac{1}{x}$ et $a = 1$ on a: $f(1 + h) = \frac{1}{1 + h} \approx 1 - h$.

- **Remarque :**
  $f(x) = x^2$ et $a = 1$ on a: $f(1 + h) = (1 + h)^2 \approx 1 + 2h$.

- **Remarque :**
  $f(x) = x^3$ et $a = 1$ on a: $f(1 + h) = (1 + h)^3 \approx 1 + 3h$.

- **Remarque :**
  $f(x) = \sqrt{x}$ et $a = 1$ on a: $f(1 + h) = \sqrt{1 + h} \approx 1 + \frac{h}{2}$.

- **Remarque :**
  $f(x) = \frac{1}{x}$ et $a = 1$ on a: $f(1 + h) = \frac{1}{1 + h} \approx 1 - h$.

- **Remarque :**
  $f(x) = x^2$ et $a = 1$ on a: $f(1 + h) = (1 + h)^2 \approx 1 + 2h$.

- **Remarque :**
  $f(x) = x^3$ et $a = 1$ on a: $f(1 + h) = (1 + h)^3 \approx 1 + 3h$.

- **Remarque :**
  $f(x) = \sqrt{x}$ et $a = 1$ on a: $f(1 + h) = \sqrt{1 + h} \approx 1 + \frac{h}{2}$.

- **Remarque :**
  $f(x) = \frac{1}{x}$ et $a = 1$ on a: $f(1 + h) = \frac{1}{1 + h} \approx 1 - h$.

- **Remarque :**
  $f(x) = x^2$ et $a = 1$ on a: $f(1 + h) = (1 + h)^2 \approx 1 + 2h$.

- **Remarque :**
  $f(x) = x^3$ et $a = 1$ on a: $f(1 + h) = (1 + h)^3 \approx 1 + 3h$.

- **Remarque :**
  $f(x) = \sqrt{x


---


<!-- Page 15 -->

# Niveau: 2 P.C. + 2 S.V.- COURS

## dérivation – étude des fonctions

### Les branches infinies

#### Asymptote horizontale

$$
\lim_{x \to \pm\infty} f(x) = a
$$

**Définition :**
(C₁) admet une asymptote horizontale c'est la droite d'équation $y = a$ au voisinage de $\pm\infty$

**Exemple :**
asymptote horizontale d'équation $y = 2$ au voisinage de $\pm\infty$

[Diagram: Graphique de la fonction $f(x) = 2$ avec une asymptote horizontale en $y = 2$]

#### Asymptote oblique et les trois cas particuliers

$$
\lim_{x \to \pm\infty} f(x) = \pm\infty
$$

**Cas particulier 1 :**
(C₁) admet une B.P.D. l'axe des ordonnées
$y = 0$
$y = x^2$
$y = x^3$

**Cas particulier 2 :**
(C₁) admet une B.P.D. l'axe des abscisses
$y = ax$
$y = x\sqrt{x}$

**Cas particulier 3 :**
(C₁) admet une asymptote oblique la droite d'équation $y = ax + b$
voisinage de $\pm\infty$
$y = x + 2$
$y = x + 7$
$y = x + 7$
$y = x + 7$

**Exemple :**
$f(x) = x + \sqrt{x - 3}$

**Exemple :**
$f(x) = x + \sqrt{x - 3}$

**Remarque :**
B.P.D. = branche parabolique de direction

#### Asymptote verticale

$$
\lim_{x \to \pm\infty} f(x) = \pm\infty
$$

**Définition :**
(C₁) admet une asymptote verticale c'est la droite d'équation $x = a$

**Exemple :**
asymptote verticale d'équation $x = 1$

[Diagram: Graphique de la fonction $f(x) = \frac{1}{x-1}$ avec une asymptote verticale en $x = 1$]

### Cas particuliers

#### Cas particulier 1 :
(C₁) admet une B.P.D. l'axe des ordonnées
$y = 0$
$y = x^2$
$y = x^3$

#### Cas particulier 2 :
(C₁) admet une B.P.D. l'axe des abscisses
$y = ax$
$y = x\sqrt{x}$

#### Cas particulier 3 :
(C₁) admet une asymptote oblique la droite d'équation $y = ax + b$
voisinage de $\pm\infty$
$y = x + 2$
$y = x + 7$
$y = x + 7$

**Exemple :**
$f(x) = x + \sqrt{x - 3}$

**Exemple :**
$f(x) = x + \sqrt{x - 3}$

**Remarque :**
B.P.D. = branche parabolique de direction

### Rq : position relative de (C₁) et (D) on étudie le signe de $f(x) - (ax + b)$

[Diagram: Graphique de la fonction $f(x) = x + \sqrt{x - 3}$ avec une asymptote oblique en $y = x + 2$]

### Exercice :
Étudier la limite de $f(x)$ en $x \to \pm\infty$ pour les fonctions suivantes :

1. $f(x) = x + \sqrt{x - 3}$
2. $f(x) = x + \sqrt{x - 3}$

### Propriété :
(C₁) admet une asymptote oblique la droite d'équation $y = ax + b$
voisinage de $\pm\infty$
$y = x + 2$
$y = x + 7$
$y = x + 7$

**Exemple :**
$f(x) = x + \sqrt{x - 3}$

**Exemple :**
$f(x) = x + \sqrt{x - 3}$

**Remarque :**
B.P.D. = branche parabolique de direction

### Exercice :
Étudier la limite de $f(x)$ en $x \to \pm\infty$ pour les fonctions suivantes :

1. $f(x) = x + \sqrt{x - 3}$
2. $f(x) = x + \sqrt{x - 3}$

### Propriété :
(C₁) admet une asymptote oblique la droite d'équation $y = ax + b$
voisinage de $\pm\infty$
$y = x + 2$
$y = x + 7$
$y = x + 7$

**Exemple :**
$f(x) = x + \sqrt{x - 3}$

**Exemple :**
$f(x) = x + \sqrt{x - 3}$

**Remarque :**
B.P.D. = branche parabolique de direction

### Exercice :
Étudier la limite de $f(x)$ en $x \to \pm\infty$ pour les fonctions suivantes :

1. $f(x) = x + \sqrt{x - 3}$
2. $f(x) = x + \sqrt{x - 3}$

### Propriété :
(C₁) admet une asymptote oblique la droite d'équation $y = ax + b$
voisinage de $\pm\infty$
$y = x + 2$
$y = x + 7$
$y = x + 7$

**Exemple :**
$f(x) = x + \sqrt{x - 3}$

**Exemple :**
$f(x) = x + \sqrt{x - 3}$

**Remarque :**
B.P.D. = branche parabolique de direction

### Exercice :
Étudier la limite de $f(x)$ en $x \to \pm\infty$ pour les fonctions suivantes :

1. $f(x) = x + \sqrt{x - 3}$
2. $f(x) = x + \sqrt{x - 3}$

### Propriété :
(C₁) admet une asymptote oblique la droite d'équation $y = ax + b$
voisinage de $\pm\infty$
$y = x + 2$
$y = x + 7$
$y = x + 7$

**Exemple :**
$f(x) = x + \sqrt{x - 3}$

**Exemple :**
$f(x) = x + \sqrt{x - 3}$

**Remarque :**
B.P.D. = branche parabolique de direction

### Exercice :
Étudier la limite de $f(x)$ en $x \to \pm\infty$ pour les fonctions suivantes :

1. $f(x) = x + \sqrt{x - 3}$
2. $f(x) = x + \sqrt{x - 3}$

### Propriété :
(C₁) admet une asymptote oblique la droite d'équation $y = ax + b$
voisinage de $\pm\infty$
$y = x + 2$
$y = x + 7$
$y = x + 7$

**Exemple :**
$f(x) = x + \sqrt{x - 3}$

**Exemple :**
$f(x) = x + \sqrt{x - 3}$

**Remarque :**
B.P.D. = branche parabolique de direction

### Exercice :
Étudier la limite de $f(x)$ en $x \to \pm\infty$ pour les fonctions suivantes :

1. $f(x) = x + \sqrt{x - 3}$
2. $f(x) = x + \sqrt{x - 3}$

### Propriété :
(C₁) admet une asymptote oblique la droite d'équation $y = ax + b$
voisinage de $\pm\infty$
$y = x + 2$
$y = x + 7$
$y = x + 7$

**Exemple :**
$f(x) = x + \sqrt{x - 3}$

**Exemple :**
$f(x) = x + \sqrt{x - 3}$

**Remarque :**
B.P.D. = branche parabolique


---

