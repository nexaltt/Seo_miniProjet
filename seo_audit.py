from worldcounter import analyser_frequences_mots
from parasitefilter import eliminer_mots_inutiles, charger_mots_inutiles
from htmlparser import nettoyer_html, extraire_donnees_balises, recuperer_html

def audit_seo_page(url):

    html = recuperer_html(url)

    if html:
        # Nettoyage du texte en retirant les balises HTML
        texte_nettoye = nettoyer_html(html)

        # Analyse des fréquences des mots dans le texte nettoyé
        frequences_mots = analyser_frequences_mots(texte_nettoye)
        print("Top 3 des mots les plus fréquents :")
        print(frequences_mots[:3], "\n")

        # Chargement et application du filtre de mots inutiles
        chemin_fichier_parasites = "inutiles.csv"
        mots_inutiles = charger_mots_inutiles(chemin_fichier_parasites)
        frequences_filtrees = eliminer_mots_inutiles(frequences_mots, mots_inutiles)
        print("Fréquences des mots après filtrage des mots inutiles :")
        print(frequences_filtrees, "\n")

        # Extraction et affichage des liens entrants
        liens_entrants = extraire_donnees_balises(html, 'a', 'href')
        print("Nombre de liens entrants :", len(liens_entrants), liens_entrants)

        # Extraction des balises alt des images
        balises_alt_images = extraire_donnees_balises(html, 'img', 'alt')
        print("Balises alt trouvées dans les images :", balises_alt_images)

if __name__ == "__main__":
    # Demande de l'URL de la page à analyser
    url_a_analyser = input("Entrez l'URL de la page pour l'audit SEO : \n")
    audit_seo_page(url_a_analyser)
