# Chat Server Side
import socket

# Define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

# Create a server socket, bind it to a IP/port, and listen
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

print("Server is running...\n")

# Accept any incoming connection and notify the client
client_socket, client_address = server_socket.accept()
client_socket.send("You are connected to the server...\n".encode(ENCODER))

# Send/receive messages
while True:
    # Receive information from the client
    message = client_socket.recv(BYTESIZE).decode(ENCODER)

    if message == "quit":
        # Quit if the client wants to disconnect
        client_socket.send("quit".encode(ENCODER))
        print("\nEnding the chat... goodbye!")
        break
    else:
        # Display the received message and send a response
        print(f"Client: {message}")
        response = input("Message: ")
        client_socket.send(response.encode(ENCODER))

# Close the socket
server_socket.close()
