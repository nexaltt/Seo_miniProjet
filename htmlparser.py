import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse



def nettoyer_html(html):

    """ Supprime toutes balises  """
    soup = BeautifulSoup(html, 'html.parser')
    texte_nettoye = soup.get_text(separator=' ', strip=True)
    
    return texte_nettoye

def extraire_donnees_balises(html, balise, attribut):

    """ Extrait données d'une balise html """
    donnees = []
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.find_all(balise)
    for element in elements:
        valeur = element.get(attribut)
        if valeur:
            donnees.append(valeur)
            
    return donnees

def obtenir_nom_domaine(url):

    """ extrait nom domaine """
    return urlparse(url).netloc

def filtrer_urls_par_domaine(domaine, urls):

    """ sépare url en deux liste """
    urls_domaine = []
    urls_externes = []

    domaine_reference = obtenir_nom_domaine("http://" + domaine).lower()

    for url in urls:
        domaine_url = obtenir_nom_domaine(url).lower()
        if domaine_url == domaine_reference:
            urls_domaine.append(url)
        else:
            urls_externes.append(url)

    return urls_domaine, urls_externes


def recuperer_html(url):

    """ recupere conenue html """
    try:
        reponse = requests.get(url)
        if reponse.status_code == 200:
            return reponse.text
        else:
            print(f"Erreur HTTP, statut : {reponse.status_code}")
            return None

    except requests.RequestException as erreur:
        print(f"Erreur lors de la récupération du HTML : {erreur}")
        return None
