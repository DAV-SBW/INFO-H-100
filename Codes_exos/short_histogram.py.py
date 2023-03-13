def histogram(s):
    """Renvoie le dictionnaire des lettres dans s avec leur fréquence"""
    d = {}
    for c in s:
        d[c] = d.get(c,0) + 1
        # Si c existe alors on rajoute 1 à sa valeur dans d
        # Sinon, on ajoute la clé c et on lui assigne la valeur 0 par défaut
    return d
