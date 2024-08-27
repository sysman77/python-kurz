from core import *
from find import *
from imdb import *


def main_menu():
    while True:
        print("\nMovie Database")
        print("1. Add a new movie by IMDb ID")
        print("2. Add a new actor")
        print("3. Add a new director")
        print("4. Search movies by title")
        print("5. List all movies")
        print("6. List movies by actor")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            imdb_id = input("Enter IMDb ID of the movie: ")
            add_movie_by_imdb_id(imdb_id)

        elif choice == '2':
            name = input("Enter actor's name: ")
            birth_year = int(input("Enter birth year: "))
            add_actor(name, birth_year)
            print("Actor added successfully.")

        elif choice == '3':
            name = input("Enter director's name: ")
            birth_year = int(input("Enter birth year: "))
            add_director(name, birth_year)
            print("Director added successfully.")

        elif choice == '4':
            title = input("Enter movie title to search: ")
            results = search_movies_by_title(title)
            for result in results:
                print(result)

        elif choice == '5':
            list_all_movies()

        elif choice == '6':
            actor_name = input("Enter actor's name: ")
            results = get_movies_by_actor(actor_name)
            for result in results:
                print(result)

        elif choice == '7':
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main_menu()
