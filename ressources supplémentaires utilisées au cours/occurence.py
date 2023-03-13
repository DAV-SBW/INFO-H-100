import os

def mot_et_occurrence(t):
    """ construit dict avec mots et occurences """
    d = {}
    s = t.split()
    for mot in s:
        if mot not in d:
            d[mot] = 1
        else:
            d[mot] += 1
    return d

os.chdir('/Users/tmassart/Enseignement/SVN/tmassart/Python/scripts')

f = open('le-petit-prince.txt',encoding='utf-8')
text = f.read()
d = mot_et_occurrence(text)
if 'mouton' in d:
    print('le mot mouton apparaît', d['mouton'], 'fois dans le texte')
else:
    print("le mot mouton n'apparaît pas dans le texte")
f.close()

        
