from apps.classes.poetser import Poetser
from apps.classes.poetssessie import Poetssessie
from apps.db.database import Database
from apps.util.helper import input_naam, input_poetssessie_duur

def main():
    poetser_naam = input_naam()
    poetser = Poetser(poetser_naam)

    db = Database('tandpoetssessie.db')

    poetser_id = db.voeg_persoon_toe(poetser)

    poetssessie_duur = input_poetssessie_duur()
    poetssessie = Poetssessie(poetser_id, poetssessie_duur)

    poetssessie_id = db.start_poetssessie(poetssessie)

    poetssessie_info = db.get_poetssessie_info(poetssessie_id)
    if poetssessie_info:
        naam, begintijd, duur = poetssessie_info
        print(f"{naam} is begonnen met poetsen om {begintijd} en heeft {duur} minuten gepoetst.")
        if duur > 5:
            print("Oei, toch niet TE lang poetsen he...")
        elif duur >= 2:
            print("Flink!")
        else:
            print("Stout, je zou meer moeten poetsen!")
    
    export_to_csv = input("Wil je alle informatie naar CSV exporteren? (ja/nee): ").lower().strip() == 'ja'

    if export_to_csv:
        db.export_to_csv()
        print("Alle informatie is geëxporteerd naar poetsInfo.csv.")

if __name__ == "__main__":
    main()