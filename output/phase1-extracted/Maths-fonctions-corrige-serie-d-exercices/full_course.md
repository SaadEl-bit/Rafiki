<!-- Page 1 -->

# Exercices avec solutions : LA DERIVATION

## Exercice 1

### 1- Montrer en utilisant la définition que la fonction $ f(x) = x^2 + x - 3 $ est dérivable en $ a = -2 $.

On dit que $ f $ est dérivable à droite en 0

$$
\lim_{x \to 0^+} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^+} \frac{x^2 + x - 3}{x} = \lim_{x \to 0^+} (x + 1) = 1 = f'(0)
$$

1 s'appelle le nombre dérivé de la fonction $ f $ à gauche de 0

On dit que $ f $ est dérivable à gauche en 0

$$
\lim_{x \to 0^-} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^-} \frac{x^2 + x - 3}{x} = \lim_{x \to 0^-} (x + 1) = 1 = f'(0)
$$

Mais on a : $ f'(0) \neq 0 $

Donc $ f $ n'est pas dérivable en 0.

### 2) Soit $ f $ une fonction définie par :

$$
f(x) = \begin{cases}
x^2 + x + 3 & \text{si } x \geq 1 \\
\frac{1}{x^2} + \frac{3}{4} & \text{si } x < 1
\end{cases}
$$

étudier la dérivabilité de $ f $ en $ x_0 = 1 $

### 3) Soit la fonction définie sur $ \mathbb{R} $ par :

$$
f(x) = \begin{cases}
3x^2 & \text{si } x < 0 \\
x & \text{si } 0 \leq x < 1 \\
-2x^2 + 3x & \text{si } x \geq 0
\end{cases}
$$

étudier la dérivabilité de $ f $ en $ x_0 = 0 $

### Solution :

1) $ \lim_{x \to 2} \frac{f(x) - f(2)}{x - 2} = \lim_{x \to 2} \frac{x^2 + x - 3}{x + 2} = \lim_{x \to 2} \frac{x^2 - x - 3}{x + 2} = \lim_{x \to 2} \frac{(x - 3)(x + 1)}{x + 2} $

$$
= \lim_{x \to 2} \frac{(x + 2)(x - 3)}{x + 2} = \lim_{x \to 2} (x - 3) = -1
$$

Donc $ f $ est dérivable en -2 et $ f'(-2) = -1 $

2) $ \lim_{x \to 1^+} \frac{f(x) - f(1)}{x - 1} = \lim_{x \to 1^+} \frac{x^2 + x - 3}{x - 1} = \lim_{x \to 1^+} \frac{(x - 1)(x + 1)}{x - 1} = \lim_{x \to 1^+} (x + 1) = 2 $

Donc $ f $ est dérivable à droite en 1

3) $ \lim_{x \to 0^+} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^+} \frac{3x^2}{x} = \lim_{x \to 0^+} 3x = 0 $

Donc $ f $ est dérivable en 0 et $ f'(0) = 0 $

### Exercice 2 :

### 1) Déterminer le domaine de définition de $ f $

### 2) Étudier la dérivabilité de $ f $ à droite en $ x_0 = 0 $ et donner une interprétation géométrique du résultat

### 3) Étudier la dérivabilité de $ f $ à gauche et à droite en $ x_0 = 1 $ et donner une interprétation géométrique

### Solution :

1) $ x \in D_f \Leftrightarrow 1 - x^2 \geq 0 \text{ et } 0 \leq x^1 $

$$
x \in D_f \Leftrightarrow -1 \leq x \leq 1 \text{ ou } x > 1
$$

$$
x \in D_f \Leftrightarrow x \in [-1, 1] \cup (1, \infty]
$$

$$
\text{donc } D_f = [0, \infty] \cup [-1, 1]
$$

2) Étude de la dérivabilité de $ f $ à droite de $ x_0 = 0 $

$$
\lim_{x \to 0^+} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^+} \frac{1}{x} = \infty
$$

$$
\lim_{x \to 0^+} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^+} \frac{1}{x} = \infty
$$

$$
\lim_{x \to 0^+} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^+} \frac{1}{x} = \infty
$$

$$
\lim_{x \to 0^+} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^+} \frac{1}{x} = \infty
$$

$$
\lim_{x \to 0^+} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^+} \frac{1}{x} = \infty
$$

