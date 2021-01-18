import sys
import time

begin = time.time()
iteration = comparaison = 0


def shellSort(tab):
    global iteration, comparaison
    size = len(tab)
    gap = size // 2

    while gap > 0:
        comparaison += 1
        iteration += 1
        for i in range(gap, size):
            iteration += 1
            anchor = tab[i]
            j = i
            while j >= gap and tab[j-gap] > anchor:
                comparaison += 1
                iteration += 1
                tab[j] = tab[j-gap]
                j -= gap
            tab[j] = anchor
        gap = gap // 2

    return tab


print('Série: ' + sys.argv[1])
print('Résultat: ' + ";".join(shellSort(sys.argv[1].split(';'))))
print('Nb de comparaison: ' + str(comparaison))
print('Nb d\'itération: ' + str(iteration))
print('Temps (sec) : ' + str(round((time.time() - begin), 4)))