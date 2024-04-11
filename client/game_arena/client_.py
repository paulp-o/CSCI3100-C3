import pygame
import socket
import sys
import pickle
import threading

# Initialize Pygame
pygame.init()

# Client setup
SERVER_IP = '127.0.0.1'
SERVER_PORT = 65432
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (SERVER_IP, SERVER_PORT)

# Window setup
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake.io - Client')

# Player setup
player_pos = {'x': window_width // 2, 'y': window_height // 2}


def send_position_to_server():
    """
    Sends the current player position to the server.
    """
    try:
        # Serialize and send player position
        message = pickle.dumps({'position': player_pos})
        client_socket.sendto(message, server_address)
    except Exception as e:
        print(f"Error sending position to server: {e}")


def receive_game_state():
    """
    Listens for incoming game state updates from the server.
    """
    global player_pos
    while True:
        try:
            data, _ = client_socket.recvfrom(4096)
            game_state = pickle.loads(data)
            # Update game state based on received data
        except Exception as e:
            print(f"Error receiving game state: {e}")
            break


# Start listening for game state updates in a separate thread
thread = threading.Thread(target=receive_game_state, args=())
thread.daemon = True
thread.start()

game_state = {

}

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # retrieve game state from server
    game_state = client_socket.recv(4096).decode()

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos['x'] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos['x'] += 5
    if keys[pygame.K_UP]:
        player_pos['y'] -= 5
    if keys[pygame.K_DOWN]:
        player_pos['y'] += 5

    send_position_to_server()

    window.fill((0, 0, 0))  # Clear the window

    # Render game state
    for player in game_state.get('players', {}).values():
        pygame.draw.circle(window, (0, 255, 0), (player['x'], player['y']), 10)

    # # Render own player
    # pygame.draw.circle(window, (255, 0, 0),
    #                    (player_pos['x'], player_pos['y']), 10)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
client_socket.close()
sys.exit()
