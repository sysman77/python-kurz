import sqlite3


def create_tables():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    # Vytvoření tabulky pro filmy
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        release_year INTEGER,
        genre TEXT,
        director_id INTEGER,
        FOREIGN KEY (director_id) REFERENCES directors(id)
    )
    ''')

    # Vytvoření tabulky pro herce
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS actors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birth_year INTEGER
    )
    ''')

    # Vytvoření tabulky pro režiséry
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS directors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birth_year INTEGER
    )
    ''')

    # Vytvoření tabulky pro vazby mezi filmy a herci
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movie_actors (
        movie_id INTEGER,
        actor_id INTEGER,
        PRIMARY KEY (movie_id, actor_id),
        FOREIGN KEY (movie_id) REFERENCES movies(id),
        FOREIGN KEY (actor_id) REFERENCES actors(id)
    )
    ''')

    conn.commit()
    conn.close()


create_tables()
