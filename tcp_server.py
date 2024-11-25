import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to an address and port
server_socket.bind(('localhost', 12345))

# Start listening for connections
server_socket.listen(1)
print("TCP Server listening on port 12345...")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Receive data from the client
data = client_socket.recv(1024).decode()
print(f"Received: {data}")

# Send a response
client_socket.send("Hello from TCP server!".encode())

# Close the connection
client_socket.close()
server_socket.close()
