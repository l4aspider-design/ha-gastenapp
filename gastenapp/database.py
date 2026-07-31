import sqlite3
from datetime import datetime

DB = "/data/gasten.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS boekingen (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        naam TEXT NOT NULL,
        personen INTEGER NOT NULL,
        aankomst TEXT NOT NULL,
        vertrek TEXT NOT NULL,
        nachten INTEGER NOT NULL,
        bedrag REAL,
        status TEXT,
        toeristenbelasting REAL,
        aangemaakt TEXT
    )
    """)

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


def opslaan(naam, personen, aankomst, vertrek, bedrag, status):
    start = datetime.strptime(aankomst, "%Y-%m-%d")
    einde = datetime.strptime(vertrek, "%Y-%m-%d")

    nachten = (einde - start).days
    belasting = personen * nachten * 5

    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    INSERT INTO boekingen
    VALUES (NULL,?,?,?,?,?,?,?,?,?)
    """,
    (
        naam,
        personen,
        aankomst,
        vertrek,
        nachten,
        bedrag,
        status,
        belasting,
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()
