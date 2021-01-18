import sys
import time

begin = time.time()
iteration = comparaison = 0


def sortInsertion(tab):
    global iteration, comparaison
    taille = len(tab)

    for i in range(taille):
        iteration += 1
        valI = tab[i]
        position = i - 1
        while position >= 0 and valI < tab[position]:
            iteration += 1
            comparaison += 1
            tab[position + 1] = tab[position]
            position -= 1
        tab[position + 1] = valI

    return tab


print('Série: ' + sys.argv[1])
print('Résultat: ' + ";".join(sortInsertion(sys.argv[1].split(';'))))
print('Nb de comparaison: ' + str(comparaison))
print('Nb d\'itération: ' + str(iteration))
print('Temps (sec) : ' + str(round((time.time() - begin), 4)))