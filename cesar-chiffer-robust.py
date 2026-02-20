alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

meddelande = "Hej, vad gör du idag!?"

nyckel = 1

resultat = meddelande

for bokstav in meddelande:
    try:
        if bokstav.isalpha():
            plats = (alfabet.index(bokstav.lower()) + nyckel) % 29
            if bokstav.isupper():  
                resultat = resultat.replace(bokstav, alfabet[plats].upper())
            else:
                resultat = resultat.replace(bokstav, alfabet[plats])
        
                print(resultat)
    except:
        None

print(f"Cesar chiffer: {resultat}")
print(f"Original meddelande: {meddelande}")
