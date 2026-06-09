<!-- Page 1 -->

# Physique et Chimie : 2ème Année Bac

## Séance 17 (Les lois de Newton)

### Professeur : Mr El GOUFIFA Jihad

### Sommaire

#### I- Complément mathématique

- 1-1/ Notions générales sur le mouvement
- 1-2/ Vecteur vitesse
- 1-3/ Vecteur accélération
- 1-4/ Repère de Frenet

#### II- Le Mouvement

- 2-1/ Mouvement rectiligne uniforme
- 2-2/ Mouvement rectiligne uniformément varié

#### III- Les forces intérieures et les forces extérieures

#### IV- Les lois de Newton

- 4-1/ La 1ère loi de Newton (Principe d’inertie)
- 4-2/ La 2ème loi de Newton (Théorème de centre d’inertie)
- 4-3/ La 3ème loi de Newton (Principe des actions réciproques)

#### V- Applications

- 5-1/ Mouvement sur un plan horizontal sans frottement
- 5-2/ Mouvement sur un plan horizontal avec frottement
- 5-3/ Mouvement sur un plan incliné sans frottement
- 5-4/ Mouvement sur un plan incliné avec frottement
- 5-5/ Mouvement curviligne

#### VI- Exercices

- 6-1/ Exercice 1
- 6-2/ Exercice 2
- 6-3/ Exercice 3
- 6-4/ Exercice 4


---


<!-- Page 2 -->

# I- Complément mathématique

## 1-1/ Notions générales sur le mouvement

Nous savons que le mouvement d'un corps est relatif au référentiel choisi, c'est-à-dire que les corps ne se déplacent que par rapport à d'autres corps.

Donc pour étudier le mouvement d'un corps on doit choisir un solide de référence fixe appelé référentiel puis un repère d'espace et un repère de temps liés à ce référentiel.

La plupart des temps, on choisi comme référentiel d'étude le référentiel terrestre.

Pour repérer la position du mobile, on utilise un repère d'espace $\left(\vec{O}, \vec{i}, \vec{j}, \vec{k}\right)$.

Le vecteur position permet de repérer le point $M$ dans l'espace par rapport à un référentiel choisi pour l'étude.

[Diagram: A 3D coordinate system with origin O, axes x, y, z, and point M. The vector OM is shown as a line from O to M, with components in the x, y, and z directions.]

$$
\vec{OM} = x. \vec{i} + y. \vec{j} + z. \vec{k}
$$

$$
\vec{OM} = \begin{pmatrix} x \\ y \\ z \end{pmatrix}
$$

Les fonctions $x(t)$, $y(t)$ et $z(t)$ sont les équations horaires du mouvement.

## 1-2/ Vecteur vitesse

Le vecteur vitesse instantanée du centre d'inertie d'un corps est égal à la dérivée du vecteur position par rapport au temps :

$$
\vec{v}_G = \frac{d\vec{OG}}{dt}
$$

Le module du vecteur vitesse est $v_G = \left\|\vec{v}_G\right\| = \sqrt{\dot{x}^2 + \dot{y}^2 + \dot{z}^2}$ en $(m/s)$.


---


<!-- Page 3 -->

# 1-3/ Vecteur accélération

Le vecteur accélération du centre d'inertie d'un corps est égal à la dérivée du vecteur vitesse par rapport au temps :

$$
\vec{a}_G = \frac{d\vec{v}_G}{dt}
$$

Le module du vecteur accélération est

$$
a_G = \left\|\vec{a}_G\right\| = \sqrt{\dot{x}^2 + \dot{y}^2 + \dot{z}^2} \text{ en } (m/s^2).
$$

# 1-4/ Repère de Frenet

Le repère de Frenet est un repère local orthonormé lié au mobile que l'on note

$$
(M, \vec{u}, \vec{n}).
$$

Le vecteur unitaire

$$
\vec{u}
$$

