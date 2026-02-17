alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

meddelande = "läxa"

nyckel = 3

resultat = meddelande

for bokstav in meddelande:
    try:
        plats = (alfabet.index(bokstav) + nyckel) % 29
        resultat = resultat.replace(bokstav, alfabet[plats])
    except:
        None

print(f"Cesar chiffer: {resultat}")
print(f"Original meddelande: {meddelande}")
