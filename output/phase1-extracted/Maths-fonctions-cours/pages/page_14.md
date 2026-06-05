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