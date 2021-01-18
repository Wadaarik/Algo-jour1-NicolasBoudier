# Journee-1-algo-iim

## EQUIPE 
- Chef : Nicolas Boudier
- Aymeric Derchain
- Lilian Gautier

## DISCORD 
- Channel TD4

## Explication

### Bubble sort
- Compare chaque éléments consécutivement et se permutent entre eux si besoin il y a

> Pratique pour les personnes commençant à coder et pour avoir un classement facile
> Peu de comparaison(9)

Le temps est de 0.0001 sec

`beaucoup d'itération (42) ce qui peut être compliqué avec plus de chiffres`

***

### Selection sort
- Récupère le plus petit nombre d'un tableau pour le mettre dans un nouveau tableau et le supprimer du précédent

Le temps est de 0.0001 sec 

> Peu de comparaison (2) et peu d'itération (21)

***

### Insertion sort
- Compare chaque élément du tableau à la valeur qui la précède.
- Les éléments plus grands sont envoyés vers le fin du tableau.

Le temps est de 0.0001 sec

> Peu de comparaison (9) et d'itération (15)

`Risque de plantage si il y a trop de nombre`

***

### Merge sort
- Il divise le tableau en deux moitiés jusqu'à ce que deux nombres peuvent être comparé
- Il compare ensuite les deux nombres et les classes dans l'ordre demandé

Le temps est de 0.0001 sec

>Peu d'itération (16)

`Le script est bien plus long à faire`

`Beaucoup de comparaison (33)`

***

### Quick sort
- Comme le `Merge sort` (tri fusion) il divise le tableau en plusieurs morceau et le recompile ensuite
- Utilise le principe d'un pivot et place les autres éléments en fonction de ce pivot

Le temps est de 0.0001 sec

> Peu de comparaison (11) et d'itération (12)

***

### Shell sort
- Variante du `Selection sort` (tri par insertion)
- Tri chaque éléments séparés de n positions
- Diminue petit à petit n jusqu'à 1

Le temps est de 0.0001 sec

>Pas de comparaison (11) et peu d'itération (19) 

`Le tri n'est pas stable`

***

### Comb sort
- Amélioration du `Bubble sort` (tri à bulle)
- Il fonctionne avec un écart de taille de grande valeur et se réduit avec un facteur de 1,3 à chaque itération jusqu'à 1

Le temps est de 0.0011 sec

> Peu de comparaison (9) et peu d'itération (18)
> Peut rivaliser avec le Quick sort