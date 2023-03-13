"""
Un polynome est représenté par une liste p de coéfficients p[i] pour i allant de 0 à i
i est donc l'exposant (l'ordre du terme)
p[i] le coéfficient
Ex : [2, 3, 0, 8, 1] = 2 + 3x + 8x^3 + x^4
"""

def peval(plist, x):
    """
    Evalue le polynome en x
    :param plist:
    :param x:
    :return val:
    """
    val = 0.0
    for i in range(len(plist)): val += plist[i]*x**i        # Coéf*valx**expi
    return val

def clean(p):
    """
    Nettoie p en supprimant les termes à coéfficients nuls
    :param p:
    :return p:
    """
    while len(p) > 0 and p[-1] == 0.0:  # Supprime les coéfs nuls sauf le polynome 0.0
        del p[-1]
    return p

def add(p1, p2):
    """
    Renvoie la somme (nettoyée) de 2 polynomes
    :param p1:
    :param p2:
    """
    if len(p1) < len(p2):
        p1, p2 = p2, p1   #On va sommer sur p1
    new = p1[:]
    for i in range(len(p2)):
        new[i] += p2[i]
    return clean(new)

def mult_const(p, c):
    """
    Renvoie p multiplié par une constante non nulle.
    :param p:
    :param c:
    :return p*c:
    """
    res = p[:]
    for i in range(len(p)):
        res[i] *= c
    return res

def sub(p1, p2):
    """
    Renvoie la différence de 2 polynomes
    :param p1:
    :param p2:
    :return p1-p2:
    """
    return add(p1, mult_const(p2, -1))

def multiply(p1, p2):
    """
    Renvoie le produit de 2 polynomes
    :param p1:
    :param p2:
    :return p1*p2:
    """
    if len(p1) > len(p2):
        p1, p2 = p2, p1
    new = [0.0]
    for i in range(len(p1)):
        new = 0
    return new