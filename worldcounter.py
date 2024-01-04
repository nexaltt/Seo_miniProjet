

def analyser_frequences_mots(texte):

    mots = texte.lower().split()
    compteur_mots = {}
    
    for mot in mots:
        compteur_mots[mot] = compteur_mots.get(mot, 0) + 1

    return sorted(compteur_mots.items(), key=lambda x: x[1], reverse=True)
