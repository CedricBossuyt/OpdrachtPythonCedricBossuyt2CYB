import sqlite3
import os
from datetime import datetime

class Database:
    def __init__(self, db_name):
        db_path = os.path.join('apps', 'db', db_name)
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS personen (
                id INTEGER PRIMARY KEY,
                naam TEXT NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS poetssessies (
                id INTEGER PRIMARY KEY,
                persoon_id INTEGER,
                begintijd TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                duur INTEGER,
                FOREIGN KEY (persoon_id) REFERENCES personen(id)
            )
        ''')
        self.conn.commit()

    def voeg_persoon_toe(self, persoon):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO personen (naam)
            VALUES (?)
        ''', (persoon.naam,))
        self.conn.commit()
        return cursor.lastrowid

    def start_poetssessie(self, poetssessie):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO poetssessies (persoon_id, begintijd, duur)
            VALUES (?, ?, ?)
        ''', (poetssessie.persoon_id, datetime.now(), poetssessie.duur))
        self.conn.commit()
        return cursor.lastrowid

    def get_poetssessie_info(self, poetssessie_id):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT personen.naam, poetssessies.begintijd, poetssessies.duur
            FROM poetssessies
            INNER JOIN personen ON personen.id = poetssessies.persoon_id
            WHERE poetssessies.id = ?
        ''', (poetssessie_id,))
        return cursor.fetchone()