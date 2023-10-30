"""
    Ce script permet de comparer plusieurs fichiers csv. Il ressort les lignes communes entre les deux fichiers.
    Script identique à une recherchev sur Excel.
    Usage: python3 recherchev.py fichier1.txt fichier2.txt fichier3.txt ....
"""

import sys
import csv
from collections import Counter


# Récupère le nombre d'arguments
nbr_files = len(sys.argv)


def csv_to_list(file):
    # parcours du fichier
    with open(file, 'r') as f:
        reader = csv.reader(f)
        liste_f = []
        for row in reader:
            # stockage des valeurs dans une liste
            liste_f.append(row)
    return liste_f


def txt_to_list(file):
    # parcours de fichier1.txt
    with open(file, 'r') as fichier1:
        liste_fichier1 = []
        for line in fichier1:
            # stockage des valeurs dans une liste
            liste_fichier1.append(line.rstrip('\n'))
    return liste_fichier1


def comparaison(*args):
    """ 
    Compare l'ensemble des listes reçues en argument.
    Renvoie les valeurs communes.
    """
    # initialisation de la liste de retour
    liste_commune = []
    liste_retour = []
    # parcours des listes reçues en argument
    for liste in args:
        # parcours de la liste en cours
        for element in liste:
            # si l'élément n'est pas déjà dans la liste de retour
            if element not in liste_commune:
                # ajout de l'élément à la liste de retour
                liste_commune.append(element)
    dictionnaire = Counter(liste_commune)
    for key, value in dictionnaire.items():
        if value == nbr_files:
            liste_retour.append(key)
    return liste_retour


for i in range(len(sys.argv)):
    if i == 0:
        continue
    else:
        if sys.argv[i].endswith('.csv'):
            csv_to_list(sys.argv[i])
        else:
            txt_to_list(sys.argv[i])
