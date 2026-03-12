# ------------------------------------------------------------
# Multiplayer Game Engine Client
# Represents a player connecting to the game
# ------------------------------------------------------------

import socket
import threading

# Connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))


# Receive updates from server
def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print("\nGame Update:", message)
        except:
            print("Connection closed")
            break


# Send player actions
def send():
    while True:
        action = input("Enter action (move/shoot/chat): ")
        client.send(action.encode())


# Run receiving thread
thread = threading.Thread(target=receive)
thread.start()

# Start sending actions
send()