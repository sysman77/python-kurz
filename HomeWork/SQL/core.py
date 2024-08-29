import sqlite3


def add_movie(title, release_year, genre, director_id, actors):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO movies (title, release_year, genre, director_id)
    VALUES (?, ?, ?, ?)
    ''', (title, release_year, genre, director_id))

    movie_id = cursor.lastrowid

    for actor_id in actors:
        cursor.execute('''
        INSERT INTO movie_actors (movie_id, actor_id)
        VALUES (?, ?)
        ''', (movie_id, actor_id))

    conn.commit()
    conn.close()


def add_actor(name, birth_year):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO actors (name, birth_year)
    VALUES (?, ?)
    ''', (name, birth_year))

    conn.commit()
    conn.close()


def add_director(name, birth_year):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO directors (name, birth_year)
    VALUES (?, ?)
    ''', (name, birth_year))

    conn.commit()
    conn.close()
