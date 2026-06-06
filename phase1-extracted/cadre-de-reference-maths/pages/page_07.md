# 2.4.5. Exprimer la translation, l'homothétie et la rotation en utilisant l'outil complexe.

# 2.4.6. Reconnaître une translation, une homothétie ou une rotation à partir de leurs expressions complexes.

# 2.4.7. Utiliser les nombres complexes pour résoudre des problèmes de géométrie (alignement, orthogonalité ...).

# 2.4.8. Résoudre l'équation $ \omega z^2 + bz + c = 0 $ dans l'ensemble des nombres complexes où $ a, b, c $ sont des nombres réels.

# 2.4.9. Résoudre des équations dont la résolution se ramène à la résolution d'une équation du second degré à une seule inconnue à coefficients réels.

## Cinquième sous-domaine : Calcul de probabilités

### 2.5.1. Utiliser le modèle de dénombrement convenable selon la situation étudiée.

### 2.5.2. Calculer la probabilité de la réunion de deux événements, de l'événement contraire d'un événement et de l'intersection de deux événements.

### 2.5.3. Calculer la probabilité conditionnelle et l'appliquer pour le calcul de la probabilité de l'intersection de deux événements.

### 2.5.4. Reconnaître l'indépendance de deux événements

### 2.5.5. Déterminer la loi de probabilité d'une variable aléatoire et calculer ses différents paramètres.

### 2.5.6. Reconnaître la loi binomiale et l'appliquer dans des situations variées.

**Définition :**
La probabilité d'un événement $ A $ est définie par $ P(A) = \frac{\text{nombre d'éléments favorables à } A}{\text{nombre total d'éléments}} $.

**Théorème :**
La probabilité de l'événement contraire $ \overline{A} $ est donnée par $ P(\overline{A}) = 1 - P(A) $.

**Démonstration :**
La probabilité de l'événement $ A $ est égale à la probabilité de l'événement $ A $, donc $ P(A) = \frac{\text{nombre d'éléments favorables à } A}{\text{nombre total d'éléments}} $.
La probabilité de l'événement contraire $ \overline{A} $ est égale à la probabilité de l'événement $ A $, donc $ P(\overline{A}) = 1 - P(A) $.

**Exemple 1 :**
On lance un dé équilibré. On veut calculer la probabilité d'obtenir un nombre pair.
Il y a 3 nombres pairs (2, 4, 6) sur 6 faces.
Donc, $ P(\text{pair}) = \frac{3}{6} = \frac{1}{2} $.

**Exemple 2 :**
On lance deux dés. On veut calculer la probabilité d'obtenir un total de 7.
Il y a 6 combinaisons possibles qui donnent un total de 7 : (1,6), (2,5), (3,4), (4,3), (5,2), (6,1).
Donc, $ P(\text{total de 7}) = \frac{6}{36} = \frac{1}{6} $.

**Exercice 1 :**
On lance un dé équilibré. On veut calculer la probabilité d'obtenir un nombre pair.
Il y a 3 nombres pairs (2, 4, 6) sur 6 faces.
Donc, $ P(\text{pair}) = \frac{3}{6} = \frac{1}{2} $.

**Propriété :**
La probabilité de l'intersection de deux événements $ A $ et $ B $ est donnée par $ P(A \cap B) = P(A) \cdot P(B) $ si $ A $ et $ B $ sont indépendants.

**Remarque :**
La probabilité conditionnelle $ P(B|A) $ est définie par $ P(B|A) = \frac{P(A \cap B)}{P(A)} $.

**Exemple 3 :**
On lance un dé équilibré. On veut calculer la probabilité d'obtenir un nombre pair sachant que le nombre est supérieur ou égal à 4.
Il y a 2 nombres pairs supérieurs ou égaux à 4 : (4, 6).
Donc, $ P(\text{pair}|\text{supérieur ou égal à 4}) = \frac{2}{6} = \frac{1}{3} $.

**Exercice 2 :**
On lance un dé équilibré. On veut calculer la probabilité d'obtenir un nombre pair sachant que le nombre est supérieur ou égal à 4.
Il y a 2 nombres pairs supérieurs ou égaux à 4 : (4, 6).
Donc, $ P(\text{pair}|\text{supérieur ou égal à 4}) = \frac{2}{6} = \frac{1}{3} $.

**Théorème :**
La loi binomiale est une loi de probabilité qui décrit la distribution des résultats d'une expérience aléatoire répétée de manière indépendante et identique.
La probabilité d'obtenir $ k $ succès dans $ n $ essais est donnée par la formule :
$ P(X = k) = \binom{n}{k} p^k (1-p)^{n-k} $.

**Exemple 4 :**
On lance un dé équilibré 10 fois. On veut calculer la probabilité d'obtenir exactement 3 fois un nombre pair.
Il y a 5 nombres pairs (2, 4, 6) sur 10 faces.
Donc, $ P(X = 3) = \binom{10}{3} (0.5)^3 (0.5)^7 = \binom{10}{3} (0.5)^{10} $.

**Exercice 3 :**
On lance un dé équilibré 10 fois. On veut calculer la probabilité d'obtenir exactement 3 fois un nombre pair.
Il y a 5 nombres pairs (2, 4, 6) sur 10 faces.
Donc, $ P(X = 3) = \binom{10}{3} (0.5)^3 (0.5)^7 = \binom{10}{3} (0.5)^{10} $.

**Propriété :**
La loi binomiale est utilisée pour modéliser des situations où les résultats sont indépendants et où chaque essai a deux résultats possibles : succès ou échec.

**Remarque :**
La loi binomiale est utilisée dans des situations variées, comme la probabilité d'obtenir un certain nombre de succès dans une série d'essais.

**Exemple 5 :**
On lance un dé équilibré 10 fois. On veut calculer la probabilité d'obtenir exactement 3 fois un nombre pair.
Il y a 5 nombres pairs (2, 4, 6) sur 10 faces.
Donc, $ P(X = 3) = \binom{10}{3} (0.5)^3 (0.5)^7 = \binom{10}{3} (0.5)^{10} $.

**Exercice 4 :**
On lance un dé équilibré 10 fois. On veut calculer la probabilité d'obtenir exactement 3 fois un nombre pair.
Il y a 5 nombres pairs (2, 4, 6) sur 10 faces.
Donc, $ P(X = 3) = \binom{10}{3} (0.5)^3 (0.5)^7 = \binom{10}{3} (0.5)^{10} $.

**Théorème :**
La loi binomiale est utilisée pour modéliser des situations où les résultats sont indépendants et où chaque essai a deux résultats possibles : succès ou échec.

**Exemple 6 :**
On lance un dé équilibré 10 fois. On veut calculer la probabilité d'obtenir exactement 3 fois un nombre pair.
Il y a 5 nombres pairs (2, 4, 6) sur 10 faces.
Donc, $ P(X = 3) = \binom{10}{3} (0.5)^3 (0.5