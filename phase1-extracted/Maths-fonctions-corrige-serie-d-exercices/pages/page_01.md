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