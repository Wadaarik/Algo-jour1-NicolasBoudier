# Journee-1-algo-iim

## EQUIPE 
- Chef : Nicolas Boudier
- Aymeric Derchain
- Lilian Gautier

## DISCORD 
- TD4

### Bubble sort
- Compare chaque éléments consécutivement et se permutent entre elles si elles en ont besoin

> Pratique pour les personnes commençant à coder et pour avoir un classement facile

Le temps est de 0.0001 sec

`beaucoup d'itération et de comparaison ce qui peut être compliqué avec plus de chiffres`

### Selection sort
- Fonctionne en repérant le plus petit nombre d'un tableau pour le passer dans un autre

Le temps est de 0.0001 sec 

> Peu de comparaison (2) et peu d'itération (21)

### Insertion sort
- Compare l'élément actuel du tableau à son prédécesseur.
- Les éléments plus grands rencontrés sont envoyés vers le haut du tableau.
- Fonction comme le tri des cartes dans une main de jeu

Le temps est de 0.0001 sec

> Peu de comparaison (9) et d'itération (15)

`Si le tableau contient énormément de nombre ou bien qu'il n'est trié un minimum au préalable`

### Merge sort
- Il divise le tableau en deux moitiés jusqu'à ce que les nombres soient deux dans un tableau
- Il compare ensuite les deux nombres et les classes dans l'ordre demandé

Le temps est de 0.0001 sec

>Peu d'itération (16)

`Le script est bien plus long à faire`
`Beaucoup de comparaison (33)`

### Quick sort
- Comme le Merge sort il divise le tableau en plusieurs morceaux et le recompile ensuite
- Utilise le principe d'un pivot et place les autres éléments en fonction de ce pivot

Le temps est de 0.0001 sec

> Peu de comparaison (11) et d'itération (12)

### Shell sort
- Variante du tri par insertion (Selection Sort)
- Tri chaque éléments séparés de n positions
- Diminue petit à petit n jusqu'à 1

Le temps est de 0.0001 sec

>Pas de comparaison (0) et peu d'itération (19) 

`Le tri n'est pas stable`

### Comb sort
- Amélioration du tri à bulle (Bubble sort)
- Il fonctionne avec un écart de taille de grande valeur et se réduit avec un facteur de 1,3 à chaque itération jusqu'à 1

Le temps est de 0.0011 sec

> Peu de comparaison (9) et peu d'itération (18)
> Peut rivaliser avec les Quck sort