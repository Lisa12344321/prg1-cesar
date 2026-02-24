alfabet = "abcdefghijklmnopqrstuvwxyzåäö"

meddelande = "Hej, vad GÖr du iDag!?"

nyckel = 700

resultat = ""

for bokstav in meddelande:
    try:
        if bokstav.isalpha():
            b = alfabet[(alfabet.index(bokstav.lower()) + nyckel) % 29]
            if bokstav.isupper():
                b = b.upper()
                resultat += b
            else:
                resultat += b

            print(resultat)
        else:
            resultat += bokstav
    except:
        None

print(f"Cesar chiffer: {resultat}")
print(f"Original meddelande: {meddelande}")
