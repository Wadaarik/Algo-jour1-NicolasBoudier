import sys
import time

begin = time.time()
iteration = comparaison = 0


def sortFusion(tab):
    global iteration, comparaison

    if len(tab) <= 1:
        comparaison += 1
        return tab

    center = len(tab) // 2
    gauche = sortFusion(tab[:center]) #Get first part
    droite = sortFusion(tab[center:]) #Get last part
    Ordonne = combineTab(gauche, droite)

    return Ordonne


def combineTab(sousTab1,sousTab2):
    global iteration, comparaison
    indice_sousTab1 = indice_sousTab2 = 0
    sousTab1Taille = len(sousTab1)
    sousTab2Taille = len(sousTab2)
    tabCombine = []

    while indice_sousTab1 < sousTab1Taille and indice_sousTab2 < sousTab2Taille:
        iteration += 1
        comparaison += 1
        if sousTab1[indice_sousTab1] < sousTab2[indice_sousTab2]: #Check same tab level
            comparaison += 1
            tabCombine.append(sousTab1[indice_sousTab1])
            indice_sousTab1 += 1
        else:
            comparaison += 1
            tabCombine.append(sousTab2[indice_sousTab2])
            indice_sousTab2 += 1
    while indice_sousTab1 < sousTab1Taille:
        iteration += 1
        comparaison += 1
        tabCombine.append(sousTab1[indice_sousTab1])
        indice_sousTab1 += 1
    while indice_sousTab2 < sousTab2Taille:
        iteration += 1
        comparaison += 1
        tabCombine.append(sousTab2[indice_sousTab2])
        indice_sousTab2 += 1

    return tabCombine


print('Série: ' + sys.argv[1])
print('Résultat: ' + ";".join(sortFusion(sys.argv[1].split(';'))))
print('Nb de comparaison: ' + str(comparaison))
print('Nb d\'itération: ' + str(iteration))
print('Temps (sec) : ' + str(round((time.time() - begin), 4)))