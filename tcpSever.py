import socket


def start_server():
    # Step 2: Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Step 3: Obtain host information
    host = socket.gethostbyname(socket.gethostname())  # Dynamically fetch the IP
    port = 12345  # Specify a port number

    # Step 4: Bind the socket
    server_socket.bind((host, port))
    print(f"Server started on {host}:{port}")

    # Step 5: Listen for incoming connections
    server_socket.listen(5)  # Allows a maximum of 5 queued connections
    print("Waiting for a connection...")

    while True:
        # Step 6: Accept connections in a loop
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        # Step 7: Send a message to the client
        message = "You are connected to the server!"
        client_socket.send(message.encode('utf-8'))

        # Close the client socket
        client_socket.close()
        print("Client connection closed. Waiting for a new connection...")

        # Break the loop if needed (uncomment to make it a one-time server)
        # break

    # Step 8: Close the server
    server_socket.close()
    print("Server closed.")


if __name__ == "__main__":
    start_server()
