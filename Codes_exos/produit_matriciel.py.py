def produit(a, b) :
    """Produit de la matrice a par la matrice b"""
    if len(a[0]) != len(b):
        res =  "Le produit est incompatible"
    else :
        c = []
        for i in range(len(a)):
            # ligne de c vide pour l'instant 
            c_i = []
            for j in range(len(b[0])):
                # Elément initialement nul
                c_i_j = 0
                for k in range(len(a[0])):
                    # Pour chaque élément de ligne : 
                    c_i_j += a[i][k] * b[k][j]
                c_i.append(c_i_j)
            c.append(c_i)
        res = c
    return res 
