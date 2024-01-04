import csv


def eliminer_mots_inutiles(dictionnaire, liste_mots_inutiles):

    dictionnaire_nettoye = dict(dictionnaire)

    # Retirer les mots inutiles du dictionnaire
    for mot in liste_mots_inutiles:
        dictionnaire_nettoye.pop(mot, None)

    return dictionnaire_nettoye

def charger_mots_inutiles(chemin_fichier_csv):

    mots_inutiles = []

    with open(chemin_fichier_csv, newline='', encoding='utf-8') as fichier_csv:
        lecteur_csv = csv.reader(fichier_csv)
        for ligne in lecteur_csv:
            mots_inutiles.extend(ligne)

    return mots_inutiles
