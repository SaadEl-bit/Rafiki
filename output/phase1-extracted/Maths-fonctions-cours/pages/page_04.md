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