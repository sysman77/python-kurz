"""
Vyviňte aplikaci, která napodobuje frontu požadavků serveru. Měli by existovat klienti, kteří posílají požadavky
 na server, každý má svou prioritu.

Každý nový klient je zařazen do fronty v závislosti na prioritě. Uložte statistiky požadavků (uživatel, čas)
do samostatné fronty.

Poskytněte statistický výstup. Potřebné datové struktury si můžete vybrat s
"""

"""
queue.PriorityQueue pro prioritní frontu.
collections.deque pro ukládání statistik.

Třídu Request, která bude obsahovat informace o uživateli, čase a prioritě.
Třídu Server, která bude spravovat přijímání požadavků a ukládání statistik.
Implementujeme funkce pro přidávání požadavků a získávání statistik.

"""

import time
from queue import PriorityQueue
from collections import deque

class Request:
    def __init__(self, user, priority):
        self.user = user
        self.priority = priority
        self.timestamp = time.time()

    def __lt__(self, other):
        return self.priority < other.priority

class Server:
    def __init__(self):
        self.request_queue = PriorityQueue()
        self.statistics = deque()

    def add_request(self, user, priority):
        request = Request(user, priority)
        self.request_queue.put(request)
        self.statistics.append((request.user, request.timestamp))
        print(f'Request from user {user} with priority {priority} added at {request.timestamp}')

    def process_request(self):
        if self.request_queue.empty():
            print('No requests to process.')
            return None
        request = self.request_queue.get()
        print(f'Processing request from user {request.user} with priority {request.priority} at {time.time()}')
        return request

    def get_statistics(self):
        print('Statistics of requests:')
        for stat in self.statistics:
            print(f'User: {stat[0]}, Time: {stat[1]}')

# Příklad použití:
server = Server()
server.add_request('User1', 2)
server.add_request('User2', 1)
server.add_request('User3', 3)

# Zpracování požadavků:
server.process_request()
server.process_request()
server.process_request()

# Výstup statistik:
server.get_statistics()