$$
\lim_{x \to 0^+} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^+} \frac{1}{x} = \infty
$$

$$
\lim_{x \to 0^+} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^+} \frac{1}{x} = \infty
$$

$$
\lim_{x \to 0^+} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^+} \frac{1}{x} = \infty
$$

$$
\lim_{x \to 0^+} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^+} \frac{1}{x} = \infty
$$

$$
\lim_{x \to 0^+} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^+} \frac{1}{x} = \infty
$$

$$
\lim_{x \to 0^+} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^+} \frac{1}{x} = \infty
$$

$$
\lim_{x \to 0^+} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^+} \frac{1}{x} = \infty
$$

$$
\lim_{x \to 0^+} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^+} \frac{1}{x} = \infty
$$

$$
\lim_{x \to 0^+} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0^+} \frac{1}{x} = \infty
$$

$$
\lim_{x \to 0^+} \frac{f(x) - f(0)}{x - 0} = \


---


<!-- Page 2 -->

# 3)a)étude de la dérivabilité de f à gauche en x₀ = 1

On a : $f(x) = |x|$, soit $0 \leq x \leq 1$

$$
f(x) - f(1) = \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1}
$$

Et puisque :
$$
\lim_{x \to 1^-} \sqrt{1-x^2} = 0 \quad \text{et} \quad \lim_{x \to 1^-} (1+x)^2 = 4
$$

Alors :
$$
\lim_{x \to 1^-} \frac{f(x) - f(1)}{x - 1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x)\sqrt{1-x^2}}{x-1} = \lim_{x \to 1^-} \frac{(1+x)\sqrt{1-x^2} - (1+x


---


<!-- Page 3 -->

# Exercice 6

## Étude de la fonction dérivée

### Exercice 6 : Etudier le domaine de dérivation de $ f $ et déterminer sa fonction dérivée dans les cas suivants :

1) $ f(x) = x^2 + 3x - 1 $

2) $ f(x) = 4 \sin x $

3) $ f(x) = 4x \sin x $ avec $ u(x) = \sin x $

4) $ f(x) = \sqrt{x} + x $ avec $ u(x) = \sqrt{x} $ et $ v(x) = x $

5) $ f(x) = \frac{1}{\sqrt{x}} $

6) $ f(x) = \frac{6}{4x^3 + 3x - 1} $

7) $ f(x) = \frac{4x - 3}{2x - 1} $

8) $ f(x) = \sqrt{x^2 - 4} $

### Solution 1 : $ f(x) = x^2 + 3x - 1 $

- $ f $ est une fonction polynomiale donc dérivable sur $ \mathbb{R} $
- $ f'(x) = 2x + 3 $
- $ D_f = \mathbb{R} $

### Solution 2 : $ f(x) = 4 \sin x $

- $ f $ est une fonction trigonométrique donc dérivable sur $ \mathbb{R} $
- $ f'(x) = 4 \cos x $
- $ D_f = \mathbb{R} $

### Solution 3 : $ f(x) = 4x \sin x $ avec $ u(x) = \sin x $

- $ f $ est une fonction dérivable sur $ \mathbb{R} $ alors $ f $ est une fonction dérivable sur $ \mathbb{R} $
- $ f'(x) = 4 \sin x + 4x \cos x $
- $ D_f = \mathbb{R} $

### Solution 4 : $ f(x) = \sqrt{x} + x $ avec $ u(x) = \sqrt{x} $ et $ v(x) = x $

- $ f $ est une fonction dérivable sur $ \mathbb{R}^+ $ alors $ f $ est une fonction dérivable sur $ \mathbb{R}^+ $
- $ f'(x) = \frac{1}{2\sqrt{x}} + 1 $
- $ D_f = \mathbb{R}^+ $

### Solution 5 : $ f(x) = \frac{1}{\sqrt{x}} $

- $ f $ est une fonction dérivable sur $ \mathbb{R}^+ $
- $ f'(x) = -\frac{1}{2x^{3/2}} $
- $ D_f = \mathbb{R}^+ $

### Solution 6 : $ f(x) = \frac{6}{4x^3 + 3x - 1} $

