"""Sur l’écran d’accueil de votre smartphone, vous pouvez placer des dossiers (de raccourcis) d’applications.
Imaginons que ces dossiers puissent contenir des sous-dossiers.
Une application sera représentée par un tuple (nom, identifiant), l’identifiant étant un entier unique
définissant le raccourci vers l’application. Un dossier d’applications sera représenté par un tuple
(nom, liste d’applications ou de sous-dossiers).
Ecrivez une fonction find_apps(name, dossier_apps) qui reçoit un mot et un dossier d’applications et
qui renvoie une liste de toutes les applications (liste de tuples) dont le nom contient le mot donné.
Par exemple :

dossier_apps = ("Mes Applications", [("Facebook", 123),("WhatApp", 37),("Google Apps", [
("Google", 1),("Google Maps", 28),("Youtube", 44),("Google Drive", 17)]),
("Utile", [("Horloge", 56),("Calculatrice", 52)]),
("Peu utile", [("Météo", 107),("Téléchargements", 8),("Encore Google", [("Google Play Films", 174),
("Google Play Musique", 66)])])])
##On recherche toutes les applis de Google
>>> find_apps("Google", dossier_apps)
[('Google', 1), ('Google Maps', 28), ('Google Drive', 17), ('Google Play Films', 174), ('Google Play Musique', 66)]
"""

def find_apps(name, dossiers_apps):
    res = []
    for c in dossiers_apps[1]:
        if type(c[1]) == list :
            res.extend(find_apps(name,c))
        elif name in c[0]:
            res.append(c)
    return res


def find_apps(name, dossiers_apps):
    res = []
    for c in dossiers_apps[1]:
        if tyoe(c[1]) == list :
            res.extend(find_apps(name,c))
        elif name in c[0]:
            res.append(c)
    return res 
