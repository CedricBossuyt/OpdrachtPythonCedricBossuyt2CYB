Bedoeling applicatie:
Een persoon kan aangeven wanneer en hoelang hij gepoetst heeft, want tanden poetsen is zeer belangrijk.
--------------------------------------------------------------------------
Structuur van de database:
    CREATE TABLE personen (
                id INTEGER PRIMARY KEY,
                naam TEXT NOT NULL
            )

    CREATE TABLE poetssessies (
                id INTEGER PRIMARY KEY,
                persoon_id INTEGER,
                begintijd TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                duur INTEGER,
                FOREIGN KEY (persoon_id) REFERENCES personen(id)
            )

Het .db bestand moet zich bevinden in: apps/db/

het bestand poetser.py noemde origineel person.py maar er waren fouten in de terminal door de basisklasse Person, dus heb ik het maar poetser.py genoemd