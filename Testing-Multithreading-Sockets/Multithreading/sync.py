import threading

counter = 0

def increment():
    global counter
    for _ in range(5000001):
        counter += 1

def decrement():
    global counter
    for _ in range(3000000):
        counter -= 1

thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=decrement)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f'Final counter value (without lock): {counter}')