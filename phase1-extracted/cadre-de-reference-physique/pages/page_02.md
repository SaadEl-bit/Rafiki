# Éléments de la théorie des probabilités

## Introduction

### Définition : Événement

Un événement est un ensemble de résultats possibles d'une expérience aléatoire. Il est représenté par un sous-ensemble de l'ensemble des résultats possibles.

### Définition : Probabilité

La probabilité d'un événement $A$ est une mesure de la chance qu'il se produise. Elle est définie comme suit :

$$
P(A) = \frac{\text{Nombre de résultats favorables à } A}{\text{Nombre total de résultats possibles}}
$$

### Théorème : Probabilité totale

Soient $A_1, A_2, \dots, A_n$ des événements mutuellement exclusifs. Alors, la probabilité de l'un des événements $A_i$ est donnée par :

$$
P(A_1 \cup A_2 \cup \dots \cup A_n) = P(A_1) + P(A_2) + \dots + P(A_n)
$$

### Théorème : Probabilité conditionnelle

Soient $A$ et $B$ deux événements tels que $P(B) > 0$. La probabilité de $A$ sachant que $B$ est réalisé est définie par :

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$

### Théorème : Formule de Bayes

Soient $A$ et $B$ deux événements tels que $P(B) > 0$. Alors, la probabilité de $A$ sachant que $B$ est réalisé est donnée par :

$$
P(A|B) = \frac{P(B|A)P(A)}{P(B)}
$$

### Exemple 1 : Probabilité conditionnelle

On considère un jeu de 52 cartes. On choisit une carte au hasard. On note $A$ l'événement "la carte est un cœur" et $B$ l'événement "la carte est un roi". On cherche à calculer la probabilité que la carte soit un cœur sachant qu'elle est un roi.

$$
P(A|B) = \frac{P(A \cap B)}{P(B)} = \frac{1/52}{4/52} = \frac{1}{4}
$$

### Exercice 1 : Probabilité conditionnelle

On dispose d'une urne contenant 10 billes : 4 rouges, 3 bleues et 3 vertes. On tire une bille au hasard. On note $A$ l'événement "la bille est rouge" et $B$ l'événement "la bille est bleue". Calculer la probabilité que la bille soit rouge sachant qu'elle est bleue.

### Propriété : Probabilité de l'union de deux événements

Soient $A$ et $B$ deux événements. Alors, la probabilité de l'union de $A$ et $B$ est donnée par :

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

### Remarque : Probabilité de l'intersection

La probabilité de l'intersection de deux événements $A$ et $B$ est donnée par :

$$
P(A \cap B) = P(A)P(B|A)
$$

### Exemple 2 : Probabilité de l'intersection

On considère un jeu de 52 cartes. On choisit une carte au hasard. On note $A$ l'événement "la carte est un cœur" et $B$ l'événement "la carte est un roi". Calculer la probabilité que la carte soit un cœur et un roi.

$$
P(A \cap B) = P(A)P(B|A) = \frac{1}{52} \times \frac{1}{52} = \frac{1}{2704}
$$

### Exercice 2 : Probabilité de l'intersection

On dispose d'une urne contenant 10 billes : 4 rouges, 3 bleues et 3 vertes. On tire une bille au hasard. On note $A$ l'événement "la bille est rouge" et $B$ l'événement "la bille est bleue". Calculer la probabilité que la bille soit rouge et bleue.

### Théorème : Probabilité de l'union de deux événements

Soient $A$ et $B$ deux événements. Alors, la probabilité de l'union de $A$ et $B$ est donnée par :

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

### Théorème : Probabilité de l'intersection

La probabilité de l'intersection de deux événements $A$ et $B$ est donnée par :

$$
P(A \cap B) = P(A)P(B|A)
$$

### Exemple 3 : Probabilité de l'intersection

On considère un jeu de 52 cartes. On choisit une carte au hasard. On note $A$ l'événement "la carte est un cœur" et $B$ l'événement "la carte est un roi". Calculer la probabilité que la carte soit un cœur et un roi.

$$
P(A \cap B) = P(A)P(B|A) = \frac{1}{52} \times \frac{1}{52} = \frac{1}{2704}
$$

### Exercice 3 : Probabilité de l'intersection

On dispose d'une urne contenant 10 billes : 4 rouges, 3 bleues et 3 vertes. On tire une bille au hasard. On note $A$ l'événement "la bille est rouge" et $B$ l'événement "la bille est bleue". Calculer la probabilité que la bille soit rouge et bleue.

### Propriété : Probabilité de l'union de deux événements

Soient $A$ et $B$ deux événements. Alors, la probabilité de l'union de $A$ et $B$ est donnée par :

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

### Remarque : Probabilité de l'intersection

La probabilité de l'intersection de deux événements $A$ et $B$ est donnée par :

$$
P(A \cap B) = P(A)P(B|A)
$$

### Exemple 4 : Probabilité de l'union

On considère un jeu de 52 cartes. On choisit une carte au hasard. On note $A$ l'événement "la carte est un cœur" et $B$ l'événement "la carte est un roi". Calculer la probabilité que la carte soit un cœur ou un roi.

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B) = \frac{1}{52} + \frac{1}{52} - \frac{1}{2704} = \frac{2}{52} - \frac{1}{2704} = \frac{104}{2704} - \frac{1}{2704} = \frac{103}{2704}
$$

### Exercice 4 : Probabilité de l'union

On dispose d'une urne contenant 10 billes : 4 rouges, 3 bleues et 3 vertes. On tire une bille au hasard. On note $A$ l'événement "la bille est rouge" et $B$ l'événement "la bille est bleue". Calculer la probabilité que la bille soit rouge ou bleue.

### Théorème : Probabilité de l'union de deux événements

Soient $A$ et $B$ deux événements. Alors, la probabilité de l'union de $A$ et $B$ est donnée par :

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

### Théorème : Probabilité de l'intersection

La probabilité de l'intersection de deux événements $A$ et $B$ est donnée par :

$$
P(A \cap B) = P(A)P(B|A)
$$

### Exemple 5 : Probabilité de l'union

On considère un jeu de 52 cartes. On choisit une carte au hasard. On note $A$ l'événement "la carte est un cœur" et $B$ l'événement "la carte est un roi". Calculer la probabilité que la carte soit un cœur ou un roi.

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B) = \frac{1}{52} + \frac{1}{