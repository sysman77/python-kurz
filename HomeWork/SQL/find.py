import sqlite3


def search_movies_by_title(title):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT movies.id, movies.title, movies.release_year, movies.genre, directors.name
    FROM movies
    JOIN directors ON movies.director_id = directors.id
    WHERE movies.title LIKE ?
    ''', ('%' + title + '%',))

    results = cursor.fetchall()
    conn.close()

    return results


def get_movies_by_actor(actor_name):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT movies.title
    FROM movies
    JOIN movie_actors ON movies.id = movie_actors.movie_id
    JOIN actors ON movie_actors.actor_id = actors.id
    WHERE actors.name LIKE ?
    ''', ('%' + actor_name + '%',))

    results = cursor.fetchall()
    conn.close()

    return results


def list_all_movies():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT movies.id, movies.title, movies.release_year, movies.genre, directors.name
    FROM movies
    JOIN directors ON movies.director_id = directors.id
    ''')

    movies = cursor.fetchall()

    for movie in movies:
        print(f"Movie ID: {movie[0]}, Title: {movie[1]}, Year: {movie[2]}, Genre: {movie[3]}, Director: {movie[4]}")

        cursor.execute('''
        SELECT actors.name
        FROM actors
        JOIN movie_actors ON actors.id = movie_actors.actor_id
        WHERE movie_actors.movie_id = ?
        ''', (movie[0],))

        actors = cursor.fetchall()
        actor_names = [actor[0] for actor in actors]
        print(f"Actors: {', '.join(actor_names)}")
        print('-' * 40)

    conn.close()
