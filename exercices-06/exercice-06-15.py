# exo 6.15
# Trouvez la chaîne de caractères la plus longue dans une liste.
# Affichez son index, sa valeur et sa longueur.
#
# ATTENTION : ne pas utiliser la fonction list.index()
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur', 'adipiscing', 'elit']
max_len = 0
for long in my_list: 
    if(len(long) > max_len): 
        max_len = len(long) 
        res = long  
print("La chaine la plus longue est: ", res) 
print("Sa valeur: ", res) 
print("Sa longueur est de: ", max_len) 
# réponse 6.15

