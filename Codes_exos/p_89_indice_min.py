def indice_min(s):
    """Renvoie l'indice du minimum dans s.

    La première valeur si le minimum est présent plusieurs fois
    """
    res = 0
    for i in range(1,len(s)):
        if s[i][0] < s[res][0]:
            res = i
    return res 
