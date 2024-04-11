import socket
import time

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 12345)

# Bind the socket to the address and port
s.bind(server_address)

# Start listening for incoming connections
s.listen(1)

print("Server started! Waiting for connections...")

while True:
    # Accept a connection
    client_socket, client_address = s.accept()
    print("Client connected: ", client_address)

    count = 0
    while True:
        count += 1
        # Send data to the client
        data = "Server data, count: {}".format(count)
        client_socket.send(data.encode())
        time.sleep(1/24)  # Sleep for a bit to simulate a real server
