import threading


# Funkce pro výpočet součtu prvků v seznamu
def calculate_sum(numbers):
    total_sum = sum(numbers)
    print(f"Součet prvků v seznamu je: {total_sum}")


# Funkce pro výpočet průměru prvků v seznamu
def calculate_average(numbers):
    if len(numbers) == 0:
        print("Seznam je prázdný, nelze vypočítat průměr.")
    else:
        average_value = sum(numbers) / len(numbers)
        print(f"Průměr prvků v seznamu je: {average_value}")


# Hlavní část programu
if __name__ == "__main__":
    # Uživatelský vstup - zadání hodnot do seznamu
    numbers = []
    n = int(input("Zadejte počet hodnot, které chcete vložit do seznamu: "))
    for i in range(n):
        num = float(input(f"Zadejte hodnotu {i + 1}: "))
        numbers.append(num)

    # Vytvoření vláken
    thread1 = threading.Thread(target=calculate_sum, args=(numbers,))
    thread2 = threading.Thread(target=calculate_average, args=(numbers,))

    # Spuštění vláken
    thread1.start()
    thread2.start()

    # Počkání na dokončení vláken
    thread1.join()
    thread2.join()
