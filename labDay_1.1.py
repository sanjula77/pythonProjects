import socket

def check_port(host, port):
    try:
        socket.create_connection((host, port), timeout=5)
        print(f"Port {port} on {host} is Open")
    except:
        print(f"Port {port} on {host} is Closed")

check_port("www.google.com", 80)  # check http
check_port("www.google.com", 443)  # check https
check_port("www.google.com", 20)  # check FTP