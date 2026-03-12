# ------------------------------------------------------------
# Multiplayer Game Engine Server
# Handles player connections and broadcasts game updates
# ------------------------------------------------------------

import socket
import threading

# Store connected players
players = []

# Function to handle each player
def handle_player(conn, addr):
    print(f"Player connected from {addr}")

    while True:
        try:
            # Receive message from player
            message = conn.recv(1024).decode()

            if not message:
                break

            print(f"Player {addr} says: {message}")

            # Send message to all other players
            broadcast(message, conn)

        except:
            break

    print(f"Player {addr} disconnected")
    players.remove(conn)
    conn.close()


# Broadcast messages to all players
def broadcast(message, sender):
    for player in players:
        if player != sender:
            try:
                player.send(message.encode())
            except:
                pass


# Main server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("127.0.0.1", 5555))
    server.listen()

    print("Game Server Started...")
    print("Waiting for players...")

    while True:
        conn, addr = server.accept()

        players.append(conn)

        thread = threading.Thread(target=handle_player, args=(conn, addr))
        thread.start()


start_server()