import sys
import time
import math

begin = time.time()
iteration = comparaison = 0


def insertFast(tab):
    global iteration, comparaison
    intervalle = len(tab)
    echange = True
    while (intervalle > 1) or (echange == True):
        iteration += 1
        intervalle = math.floor(intervalle / 1.3)
        if intervalle < 1:
            comparaison += 1
            intervalle = 1
        i = 0
        echange = False
        while i < (len(tab) - intervalle):
            iteration += 1
            if tab[i] > tab[i + intervalle]:
                comparaison += 1
                tab[i], tab[i + intervalle] = tab[i + intervalle], tab[i]
            i += 1
    return tab


print('Série: ' + sys.argv[1])
print('Résultat: ' + ";".join(insertFast(sys.argv[1].split(';'))))
print('Nb de comparaison: ' + str(comparaison))
print('Nb d\'itération: ' + str(iteration))
print('Temps (sec) : ' + str(round((time.time() - begin), 4)))
