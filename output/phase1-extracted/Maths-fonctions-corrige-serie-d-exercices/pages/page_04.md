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