- $ f $ est une fonction rationnelle alors il est dérivable sur $ D_f = \mathbb{R} \setminus \left\{ -\frac{1}{4} \right\} $
- $ f'(x) = \frac{-6(12x^2 + 3)}{(4x^3 + 3x - 1)^2} $
- $ D_f = \mathbb{R} \setminus \left\{ -\frac{1}{4} \right\} $

### Solution 7 : $ f(x) = \frac{4x - 3}{2x - 1} $

- $ f $ est une fonction rationnelle alors il est dérivable sur $ D_f = \mathbb{R} \setminus \left\{ \frac{1}{2} \right\} $
- $ f'(x) = \frac{4(2x - 1) - (4x - 3) \cdot 2}{(2x - 1)^2} $
- $ D_f = \mathbb{R} \setminus \left\{ \frac{1}{2} \right\} $

### Solution 8 : $ f(x) = \sqrt{x^2 - 4} $

- $ f $ est une fonction dérivable sur $ D_f = [-2, 2] $
- $ f'(x) = \frac{x}{\sqrt{x^2 - 4}} $
- $ D_f = [-2, 2] $

### Remarque :

- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $
- $ f $ est une fonction dérivable sur $ D_f $ si et seulement si $ f $ est dérivable sur $ D_f $


---


<!-- Page 4 -->

# M3allem

## Exercice 7 : Déterminer les fonctions dérivées des fonctions suivantes :

1) $f(x) = \sin(2x^2 - 1)$

2) $f(x) = \cos\left(\frac{1}{x^2 + 2}\right)$

3) $f(x) = \tan(\cos(x))$

## Exercice 8 : Soit la fonction définie sur $\mathbb{R}$ par $f(x) = \cos(x)$

1) Montrer que $f$ est une bijection de $[0, \pi]$ vers $[-1, 1]$

2) Calculer : $\left(f^{-1}\right)'(0)$

## Exercice 9 : soit $f$ une fonction définie par : $f(x) = x^3 + x$

1) Dresser le tableau de variation de $f$

2) Montrer que $f$ est une bijection de $\mathbb{R}^*$ vers $\mathbb{R}^*$

3) Déterminer $f^{-1}(2)$

## Exercice 10 : Soit la fonction $g(x) = \cos(2x)$

1) Dresser le tableau de variation de $g$ dans $[0, \pi/2]$

2) Montrer que $g$ est une bijection de $[0, \pi/2]$ vers $[-1, 1]$

## Exercice 11 : Déterminer les domaines des fonctions suivantes :

1) $f(x) = \sqrt[3]{x^2 + x - 4}$

2) $f(x) = \sqrt{\frac{2x - 1}{x^2 - x}}$

## Exercice 12 : résoudre dans $\mathbb{R}$ les équations suivantes :

$(E_1) : \sqrt{3}x + \sqrt{3}x - \sqrt{3}x = \sqrt{9 - x^2}$

$(E_2) : 2x\sqrt{-3x^2 + 3x} = 20$

## Solutions

### 3- Vérifier que $(\forall y \in [0, \pi/2[) \ (g'(y) \neq 0)$ et déterminer $g^{-1}(x)$ pour $x$ dans $] -1, 1[$.

**Solutions :** $g$ est dérivable sur $\mathbb{R}$ et $(\forall x \in \mathbb{R}) (g'(x) \neq 0)$

- Si $x \in [0, \pi/2]$ alors $2x \in [0, \pi]$ et par suite $g'(x) = -2\sin(2x) \geq 0$

- Si $x \in [\pi/2, \pi]$ alors $2x \in [\pi, 2\pi]$ et par suite $g'(x) = -2\sin(2x) \geq 0$

### 2- La fonction $g$ est continue (composition de deux fonctions continues) strictement décroissante de $[0, \pi/2]$ vers $[0, \pi/2]$

$g([0, \pi/2]) = \lim_{x \to \pi/2^-} g(x), \lim_{x \to \pi/2^+} g(x) = 1 - 1$

Donc $g$ est une bijection de $[0, \pi/2]$ vers $] -1, 1[$, soit $g^{-1}$ sa fonction réciproque.

### 3- On a : $g$ est dérivable sur $[0, \pi/2]$

$(\forall x \in [0, \pi/2]) (g'(x) = -2\sin(2x) \neq 0)$ donc $g^{-1}$ est dérivable sur $] -1, 1[$.

Soit $x \in ]-1, 1[$, $(g^{-1})'(x) = \frac{1}{g'(g^{-1}(x))}$

$$
\frac{1}{g'(g^{-1}(x))} = \frac{1}{-2\sin(2g^{-1}(x))} = -\frac{1}{2\sin(2g^{-1}(x))}
$$

$$
= -\frac{1}{2\sqrt{1 - \cos^2(2g^{-1}(x))}} = -\frac{1}{2\sqrt{1 - \left(\frac{1}{\sqrt{1 - x^2}}\right)^2}} = -\frac{1}{2\sqrt{1 - \frac{1}{1 - x^2}}}
$$

$$
= -\frac{1}{2\sqrt{\frac{1 - x^2 - 1}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}}
$$

$$
= -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}}
$$

