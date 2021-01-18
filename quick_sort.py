import sys
import time

begin = time.time()
iteration = comparaison = 0


def sortQuick(tab):
    global iteration, comparaison
    length = len(tab)

    if length <= 1:
        comparaison += 1
        return tab
    else:
        pivot = tab.pop()  # pop supprime l'element à la position spécifiée
    greater = []
    lower = []
    for i in tab:
        iteration += 1
        if i > pivot:
            comparaison += 1
            greater.append(i)
        else:
            lower.append(i)

    return sortQuick(lower) + [pivot] + sortQuick(greater)


print('Série: ' + sys.argv[1])
print('Résultat: ' + ";".join(sortQuick(sys.argv[1].split(';'))))
print('Nb de comparaison: ' + str(comparaison))
print('Nb d\'itération: ' + str(iteration))
print('Temps (sec) : ' + str(round((time.time() - begin), 4)))