est tangent à la trajectoire au point

$$
M
$$

et orienté dans le sens du mouvement.

Le vecteur unitaire

$$
\vec{n}
$$

est normal, et dirigé vers le centre de courbure de la trajectoire, il est perpendiculaire à

$$
\vec{u}
$$

L'expression du vecteur accélération dans le repère de Frenet est :

- $a_t = \frac{dv}{dt}$ est la composante tangentielle du vecteur accélération.
- $a_n = \frac{v^2}{\rho}$ est la composante normale du vecteur accélération.

$\rho$ est le rayon de courbure de la trajectoire au point

$$
M
$$

Si la trajectoire est un cercle $\rho = R$ (Rayon du cercle).

# II- Le Mouvement

## 2-1/ Mouvement rectiligne uniforme

Le mouvement rectiligne uniforme est caractérisé par :


---


<!-- Page 4 -->

- Une trajectoire rectiligne.
- Une vitesse constante : $\vec{v} = \frac{d\vec{x}}{dt} \, \vec{i} = c\vec{t}e$.
- Une accélération nulle : $\vec{a} = \frac{d^2\vec{x}}{dt^2} \, \vec{i} = \vec{0}$.

L'équation horaire du mouvement est : $x = v \cdot t + x_0$ (abscisse à l'origine).

---

## 2-2/ Mouvement rectiligne uniformément varié

Le mouvement rectiligne uniformément varié est caractérisé par :

- Une trajectoire rectiligne.
- Une accélération constante $\vec{a} = \frac{d^2\vec{x}}{dt^2} \, \vec{i} = c\vec{t}e$

L'équation de la vitesse est $v = a \cdot t + v_0$.

L'équation horaire du mouvement est $x = \frac{1}{2} a \cdot t^2 + v_0 \cdot t + x_0$.

Dans ce cas la vitesse en fonction du temps est une fonction affine, son coefficient directeur est égal à l'accélération.

[Diagram: three graphs showing x vs t, Vx vs t, and x vs t for a uniformly accelerated motion]

---

## III- Les forces internes et les forces externes

On appelle forces externes, les forces qui s'exercent sur le système par des corps qui n'appartiennent pas au système.

On appelle forces internes, les forces qui s'exercent sur le système par des corps qui appartiennent pas au système.

Un système est dit isolé s'il n'est soumis à aucune force externe.

Un système est dit pseudo-isolé si les forces extérieures auquel il est soumis se compensent.

---

## IV- Les lois de Newton

### 4-1/ La 1ère loi de Newton (Principe d'inertie)

