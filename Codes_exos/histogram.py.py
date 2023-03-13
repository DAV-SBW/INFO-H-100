def histrogram(s):
    """Renvoie le dico des lettres dans s avec leur fréquence"""
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
            # On ajoute le c et la valeur 1 correpondante
        else :
            d[c] += 1
    return d
