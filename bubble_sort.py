import sys
import time

begin = time.time()
iteration = comparaison = 0


def sortBulle(tab):
    global iteration, comparaison
    taille = len(tab)

    for i in range(taille):
        iteration += 1
        for j in range(taille):
            iteration += 1
            if tab[j] > tab[i]:
                comparaison += 1
                tab[j], tab[i] = tab[i], tab[j]

    return tab


print('Série: ' + sys.argv[1])
print('Résultat: ' + ";".join(sortBulle(sys.argv[1].split(';'))))
print('Nb de comparaison: ' + str(comparaison))
print('Nb d\'itération: ' + str(iteration))
print('Temps (sec) : ' + str(round((time.time() - begin), 4)))