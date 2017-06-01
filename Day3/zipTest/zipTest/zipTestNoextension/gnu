#!/usr/bin/env python3
# coding: utf-8

""" Dictionnaire en compréhension,
    tris des clefs, lambda fonction
    conversion, ensemble, liste
"""

from gnuText import gnu as texte

print(" %d caractères sur un alphabet de %d symboles." % (len(texte), len(set(texte))))

fr = dict((c,texte.count(c)) for c in set(texte))

li_fr = list((x,fr[x]) for x in fr.keys())

# Le résultat suivant est faux car ce critère de tri est l'ordre
# ascii sur les clefs (les symboles composants le texte)
li_fr.sort( reverse=True)
print("dictionnaire des fréquences : \n", li_fr)


# Il faut spécifier le critère de tris
li_fr.sort(key=lambda b :b[1] , reverse=True)

print("fréquences par tri décroissant : \n", li_fr)


