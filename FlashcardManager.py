import sqlite3
from datetime import datetime, timedelta

class FlashcardManager:
    def __init__(self, db_path="flashcards.db"):
        self.conn = sqlite3.connect(db_path)
        self._init_db()

    def _init_db(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS flashcards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            reponse TEXT,
            niveau INTEGER DEFAULT 1 CHECK (niveau BETWEEN 1 AND 9),
            dateDeVue INTEGER NOT NULL
        )
        """)
        self.conn.commit()

    def ajouter_carte(self, question: str, reponse: str):
        date_vue = int(datetime.now().timestamp())
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO flashcards (question, reponse, dateDeVue) VALUES (?, ?, ?)",
            (question, reponse, date_vue)
        )
        self.conn.commit()
