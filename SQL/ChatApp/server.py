import socket
import threading
import sqlite3

# Inicializace databáze a nastavení
conn = sqlite3.connect('chat_app.db', check_same_thread=False)
cursor = conn.cursor()

# Inicializace socket serveru
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(5)

clients = []
usernames = {}
user_rooms = {}


def broadcast(message, _client):
    room_id = user_rooms[_client]
    for client in clients:
        if user_rooms[client] == room_id and client != _client:
            client.send(message)


def send_user_list(client, room_id):
    users_in_room = [usernames[client] for client in clients if user_rooms[client] == room_id]
    users_message = "Users in this room: " + ", ".join(users_in_room)
    client.send(users_message.encode('utf-8'))


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                broadcast(message, client)
        except:
            index = clients.index(client)
            room_id = user_rooms[client]
            clients.remove(client)
            username = usernames[client]
            del usernames[client]
            del user_rooms[client]
            client.close()
            broadcast(f'{username} has left the chat.'.encode('utf-8'), client)
            send_user_list(client, room_id)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("USERNAME".encode('utf-8'))
        username = client.recv(1024).decode('utf-8')

        cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user:
            client.send("PASSWORD".encode('utf-8'))
            password = client.recv(1024).decode('utf-8')

            cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
            user = cursor.fetchone()

            if user:
                client.send("ROOM_SELECTION".encode('utf-8'))

                cursor.execute("SELECT id, name FROM rooms")
                rooms = cursor.fetchall()
                room_list = "\n".join([f"{room[0]}: {room[1]}" for room in rooms])

                client.send(room_list.encode('utf-8'))
                room_choice = client.recv(1024).decode('utf-8')

                cursor.execute("SELECT id FROM rooms WHERE id = ?", (room_choice,))
                room = cursor.fetchone()

                if room:
                    clients.append(client)
                    usernames[client] = username
                    user_rooms[client] = room_choice
                    print(f"Username: {username} connected to room {room_choice}")
                    client.send("OK".encode('utf-8'))
                    broadcast(f"{username} joined the chat!".encode('utf-8'), client)
                    send_user_list(client, room_choice)
                    thread = threading.Thread(target=handle_client, args=(client,))
                    thread.start()
                else:
                    client.send("FAIL".encode('utf-8'))
                    client.close()
            else:
                client.send("FAIL".encode('utf-8'))
                client.close()
        else:
            client.send("FAIL".encode('utf-8'))
            client.close()


if __name__ == "__main__":
    print("Server is running...")
    receive()
