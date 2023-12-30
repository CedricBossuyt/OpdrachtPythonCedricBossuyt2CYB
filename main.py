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

if __name__ == "__main__":
    main()