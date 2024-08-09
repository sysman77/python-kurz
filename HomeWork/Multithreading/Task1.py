import threading
import random

# Společné proměnné
numbers = []
sum_result = 0
average_result = 0

# Zámek pro synchronizaci
list_filled_event = threading.Event()


# Funkce pro vlákno, které naplní seznam náhodnými čísly
def fill_list():
    global numbers
    numbers = [random.randint(1, 100) for _ in range(10)]
    print(f"Seznam náhodných čísel: {numbers}")
    # Uvolnění zámku pro další vlákna
    list_filled_event.set()


# Funkce pro vlákno, které spočítá součet
def calculate_sum():
    global sum_result
    # Čekání na naplnění seznamu
    list_filled_event.wait()
    sum_result = sum(numbers)
    print(f"Součet čísel v seznamu: {sum_result}")

# Funkce pro vlákno, které spočítá průměr


def calculate_average():
    global average_result
    # Čekání na naplnění seznamu
    list_filled_event.wait()
    average_result = sum(numbers) / len(numbers)
    print(f"Průměr čísel v seznamu: {average_result:.2f}")


# Vytvoření a spuštění vláken
thread_fill = threading.Thread(target=fill_list)
thread_sum = threading.Thread(target=calculate_sum)
thread_average = threading.Thread(target=calculate_average)

thread_fill.start()
thread_sum.start()
thread_average.start()

# Čekání na dokončení všech vláken
thread_fill.join()
thread_sum.join()
thread_average.join()