$$
= -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}}
$$

$$
= -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}}
$$

$$
= -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}}
$$

$$
= -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}}
$$

$$
= -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}}
$$

$$
= -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}}
$$

$$
= -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}}
$$

$$
= -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}}
$$

$$
= -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}}
$$

$$
= -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}}
$$

$$
= -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^2}}} = -\frac{1}{2\sqrt{\frac{-x^2}{1 - x^


---


<!-- Page 5 -->

# Correction :1)
## $\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

Le domaine de définition de l'équation $\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$ est : $\left[ -3; 3 \right]$

On a :
$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x = \sqrt{9 - x^{2}}$

$\left( \frac{3}{x} \right)^{3} - \left( \frac{3}{x} \right)^{3} - x


---


<!-- Page 6 -->

# Exercice 14

## Définition :
Soit $f$ une fonction définie sur $I = [-\pi, \pi[$ par :
$$
f(x) = \begin{cases}
2 \cos x - 1 & \text{si } -\pi < x < 0 \\
\frac{x}{x+1} & \text{si } 0 < x < \pi
\end{cases}
$$

## Théorème :
1) Montrer que $f$ est dérivable en $x_0 = 0$ et donner l'équation de la tangente à la courbe de $f$ en $x_0 = 0$.

2) a) Étudier la dérivabilité de $f$ en $x_0 = -1$
b) Donner les équations des demi-tangentes à la courbe de $f$ en $x_0 = -1$.

## Démonstration :
### 1) Étude de la dérivabilité de $f$ en $x_0 = 0$

$$
\lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{2 \cos x - 1 - 1}{x} = \lim_{x \to 0} \frac{2 \cos x - 2}{x} = \lim_{x \to 0} \frac{-2 \sin x}{x} = -2
$$

$$
\lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{2 \cos x - 1 - 1}{x} = \lim_{x \to 0} \frac{2 \cos x - 2}{x} = \lim_{x \to 0} \frac{-2 \sin x}{x} = -2
$$

$$
\lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{2 \cos x - 1 - 1}{x} = \lim_{x \to 0} \frac{2 \cos x - 2}{x} = \lim_{x \to 0} \frac{-2 \sin x}{x} = -2
$$

$$
\lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{2 \cos x - 1 - 1}{x} = \lim_{x \to 0} \frac{2 \cos x - 2}{x} = \lim_{x \to 0} \frac{-2 \sin x}{x} = -2
$$

$$
\lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{2 \cos x - 1 - 1}{x} = \lim_{x \to 0} \frac{2 \cos x - 2}{x} = \lim_{x \to 0} \frac{-2 \sin x}{x} = -2
$$

$$
\lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{2 \cos x - 1 - 1}{x} = \lim_{x \to 0} \frac{2 \cos x - 2}{x} = \lim_{x \to 0} \frac{-2 \sin x}{x} = -2
$$

$$
\lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{2 \cos x - 1 - 1}{x} = \lim_{x \to 0} \frac{2 \cos x - 2}{x} = \lim_{x \to 0} \frac{-2 \sin x}{x} = -2
$$

$$
\lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{2 \cos x - 1 - 1}{x} = \lim_{x \to 0} \frac{2 \cos x - 2}{x} = \lim_{x \to 0} \frac{-2 \sin x}{x} = -2
$$

$$
\lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{2 \cos x - 1 - 1}{x} = \lim_{x \to 0} \frac{2 \cos x - 2}{x} = \lim_{x \to 0} \frac{-2 \sin x}{x} = -2
$$

$$
\lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{2 \cos x - 1 - 1}{x} = \lim_{x \to 0} \frac{2 \cos x - 2}{x} = \lim_{x \to 0} \frac{-2 \sin x}{x} = -2
$$

$$
\lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{2 \cos x - 1 - 1}{x} = \lim_{x \to 0} \frac{2 \cos x - 2}{x} = \lim_{x \to 0} \frac{-2 \sin x}{x} = -2
$$

$$
\lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{2 \cos x - 1 - 1}{x} = \lim_{x \to 0} \frac{2 \cos x - 2}{x} = \lim_{x \to 0} \frac{-2 \sin x}{x} = -2
$$

$$
\lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{2 \cos x - 1 - 1}{x} = \lim_{x \to 0} \frac{2 \cos x - 2}{x} = \lim_{x \to 0} \frac{-2 \sin x}{x} = -2
$$

$$
\lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{2 \cos x - 1 - 1}{x} = \lim_{x \to 0} \frac{2 \cos x - 2}{x} = \lim_{x \to 0} \frac{-2 \sin x}{x} = -2
$$

$$
\lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{2 \cos x - 1 - 1}{x} = \lim_{x \to 0} \frac{2 \cos x - 2}{x} = \lim_{x \to 0} \frac{-2 \sin x}{x} = -2
$$

$$
\lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{2 \cos x - 1 - 1}{x} = \lim_{x \to 0} \frac{2 \cos x - 2}{x} = \lim_{x \to 0} \frac{-2 \sin x}{x} = -2
$$

$$
\lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{2 \cos x - 1 - 1}{x} = \lim_{x \to 0} \frac{2 \cos x - 2}{x} = \lim_{x \to 0} \frac{-2 \sin x}{x} = -2
$$

$$
\lim_{x \to 0} \frac{f(x) - f(0)}{x - 0} = \lim_{x \to 0} \frac{2 \cos x - 1 - 1}{x}


---


<!-- Page 7 -->

# M3allem

## Définition :

3x-2 > 0 ⇔ x > 2/3 donc la fonction x → g(3x-2) est dérivable sur Df - {2/3}

## Théorème :

donc : f est dérivable sur Df - {2/3} cad Df' = Df - {2/3}

## Démonstration :

∀x ∈ Df :

f'(x) = (g(3x-2))' × h(x) + g(3x-2) × (h(x))'
(g(3x-2))' = (3x-2)' × g(3x-2) = 3 × (1/2√3x-2)
Car : g'(x) = ( √x )' = 1/(2√x)
(h(x))' = 3 × (2x+1)/(x-1) × (2x+1)/(x-1)²
(2x+1)/(x-1) = (2x+1)²/(x-1)²
Donc : f'(x) = (3/2√3x-2) × (2x+1)³ + √3x-2 × (2x+1)²/(x-1)²
f'(−1) = 2018 × (2+1)² × (2+1) = 2018 × 2017 × 2018

## Exemple 1 :

lim (x+2)²⁰¹⁸ / x+1 = lim (x+2)²⁰¹⁸ / (x-1) = f'(-1) = 2018

## Exercice 16 :

### En utilisant la dérivée calculer les limites suivantes :

1) lim (x+2)²⁰¹⁸ / x+1
2) lim 2sinx-1 / x-π/6

## Solution 1 :

on pose : f(x) = (x+2)²⁰¹⁸
on a : f est dérivable sur R en particulier en -1 et f(-1) = (-1+2)²⁰¹⁸ = 1

Donc : lim (x+2)²⁰¹⁸ / x+1 = lim (f(x) - f(-1)) / (x - (-1)) = f'(-1)
Et puisque : f'(x) = 2018 × (x+2)²⁰¹⁷ × (x+2) = 2018 × (x+2)²⁰¹⁷
Donc : f'(-1) = 2018 × 1²⁰¹⁷ = 2018

Donc : lim (x+2)²⁰¹⁸ / x+1 = 2018

## Exemple 2 :

lim 2sinx-1 / x-π/6
on pose : f(x) = 2sinx
on a : f est dérivable sur R en particulier en

## Propriété :

C'est en s'entrainant régulièrement aux calculs et exercices Que l'on devient un mathématicien

## Remarque :

« C'est en forçant que l'on devient forgeron »
Dit un proverbe.


---

