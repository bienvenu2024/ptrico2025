def factoriel_for(n):
    resultat = 1
    for i in range(1, n+1):
        resultat *=i
    return resultat

def factoriel_while(n):
    resultat = 1
    i=1
    while i <=n:
        resultat *=i
        i += 1
    return resultat

nom = "AKPANOUDO"
prenom = "Patrick"

for i in range(1, 51):
    if i%3 == 0 and i%5 == 0:
        print(nom, prenom)
    elif i%3 == 0:
        print(nom)
    elif i%5 == 0:
        print(prenom)
