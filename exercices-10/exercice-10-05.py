# exo 10.5
# Créer une fonction nommée `compare()` qui :
# - prend deux paramètres `a` et `b` de type `float`
# - renvoie une valeur de type `int`
# - renvoie 1 si `a` est plus grand que `b`
# - renvoie -1 si `a` est plus petit que `b`
# - renvoie 0 si `a` et `b` sont égaux
# Appelez la fonction et affichez le résultat

# réponse 10.5
def compare(a,b):
    if(float(a) > float(b)):
        return 1
    elif(float(a) < float(b)):
        return -1
    else:
        return 0

print(compare(int(2),int(1.5))) 
