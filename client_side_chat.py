# Chat Client Side
import socket

# Define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

# Create a client socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

# Send/Receive messages
while True:
    # Receive information from the server
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    # Quit if the server wants to end the connection
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding the chat... goodbye!")
        break
    else:
        # Display the server message and send a response
        print(f"Server: {message}")
        message = input("You: ")
        client_socket.send(message.encode(ENCODER))

# Close the client socket
client_socket.close()
