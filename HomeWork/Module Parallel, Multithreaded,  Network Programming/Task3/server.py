import socket
import threading
import pickle

# Dictionary to store users {username: password}
users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

clients = []


def broadcast(message, _client_socket):
    """Send a message to all connected clients except the sender"""
    for client in clients:
        if client != _client_socket:
            try:
                client.send(pickle.dumps(message))
            except:
                clients.remove(client)


def handle_client(client_socket):
    """Handle a single client connection"""
    try:
        while True:
            message = pickle.loads(client_socket.recv(1024))
            if message:
                broadcast(message, client_socket)
    except:
        clients.remove(client_socket)
        client_socket.close()


def authenticate(client_socket):
    """Authenticate a user by username and password"""
    while True:
        credentials = pickle.loads(client_socket.recv(1024))
        username = credentials['username']
        password = credentials['password']

        if username in users and users[username] == password:
            client_socket.send(pickle.dumps({"status": "success", "message": "Authenticated!"}))
            return True
        else:
            client_socket.send(pickle.dumps({"status": "fail", "message": "Invalid username or password."}))


def start_server():
    """Start the chat server"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5555))
    server_socket.listen()

    print("Server is running...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} established.")

        if authenticate(client_socket):
            clients.append(client_socket)
            client_socket.send(pickle.dumps({"status": "success", "message": "Welcome to the chat!"}))

            thread = threading.Thread(target=handle_client, args=(client_socket,))
            thread.start()


if __name__ == "__main__":
    start_server()
