import time

class Request:
    def __init__(self, user, priority):
        self.user = user
        self.priority = priority
        self.timestamp = time.time()

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def put(self, request):
        self.queue.append(request)
        self.queue.sort(key=lambda req: req.priority)

    def get(self):
        if not self.queue:
            return None
        return self.queue.pop(0)

    def empty(self):
        return len(self.queue) == 0

class Server:
    def __init__(self):
        self.request_queue = PriorityQueue()
        self.statistics = []

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
