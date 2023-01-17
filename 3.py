import hashlib
from datetime import datetime

def attaque_brute_force_hash(h):
    n = 0 # pour compter le nombre de mots
    t0 = datetime.now() # l'heure à l'instant présent 
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for a in alphabet: 
        for b in alphabet:
            for c in alphabet: 
                mot = a+b+c 
                n=n+1
                
                if hashlib.sha256(mot.encode()).hexdigest() == h: 
                    print()
                    print("TROUVÉ ! '{}' a le hash {},".format(mot,h))
                    print("{} mot(s) ont étés testés en {} seconde(s).".format(n, (datetime.now()-t0).total_seconds())) 
                    return
                
                if n % 1000 == 0: 
                    print(".", end="")
                    
    print()
    print("{} mot(s) ont étés testés en {} seconde(s),".format(n, (datetime.now()-t0).total_seconds())) 
    print("Aucun des mots testés n'avait le hash {}.".format(h))

print(attaque_brute_force_hash("07123e1f482356c415f684407a3b8723e10b2cbbc0b8fcd6282c49d37c9c1abc"))