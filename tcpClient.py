import socket


def start_client():
    # Step 1: Create a TCP client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Step 2: Connect to the server
    host = socket.gethostbyname(socket.gethostname())  # Dynamically fetch the server IP
    port = 12345  # Same port as the server
    client_socket.connect((host, port))
    print(f"Connected to the server at {host}:{port}")

    # Step 3: Receive messages from the server
    message = client_socket.recv(1024).decode('utf-8')  # Buffer size of 1024 bytes
    print("Message from server:", message)

    # Step 5: Close the client socket
    client_socket.close()
    print("Client connection closed.")


if __name__ == "__main__":
    start_client()
