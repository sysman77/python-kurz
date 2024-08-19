import threading
import time
from random import random

def find_largest(numbers):
    # nejaka operacia narocnejsia
    time.sleep(random())
    numbers.append(-1000) # potencionalna chyba
    largest = max(numbers)
    print(f"Largest value: {largest}")


def find_smallest(numbers):
    # nejaka narocnejsia opercia
    time.sleep(random())
    smallest = min(numbers)
    print(f"Smallest value: {smallest}")


user_values = input("Enter values separated by commas: ")
values_list = [int(x) for x in user_values.split(',')]

thread_largest = threading.Thread(target=find_largest, args=(values_list,))
thread_smallest = threading.Thread(target=find_smallest, args=(values_list,))
#target(args)

thread_largest.start()
thread_smallest.start()

thread_largest.join()
thread_smallest.join()