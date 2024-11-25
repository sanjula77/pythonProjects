import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 12345))
print("Connected to the TCP server.")

# Send data
client_socket.send("Hello from TCP client!".encode())

# Receive a response
response = client_socket.recv(1024).decode()
print(f"Server response: {response}")

# Close the connection
client_socket.close()
