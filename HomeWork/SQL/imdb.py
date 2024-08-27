import imdb
import sqlite3


def add_movie_by_imdb_id(imdb_id):
    ia = imdb.IMDb()

    # Načtení informací o filmu z IMDb
    movie = ia.get_movie(imdb_id)

    title = movie.get('title')
    year = movie.get('year')
    genre = ', '.join(movie.get('genres', []))
    imdb_rating = movie.get('rating')

    # Načtení informací o režisérovi
    director_name = movie.get('director')[0]['name']

    # Načtení seznamu herců
    actors = movie.get('cast')[:5]  # Omezíme na 5 hlavních herců

    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    # Přidání režiséra do databáze (pokud neexistuje)
    cursor.execute('''
    SELECT id FROM directors WHERE name = ?
    ''', (director_name,))
    director = cursor.fetchone()

    if director is None:
        cursor.execute('''
        INSERT INTO directors (name, birth_year)
        VALUES (?, ?)
        ''', (director_name, None))
        director_id = cursor.lastrowid
    else:
        director_id = director[0]

    # Přidání filmu do databáze
    cursor.execute('''
    INSERT INTO movies (title, release_year, genre, director_id, imdb_rating)
    VALUES (?, ?, ?, ?, ?)
    ''', (title, year, genre, director_id, imdb_rating))

    movie_id = cursor.lastrowid

    # Přidání herců do databáze
    for actor in actors:
        actor_name = actor['name']

        cursor.execute('''
        SELECT id FROM actors WHERE name = ?
        ''', (actor_name,))
        actor_entry = cursor.fetchone()

        if actor_entry is None:
            cursor.execute('''
            INSERT INTO actors (name, birth_year)
            VALUES (?, ?)
            ''', (actor_name, None))
            actor_id = cursor.lastrowid
        else:
            actor_id = actor_entry[0]

        cursor.execute('''
        INSERT INTO movie_actors (movie_id, actor_id)
        VALUES (?, ?)
        ''', (movie_id, actor_id))

    conn.commit()
    conn.close()

    print(f"Movie '{title}' has been added successfully from IMDb.")
