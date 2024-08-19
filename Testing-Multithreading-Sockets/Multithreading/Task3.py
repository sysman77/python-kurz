import threading
import random

# Generate 30 random integers between 1 and 100 (inclusive)
random_numbers = [random.randint(1, 100) for _ in range(30)]

# Funkce pro zápis sudých čísel do souboru
def write_even_numbers(numbers, output_file):
    even_numbers = [num for num in numbers if num % 2 == 0]
    with open(output_file, 'w') as file:
        for num in even_numbers:
            file.write(f"{num}\n")
    print(f"Počet sudých čísel: {len(even_numbers)}")


# Funkce pro zápis lichých čísel do souboru
def write_odd_numbers(numbers, output_file):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    with open(output_file, 'w') as file:
        for num in odd_numbers:
            file.write(f"{num}\n")
    print(f"Počet lichých čísel: {len(odd_numbers)}")


# Hlavní část programu
if __name__ == "__main__":

    # Generate 30 random integers between 1 and 100 (inclusive)
    numbers = [random.randint(1, 100) for _ in range(30)]


    # Cesty k výstupním souborům
    even_output_file = "even_numbers.txt"
    odd_output_file = "odd_numbers.txt"

    # Vytvoření vláken
    thread1 = threading.Thread(target=write_even_numbers, args=(numbers, even_output_file))
    thread2 = threading.Thread(target=write_odd_numbers, args=(numbers, odd_output_file))

    # Spuštění vláken
    thread1.start()
    thread2.start()

    # Počkání na dokončení vláken
    thread1.join()
    thread2.join()
