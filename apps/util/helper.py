def input_naam():
    return input("Voer je naam in: ")

def input_poetssessie_duur():
    while True:
        duur_input = input("Voer de duur van de poetsessie in minuten in: ")
        try:
            duur = float(duur_input)
            if duur < 0:
                print("Voer een positief getal in voor de duur.")
            else:
                return duur
        except ValueError:
            print("Voer a.u.b. een geldig getal in.")