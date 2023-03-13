def lecture_liens():
  g = {}
  x = input('personne suivante (rien si terminé) : ')
  while x!= '':
    amis = input('liste de ses amis : ')
    g[x] = amis.strip().split()
    x = input('personne suivante (rien si terminé) : ')
  return g

def connaissance_indirecte(g,x):
   s = {x}
   to_do = {x}
   while len(to_do) > 0:
      z = to_do.pop()
      # print("Debug personne:", z) # Debug
      for ami in g[z]:
        # print("Debug ami:", ami) # Debug
        if ami not in s:
           s.add(ami)
           to_do.add(ami) 
   return s - {x}

mon_graphe = lecture_liens()
personne = input('De qui voulez-vous la liste des connaissances indirectes? : ')
if personne != '' and personne in mon_graphe :
   print("amis indirects de ", personne, " : ", connaissance_indirecte(mon_graphe,personne))
