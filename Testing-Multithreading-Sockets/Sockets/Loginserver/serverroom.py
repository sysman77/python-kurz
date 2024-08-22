import socket
import threading
from collections import defaultdict

clients = []

credentials = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}
class Room:
    def __init__(self, name):
        self.name = name
        self.clients = []

rooms = defaultdict(Room)  # Slovník pro ukládání roomů

def broadcast(message, client_socket, room_name):
    room = rooms[room_name]
    for client in room.clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                room.clients.remove(client)


def handle_client(client_socket, username):
    while True:
        try:
            message = client_socket.recv(1024)
            # Získat název roomu z message (implementovat)
            room_name = extract_room_name(message)
            broadcast(message, client_socket, room_name)
        except:
            client_socket.close()
            # Odebrat klienta ze všech roomů (implementovat)
            remove_client_from_rooms(client_socket)
            break


def receive_connections(server_socket):
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Připojení od {client_address} bylo navázáno.")

        client_socket.send("USERNAME".encode('utf-8'))
        username = client_socket.recv(1024).decode('utf-8')

        client_socket.send("PASSWORD".encode('utf-8'))
        password = client_socket.recv(1024).decode('utf-8')

        if username in credentials and credentials[username] == password:
            clients.append(client_socket)
            print(f"Uživatelské jméno klienta je {username}")
            # Přidat klienta do defaultního roomu (nebo jiného počátečního roomu)
            add_client_to_room(client_socket, "default_room")

            thread = threading.Thread(target=handle_client, args=(client_socket, username))
            thread.start()
        else:
            client_socket.send("Neplatné uživatelské jméno nebo heslo.".encode('utf-8'))
            client_socket.close()

# Funkce pro přidání klienta do roomu
def add_client_to_room(client_socket, room_name):
    room = rooms[room_name]
    room.clients.append(client_socket)

# Funkce pro odebrání klienta ze všech roomů
def remove_client_from_rooms(client_socket):
    for room in rooms.values():
        if client_socket in room.clients:
            room.clients.remove(client_socket)

# Funkce pro vytvoření nového roomu
def create_room(room_name):
    rooms[room_name] = Room(room_name)

# Funkce pro změnu roomu klienta
def change_room(client_socket, old_room_name, new_room_name):
    # Odebrat klienta ze starého roomu
    remove_client_from_rooms(client_socket)
    # Přidat klienta do nového roomu
    add_client_to_room(client_socket, new_room_name)

# Funkce pro získání názvu roomu z message
def extract_room_name(message):
    # Implementovat logiku pro získání názvu roomu z message
    pass

# ... ostatní funkce ...
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5555))
    server_socket.listen()

    print("Server naslouchá...")
    receive_connections(server_socket)


if __name__ == "__main__":
    start_server()