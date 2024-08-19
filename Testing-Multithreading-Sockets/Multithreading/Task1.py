import threading


# Funkce pro nalezení největší hodnoty v seznamu
def find_maximum(numbers):
    maximum_value = max(numbers)
    print(f"Největší hodnota v seznamu je: {maximum_value}")


# Funkce pro nalezení nejmenší hodnoty v seznamu
def find_minimum(numbers):
    minimum_value = min(numbers)
    print(f"Nejmenší hodnota v seznamu je: {minimum_value}")


# Hlavní část programu
if __name__ == "__main__":
    # Uživatelský vstup - zadání hodnot do seznamu
    numbers = []
    n = int(input("Zadejte počet hodnot, které chcete vložit do seznamu: "))
    for i in range(n):
        num = float(input(f"Zadejte hodnotu {i + 1}: "))
        numbers.append(num)

    # Vytvoření vláken
    thread1 = threading.Thread(target=find_maximum, args=(numbers,))
    thread2 = threading.Thread(target=find_minimum, args=(numbers,))

    # Spuštění vláken
    thread1.start()
    thread2.start()

    # Počkání na dokončení vláken
    thread1.join()
    thread2.join()
