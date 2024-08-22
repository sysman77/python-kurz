import socket
import threading

def receive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "USERNAME":
                client.send(username.encode('utf-8'))
            elif message == "PASSWORD":
                client.send(password.encode('utf-8'))
            elif message == "ROOM_SELECTION":
                # Získání seznamu místností ze serveru
                rooms = client.recv(1024).decode('utf-8')
                print("Available rooms:")
                print(rooms)
                room_choice = input("Enter the ID of the room you want to join: ")
                client.send(room_choice.encode('utf-8'))
            elif message == "OK":
                print("Successfully logged in and joined the room!")
            elif message == "FAIL":
                print("Login or room selection failed. Check your credentials.")
                client.close()
                break
            else:
                print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def send_messages(client):
    while True:
        message = input('')
        if message.lower() == 'exit!':
            client.send(f'{username} has left the chat.'.encode('utf-8'))
            client.close()
            break
        else:
            client.send(f'{username}: {message}'.encode('utf-8'))

if __name__ == "__main__":
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client,))
    send_thread.start()
