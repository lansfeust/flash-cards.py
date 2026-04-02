import sqlite3
import datetime
import random

def connect_db():
    """Connecte à la base de données SQLite."""
    conn = sqlite3.connect('flashcards.db')  # Nom de la base de données
    return conn

def create_table(conn):
    """Crée la table flashcards si elle n'existe pas."""
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS flashcards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            reponse TEXT,
            type_carte TEXT,
            niveau INTEGER,
            dateDeVue INTEGER
        )
    """)
    conn.commit()

def insert_flashcard(conn, question, reponse, type_carte, niveau, dateDeVue):
    """Insère une nouvelle flashcard dans la base de données."""
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO flashcards (question, reponse, type_carte, niveau, dateDeVue)
        VALUES (?, ?, ?, ?, ?)
    """, (question, reponse, type_carte, niveau, dateDeVue))
    conn.commit()

def get_all_flashcards(conn):
    """Récupère toutes les flashcards de la base de données."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flashcards")
    rows = cursor.fetchall()
    return rows

def get_flashcard_by_id(conn, card_id):
    """Récupère une flashcard spécifique par son ID."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flashcards WHERE id = ?", (card_id,))
    row = cursor.fetchone()
    return row