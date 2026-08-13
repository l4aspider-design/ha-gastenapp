import sqlite3
from datetime import datetime

DB = "/data/gasten.db"


def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS boekingen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        boeker TEXT NOT NULL,
        gast1 TEXT,
        gast2 TEXT,
        personen INTEGER NOT NULL,
        aankomst TEXT NOT NULL,
        vertrek TEXT NOT NULL,
        bedrag REAL,
        nachtprijs REAL,
        aangemaakt TEXT
    )
    """)

    # Bestaande databases uitbreiden met nachtprijs
    try:
        c.execute("ALTER TABLE boekingen ADD COLUMN nachtprijs REAL")
    except sqlite3.OperationalError:
        pass

    conn.commit()
    conn.close()

def alle_boekingen():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    c.execute("""
    SELECT * FROM boekingen
    ORDER BY aankomst DESC
    """)

    data = c.fetchall()
    conn.close()

    return data


def opslaan(boeker, gast1, gast2, personen, aankomst, vertrek, nachtprijs):

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    INSERT INTO boekingen
    VALUES (NULL,?,?,?,?,?,?,?,?,?)
    """,
    (
        boeker,
        gast1,
        gast2,
        personen,
        aankomst,
        vertrek,
        0,
        nachtprijs,
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()

def verwijderen(id):

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute(
        "DELETE FROM boekingen WHERE id=?",
        (id,)
    )
   
    conn.commit()
    conn.close()


def ophalen(id):

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    c = conn.cursor()

    c.execute(
        "SELECT * FROM boekingen WHERE id=?",
        (id,)
    )

    data = c.fetchone()

    conn.close()

    return data



def aanpassen(id, boeker, gast1, gast2, personen, aankomst, vertrek, bedrag):

    conn = sqlite3.connect(DB)

    c = conn.cursor()

    c.execute("""
    UPDATE boekingen
    SET boeker=?,
        gast1=?,
        gast2=?,
        personen=?,
        aankomst=?,
        vertrek=?,
        bedrag=?
    WHERE id=?
    """,
    (
        boeker,
        gast1,
        gast2,
        personen,
        aankomst,
        vertrek,
        bedrag,
        id
    ))

    conn.commit()
    conn.close()


