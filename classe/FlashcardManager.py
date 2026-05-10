import sqlite3
import random
from datetime import datetime, timedelta

class FlashcardManager:
    def __init__(self, db_path="flashcards.db"):
        self.bd =self.connect_db()
        

    def connect_db(self,bd='flashcards' ):
        """Connecte à la base de données SQLite."""
        base = bd+'.db'
        connection = sqlite3.connect( base )  # Nom de la base de données
        return connection

    def create_table(self,connection):
        """Crée les tables flashcards et famille si elle n'existent pas."""
        flashcards="""
            CREATE TABLE IF NOT EXISTS flashcards (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT,
                reponse TEXT,
                famille INTEGER,
                niveau INTEGER,
                dateDeVue INTEGER
            )
        """
        famille="""
            CREATE TABLE IF NOT EXISTS famille (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                famille TEXT
            )
        """
        cursor = connection.cursor()
        
        cursor.execute( flashcards )
        connection.commit()

        cursor.execute( famille )
        connection.commit()

    def insert_flashcard(self,connection, question, reponse, famille, niveau, dateDeVue):
        """Insère une nouvelle flashcard dans la base de données."""
        
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO flashcards (question, reponse, famille, niveau, dateDeVue)
            VALUES (?, ?, ?, ?, ?)
        """, (question, reponse, famille, niveau, dateDeVue))
        connection.commit()

    def insert_famille(self,connection, famille ):
        """Insère une nouvelle famille dans la base de données."""
        
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO famille ( famille )
            VALUES (?)
        """, ( famille ))
        connection.commit()

    def get_all_flashcards(self,connection):
    #"""Récupère toutes les flashcards de la base de données ,
    # sauf si pas achivé(niveau != 0) , ou dateDeVue passé .
    # et limité a 15 entré 
    # et choisi aléatoirement dans la base de donné"""
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM flashcards WHERE niveau != 0 AND dateDeVue < date('now') ORDER BY RANDOM LIMIT 15")
        liste_de_tuple = cursor.fetchall()
    # met aléatoirement le resultat     
        liste_flashcards = list(liste_de_tuple)
        random.shuffle(liste_flashcards)

        return liste_flashcards


    def get_all_famille(self,connection):
        """Récupère toutes les familles de la base de données."""
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM familles  ")
        liste_de_tuple = cursor.fetchall()
        return liste_de_tuple