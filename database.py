import sqlite3
import random

def connect_db(bd='flashcards' ):
    """Connecte à la base de données SQLite."""
    base = bd+'.db'
    connection = sqlite3.connect( base )  # Nom de la base de données
    return connection

def create_table(connection):
    """Crée les tables flashcards et famille si elle n'existent pas."""
    flashcards="""
        CREATE TABLE IF NOT EXISTS flashcards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            reponse TEXT,
            famille TEXT,
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

def insert_flashcard(connection, question, reponse, famille, niveau, dateDeVue):
    """Insère une nouvelle flashcard dans la base de données."""
    
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO flashcards (question, reponse, famille, niveau, dateDeVue)
        VALUES (?, ?, ?, ?, ?)
    """, (question, reponse, famille, niveau, dateDeVue))
    connection.commit()

def get_all_flashcards(connection):
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

def get_flashcard_by_id(connection, card_id):
    """Récupère une flashcard spécifique par son ID."""
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM flashcards WHERE id = ?", (card_id,))
    row = cursor.fetchone()
    return row

def insert_famille(connection, famille_nom):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO famille (famille) VALUES (?)", (famille_nom,))
    connection.commit()

def get_famille(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM famille")
    return cursor.fetchall()  # ✅ Retourne TOUTES les lignes

def get_all_ID(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM flashcards")
    return cursor.fetchall()  # ✅ Retourne TOUTES les lignes

