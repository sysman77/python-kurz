import socket
import threading
import pickle


def receive_messages(client_socket):
    """Receive messages from the server and print them"""
    while True:
        try:
            message = pickle.loads(client_socket.recv(1024))
            print(message)
        except:
            print("An error occurred.")
            client_socket.close()
            break


def start_client():
    """Start the chat client"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5555))

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    credentials = {'username': username, 'password': password}
    client_socket.send(pickle.dumps(credentials))

    response = pickle.loads(client_socket.recv(1024))
    if response['status'] == 'fail':
        print(response['message'])
        return

    print("Connected to the chat room!")

    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    while True:
        message = input()
        if message.lower() == "quit":
            client_socket.close()
            break

        client_socket.send(pickle.dumps(f"{username}: {message}"))


if __name__ == "__main__":
    start_client()