Dans un référentiel galiléen, tout corps isolé (aucune force n'est appliquée) ou pseudo isolé (la somme des forces est nulle) est soumis d'un mouvement rectiligne uniforme $\left(\vec{v} = c\vec{t}e\right)$ ou il est immobile $\left(\vec{v} = \vec{0}\right)$.

[Diagram: a diagram showing a system with forces acting on it, labeled as "forces externes" and "forces internes"]


---


<!-- Page 5 -->

# Remarque

Le repère de Copernic est le meilleur repère galiléen (son origine est le soleil et ses trois axes son dirigés vers trois étoiles fixes).

Tout repère en mouvement de translation rectiligne uniforme par rapport au repère de Copernic est considéré galiléen, donc tous les repères terrestres peuvent être considérés galiléen pendant des intevalles de temps courts.

## 4-2/ La 2ème loi de Newton (Théorème de centre d’inertie)

Dans un repère galiléen la somme des vecteurs forces qui s'exercent sur un corps est égale au produit de la masse du corps et du vecteur accélération de son centre d'inertie.

$$
\sum \vec{F}_{ext} = m \vec{a}_G
$$

## 4-3/ La 3ème loi de Newton (Principe des actions réciproques)

Lorsqu'il y a une interaction entre deux corps A et B, le corps A exerce une force sur le corps B, on la note $\vec{F}_{A/B}$, et le corps B exerce une force de même intensité $\vec{F}_{B/A}$.

Ces deux vecteurs sont liés vectoriellement par la relation suivante :

$$
\vec{F}_{A/B} = -\vec{F}_{B/A}
$$

Leur intensité est :

$$
F_{A/B} = -F_{B/A} = G \frac{m_A m_B}{d^2}
$$

$G$ est la constante de gravitation universelle, elle vaut $6,67 \times 10^{-11} N \cdot m^2 \cdot kg^{-2}$, et $d$ la distance qui les sépare.

## V- Applications

### 5-1/ Mouvement sur un plan horizontal sans frottement

On considère un corps solide (S) en mouvement sur un plan horizontal sans frottement sous l'action d'une force constante $\vec{F}$ comme l'indique la figure suivante :

[Diagram: A diagram showing a solid object (S) on a horizontal plane, with forces $\vec{F}$, $\vec{P}$, and $\vec{R}$ acting on it. The object has a center of mass G. The forces are: $\vec{F}$ (horizontal), $\vec{P}$ (vertical, possibly gravity), and $\vec{R}$ (normal force). The equation $\vec{F} + \vec{P} + \vec{R} = m \vec{a}$ is written below the diagram.]

$$
\vec{F} + \vec{P} + \vec{R} = m \vec{a}
$$

$$
a = \frac{F}{m}
$$


---


<!-- Page 6 -->

# 5-2/ Mouvement sur un plan horizontal avec frottement

On considère un corps solide $(S)$ en mouvement sur un plan horizontal avec frottement sous l’action d’une force constante $\vec{F}$ comme l’indique la figure suivante :

[Diagram: A diagram showing a solid object (S) on a horizontal plane, with forces $\vec{F}$, $\vec{P}$, and $\vec{R}$ acting on it. The forces are labeled with arrows and directions. The object is labeled with its center of mass G. The forces are shown as vectors: $\vec{F}$ is horizontal, $\vec{P}$ is vertical, and $\vec{R}$ is a vector from the center of mass to the point of contact with the plane. The diagram includes a coordinate system with x and y axes.]

$$
\vec{F} + \vec{P} + \vec{R} = m.\vec{a}
$$

$$
R = \sqrt{f^2 + R_N^2}
$$

$$
k = \tan \varphi = \frac{f}{R_N} \Leftrightarrow \varphi = \arctan k
$$

# 5-3/ Mouvement sur un plan incliné sans frottement

On libère un corps solide $(S)$ de masse $m$ sur un plan incliné d’un angle $\alpha$ par rapport à l’horizontale et il glisse sans frottement vers le bas :

[Diagram: A diagram showing a solid object (S) on an inclined plane, with forces $\vec{P}$, $\vec{R}$, and $\vec{a}$ acting on it. The forces are labeled with arrows and directions. The object is labeled with its center of mass G. The plane is inclined at an angle $\alpha$ to the horizontal. The forces are shown as vectors: $\vec{P}$ is perpendicular to the plane, $\vec{R}$ is a vector from the center of mass to the point of contact with the plane, and $\vec{a}$ is the acceleration vector. The diagram includes a coordinate system with x and y axes.]

$$
\vec{P} + \vec{R} = m.\vec{a}
$$

$$
a = g \sin \alpha
$$

# 5-4/ Mouvement sur un plan incliné avec frottement

On tire un corps solide $(S)$ de masse $m$ sur un plan incliné d’un angle $\alpha$ par rapport à l’horizontale en utilisant une corde, il glisse avec frottement vers le haut :

[Diagram: A diagram showing a solid object (S) on an inclined plane, with forces $\vec{P}$, $\vec{R}$, and $\vec{a}$ acting on it. The forces are labeled with arrows and directions. The object is labeled with its center of mass G. The plane is inclined at an angle $\alpha$ to the horizontal. The forces are shown as vectors: $\vec{P}$ is perpendicular to the plane, $\vec{R}$ is a vector from the center of mass to the point of contact with the plane, and $\vec{a}$ is the acceleration vector. The diagram includes a coordinate system with x and y axes.]


---


<!-- Page 7 -->

# 5-5/ Mouvement curviligne

Une bille (S) de masse m se déplace sur un rail ABCD, contenant trois portions, comme l’indique la figure suivante :

## 1. La portion AB est inclinée d’une angle α où le mouvement se fait sans frottement :

[Diagram: A sphere (S) of mass m is on a rail ABCD, with portion AB inclined at an angle α. The diagram shows the forces acting on the sphere: weight (mg), normal force (N), and the frictionless motion. The forces are represented as vectors: mg (downward), N (perpendicular to the surface), and the acceleration vector (a). The diagram also shows the coordinate system with x and y axes.]

$$
\vec{P} + \vec{R} + \vec{T} = m. \vec{a}
$$

$$
R = \sqrt{f^2 + R_N^2}
$$

$$
v_B = \sqrt{2gAB \sin \alpha}
$$

## 2. La portion BC horizontale où le mouvement se fait avec frottement :

[Diagram: A sphere (S) of mass m is on a rail ABCD, with portion BC horizontal. The diagram shows the forces acting on the sphere: weight (mg), normal force (N), and friction (f). The forces are represented as vectors: mg (downward), N (perpendicular to the surface), and friction (f) acting opposite to the direction of motion. The diagram also shows the coordinate system with x and y axes.]

$$
\vec{P} + \vec{R} + \vec{T} = m. \vec{a}
$$

$$
R = \sqrt{f^2 + R_N^2}
$$

$$
v_B = \sqrt{2gAB \sin \alpha}
$$

**Remarque :** Le mouvement de la bille sur le rail ABCD est décrit par des lois de Newton appliquées à la bille en mouvement curviligne. La première portion AB est inclinée d'un angle α et le mouvement se fait sans frottement, ce qui implique que la seule force de frottement est nulle. La deuxième portion BC est horizontale et le mouvement se fait avec frottement, ce qui implique que la force de frottement agit dans la direction opposée au mouvement.


---


<!-- Page 8 -->

# VI- Exercices

## 6-1/ Exercice 1

Les coordonnées du vecteur position $\vec{OG}$ au cours du mouvement d’un corps solide dans un repère orthonormé $R$ ($O, i, j$) sont :
$$
\begin{cases}
x = t + 3 \\
y = t^2 - t + 3
\end{cases}
$$

1. Trouver l’équation de la trajectoire $y = f(x)$. En déduire sa nature.
2. Déterminer les coordonnées du vecteur vitesse $\vec{V}_G$ dans le repère $R$.
3. Calculer la norme de la vitesse $\vec{V}_G$ à la date $t = 1,5s$.
4. Trouver les coordonnées du vecteur accélération $\vec{a}_G$ dans le repère $R$.
5. Calculer la norme du vecteur accélération $\vec{a}_G$.
6. Déterminer la nature du mouvement du mobile (accéléré ou retardé).

## 6-2/ Exercice 2

Un skieur (avec ses équipements) assimilé à un corps solide de masse $m = 70Kg$, décrit une piste formée par deux parties :
- $OB$, une pente inclinée de $20^\circ$ avec le plan horizontal

[Diagram: A diagram showing a circular arc with a point O at the origin, a point B on the horizontal axis, and a point C on the arc. The diagram includes a vector $\vec{R}$ from O to C, a vector $\vec{P}$ from O to B, and a vector $\vec{M}$ from O to the center of the arc. The diagram also shows a horizontal line labeled $x$ and a vertical line labeled $y$. The diagram includes a right triangle with a horizontal leg of length $r$, a vertical leg of length $h$, and an angle $\theta$ at the origin. The diagram shows a vector $\vec{v}$ from O to the point on the arc, and a vector $\vec{a}$ from O to the center of the arc. The diagram shows a vector $\vec{R}$ from O to the center of the arc, and a vector $\vec{P}$ from O to the point on the arc. The diagram shows a vector $\vec{M}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{a}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{R}$ from O to the center of the arc, and a vector $\vec{P}$ from O to the point on the arc. The diagram shows a vector $\vec{M}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{a}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{R}$ from O to the center of the arc, and a vector $\vec{P}$ from O to the point on the arc. The diagram shows a vector $\vec{M}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{a}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{R}$ from O to the center of the arc, and a vector $\vec{P}$ from O to the point on the arc. The diagram shows a vector $\vec{M}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{a}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{R}$ from O to the center of the arc, and a vector $\vec{P}$ from O to the point on the arc. The diagram shows a vector $\vec{M}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{a}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{R}$ from O to the center of the arc, and a vector $\vec{P}$ from O to the point on the arc. The diagram shows a vector $\vec{M}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{a}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{R}$ from O to the center of the arc, and a vector $\vec{P}$ from O to the point on the arc. The diagram shows a vector $\vec{M}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{a}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{R}$ from O to the center of the arc, and a vector $\vec{P}$ from O to the point on the arc. The diagram shows a vector $\vec{M}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{a}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{R}$ from O to the center of the arc, and a vector $\vec{P}$ from O to the point on the arc. The diagram shows a vector $\vec{M}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{a}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{R}$ from O to the center of the arc, and a vector $\vec{P}$ from O to the point on the arc. The diagram shows a vector $\vec{M}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{a}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{R}$ from O to the center of the arc, and a vector $\vec{P}$ from O to the point on the arc. The diagram shows a vector $\vec{M}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{a}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{R}$ from O to the center of the arc, and a vector $\vec{P}$ from O to the point on the arc. The diagram shows a vector $\vec{M}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{a}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{R}$ from O to the center of the arc, and a vector $\vec{P}$ from O to the point on the arc. The diagram shows a vector $\vec{M}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{a}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{R}$ from O to the center of the arc, and a vector $\vec{P}$ from O to the point on the arc. The diagram shows a vector $\vec{M}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{a}$ from O to the center of the arc, and a vector $\vec{v}$ from O to the point on the arc. The diagram shows a vector $\vec{R}$ from O to the center of the arc, and a vector $\vec{P}$ from O to the point on the arc. The diagram shows a vector $\vec{M


---


<!-- Page 9 -->

- BC, une voie rectiligne et horizontale.
- Le contact entre le skieur avec ses équipements se fait sans frottements sur la partie $OB = 2,4\,\text{m}$ :

L’intensité de gravitation $g = 9,81\,\text{m}\,\text{s}^{-2}$.

On étudie le mouvement du corps $(S)$ dans un repère galiléen $R\left(O,\,\vec{i},\,\vec{j}\right)$.

## La partie $OB$

1. En appliquant la 2ème loi de Newton, déterminer l’abscisse $a_{G_x}$ du vecteur accélération du centre d’inertie de $(S)$. Quelle est la nature de son mouvement ?

2. Déterminer les équations horaires $v(t)$ et $x(t)$ du mouvement, on prend comme origine des dates lorsque le skieur est au point $O$ et sa vitesse initiale est nulle.

3. Déterminer l’instant $t_B$ ou le corps $(S)$ atteint le point $B$.

4. Calculer la vitesse au point $B$.

5. Calculer l’intensité de la réaction du plan sur le skieur.

## La partie $BC$

Le solide $(S)$ arrive au point $B$ avec la vitesse $V_B$.

On prend comme origine des dates et d’espace lorsque le skieur atteint le point $B$.

Le contact entre le plan $BC$ et $(S)$ se fait avec frottements équivalents à une force $\vec{f}$ constante et horizontale $f = 80\,\text{N}$ de sens opposé à celui du mouvement.

6. En appliquant la 2ème loi de Newton, déterminer l’abscisse $a_{G_x}$ du vecteur accélération.

7. Déterminer les équations horaires $v(t)$ et $x(t)$ du mouvement.

8. Déterminer l’instant $t_C$ sachant que $(S)$ arrête au point $C$.

9. Calculer la distance $BC$.

10. Calculer l’intensité de la réaction du plan sur le skieur.

11. En déduire le coefficient de frottement $K$ et l’angle de frottement $\varphi$.

6-3/ Exercice 3


---


<!-- Page 10 -->

Une piste $BCD$ dans un plan vertical est constituée d’une partie $BC$ horizontale de longueur $BC = 80cm$ et d’une partie $CD$ circulaire de rayon $r = 10cm$.

On lance, à $t = 0$, un corps $(S)$ de masse $m = 200g$ à partir du point $B$ origine de repère $(B, x)$ considéré galiléen avec une vitesse initiale $v_B = 2m.s^{-1}$ et le corps $(S)$ se déplace sur la partie $BC$ avec frottement :

On prend $g = 9,81m.s^{-2}$.

1. Trouver l’expression de la force de frottement $f$, calculer sa valeur sachant que l’accélération $a_{Gx}$ du centre d’inertie est $a_{Gx} = -2m.s^{-2}$.

2. Calculer la valeur de la réaction de la partie $BC$ sur le corps $(S)$. Déduire la valeur de l’angle de frottement.

3. En utilisant les équations horaires $v(t)$ et $x(t)$ déterminer la vitesse $v_C$ au point $C$.

Arrivant au point $C$, le corps $(S)$ continue son mouvement sur la partie circulaire $CD$ sans frottement.

4. Trouver l’expression de la force de réaction $R$ appliquée par la partie $CD$ sur le corps $(S)$ à la position $M$ repérée par l’angle $\theta$ en fonction de $m, g, r, \theta$ et $v_M$ la vitesse au point $M$.

5. Appliquer le théorème de l’énergie cinétique entre $C$ et $M$ et montrer que l’expression de $v_M$ s’écrit : $v_M = \sqrt{v_C^2 - 2g.r(1 - \cos\theta)}$.

6. Déterminer la valeur de l’angle maximal $\theta_{max}$ pour lequel le solide $(S)$ revient dans le sens inverse.

7. Calculer l’intensité de la force de réaction $R$ à cet angle.

**Rappel**

Dans le repère de Frenet, le vecteur accélération s’écrit :

$\vec{a}_G = \vec{a}_T + \vec{a}_n = \vec{a}_T \cdot \vec{u} + \vec{a}_n \cdot \vec{n}$ avec $\vec{a}_T = \frac{dv}{dt}$ et $\vec{a}_n = \frac{v^2}{r}$.

**6-4/ Exercice 4**

Cet exercice se propose d’étudier le mouvement du centre d’inertie $G$ d’un système $(S)$ formé d’un motard et d’une moto se déplaçant sur une piste de compétition.

Cette piste est formée d’une partie rectiligne $A'B'$ inclinée d’un angle $p$ par rapport à l’horizontale

[Diagram: A diagram showing a horizontal part BC of length 80 cm and a circular part CD of radius 10 cm, with a block S on BC and a point M on CD. The diagram includes a coordinate system with x-axis and y-axis, and a vector v_B pointing to the right.]

**Exercice 4 :**

1. Trouver l’expression de la force de frottement $f$, calculer sa valeur sachant que l’accélération $a_{Gx}$ du centre d’inertie est $a_{Gx} = -2m.s^{-2}$.

2. Calculer la valeur de la réaction de la partie $BC$ sur le corps $(S)$. Déduire la valeur de l’angle de frottement.

3. En utilisant les équations horaires $v(t)$ et $x(t)$ déterminer la vitesse $v_C$ au point $C$.

4. Trouver l’expression de la force de réaction $R$ appliquée par la partie $CD$ sur le corps $(S)$ à la position $M$ repérée par l’angle $\theta$ en fonction de $m, g, r, \theta$ et $v_M$ la vitesse au point $M$.

5. Appliquer le théorème de l’énergie cinétique entre $C$ et $M$ et montrer que l’expression de $v_M$ s’écrit : $v_M = \sqrt{v_C^2 - 2g.r(1 - \cos\theta)}$.

6. Déterminer la valeur de l’angle maximal $\theta_{max}$ pour lequel le solide $(S)$ revient dans le sens inverse.

7. Calculer l’intensité de la force de réaction $R$ à cet angle.

**Rappel**

Dans le repère de Frenet, le vecteur accélération s’écrit :

$\vec{a}_G = \vec{a}_T + \vec{a}_n = \vec{a}_T \cdot \vec{u} + \vec{a}_n \cdot \vec{n}$ avec $\vec{a}_T = \frac{dv}{dt}$ et $\vec{a}_n = \frac{v^2}{r}$.

**6-4/ Exercice 4**

Cet exercice se propose d’étudier le mouvement du centre d’inertie $G$ d’un système $(S)$ formé d’un motard et d’une moto se déplaçant sur une piste de compétition.

Cette piste est formée d’une partie rectiligne $A'B'$ inclinée d’un angle $p$ par rapport à l’horizontale


---


<!-- Page 11 -->

Dans tout l’exercice, les frottements sont négligés et l’étude du mouvement du centre d’inertie $G$ est réalisée dans le référentiel terrestre considéré comme galiléen.

Données :
- L’angle $\beta = 10^\circ$
- Intensité de la pesanteur : $g = 10 \, m.s^{-2}$
- Masse du système $(S)$ : $m = 190 \, kg$.

À un instant choisi connue origine des dates $(t = 0)$, le système $(S)$ s’élance sans vitesse initiale, d’une position où le centre d’inertie $G$ est confondu avec le point $A$.

Le système est soumis, au cours de son mouvement sur la partie $A'B'$, à la réaction du plan incliné, à son poids et à une force motrice $\vec{F}$ constante, dont la ligne d’action est parallèle à la trajectoire de $G$ et le sens est celui du mouvement.

Pour étudier le mouvement de $G$ au cours de cette phase, on choisit un repère d’espace $\left( A, \vec{i} \right)$ parallèle à $A'B'$ et on repère la position de $G$ par son abscisse $x$ :

[Diagram: A diagram showing a motorcycle on an inclined plane. The plane is labeled with points A, B, and B'. The incline is at an angle $\beta$ to the horizontal. The center of mass G is shown on the motorcycle. The diagram includes a vector $\vec{F}$ pointing along the incline, and a vector $\vec{g}$ pointing vertically downward. The coordinate system is defined with $A$ as the origin and $\vec{i}$ as the direction of the incline.]

1. En appliquant la deuxième loi de Newton, montrer que l’expression de l’accélération $a_G$ du mouvement de $G$ est $a_G = \frac{F}{m} + g.\sin\beta$

La courbe suivante représente les variations de la vitesse instantanée $V_G$ du centre d’inertie $G$ en fonction du temps :

2. En exploitant cette courbe, trouver la valeur de l’accélération $a_G$.

3. Déduire l’intensité $F$ de la force motrice.

4. Écrire l’expression numérique de l’équation horaire $x = f(t)$ du mouvement de $G$.


---


<!-- Page 12 -->

# Exercices de M3allem

## Exercice 5

5. Sachant que $AB = 36m$, déterminer l'instant $t_B$ de passage de $G$ par le point $B$.

## Exercice 6

6. Calculer la vitesse $V_B$ de passage de $G$ par le point $B$.


---

