import sys
import time

begin = time.time()
iteration = comparaison = 0


def sortSelect(tab):
    global iteration, comparaison
    sortTaille = len(tab)

    for i in range(sortTaille):
        iteration = iteration + 1
        minimum = i
        for j in range(i+1, sortTaille):
            iteration = iteration + 1
            if tab[minimum] > tab[j]:
                comparaison = comparaison + 1
                minimum = j
        temporaire = tab[i]
        tab[i] = tab[minimum]
        tab[minimum] = temporaire

    return tab


print('Série: ' + sys.argv[1])
print('Résultat: ' + ";".join(sortSelect(sys.argv[1].split(';'))))
print('Nb de comparaison: ' + str(comparaison))
print('Nb d\'itération: ' + str(iteration))
print('Temps (sec) : ' + str(round((time.time() - begin), 4)))

