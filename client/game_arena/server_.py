import socket
import threading
import pygame
import sys
import pickle
import random

# Basic game setup
pygame.init()

# Set the dimensions of the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
input_method = 'mouse'  # or keyboard

# Define arena bounds
arena_width = 2000
arena_height = 2000
arena_rect = pygame.Rect(0, 0, arena_width, arena_height)

# Define viewport
# Initial viewport is the same size as the window, centered in the game arena
viewport = pygame.Rect(0, 0, window_width, window_height)
# Center the viewport in the game arena
viewport.center = (arena_width / 2, arena_height / 2)


# Set the title of the window
pygame.display.set_caption('Snake.io')

# Load resources
# Load your background image
background = pygame.image.load('background_image.jpg').convert()
background_rect = background.get_rect()


# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define snake properties
snake_pos = pygame.math.Vector2(
    window_width//2, window_height//2)  # Starting in the middle
snake_body = [pygame.math.Vector2(snake_pos.x, snake_pos.y)
              for _ in range(5)]  # A list of vectors
snake_direction = pygame.math.Vector2(1, 0)  # Moving right initially
snake_speed = 3
turn_speed = 5  # Degrees per frame


# Initialize level progression
level_duration = 60  # Seconds
level = 1
start_time = pygame.time.get_ticks()


# Define the dot properties
dot_pos = pygame.math.Vector2(random.randrange(
    1, window_width), random.randrange(1, window_height))
dot_size = 10


# Networking setup
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
BUFFER_SIZE = 4096  # Standard buffer size for UDP packets

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
print(f"Server listening on {HOST}:{PORT}")

clients = []  # Keep track of connected clients

game_state = {
    'players': {}
}


# Draw the dot


def rotate_vector(vector, angle):
    """Rotate a vector by a given angle."""
    rad_angle = math.radians(angle)
    cos_theta = math.cos(rad_angle)
    sin_theta = math.sin(rad_angle)
    rotated_x = vector.x * cos_theta - vector.y * sin_theta
    rotated_y = vector.x * sin_theta + vector.y * cos_theta
    return pygame.math.Vector2(rotated_x, rotated_y)


def move_snake(snake_body, snake_direction, snake_speed):
    # Move the body
    new_body = []
    for i, segment in enumerate(snake_body):
        if i == 0:
            new_head = segment + snake_direction * snake_speed
            new_body.append(new_head)
        else:
            new_body.append(snake_body[i-1])
    return new_body


def grow_snake(snake_body, additional_segments):
    for _ in range(additional_segments):
        snake_body.append(snake_body[-1])


def draw_dot(window, dot_pos):
    pygame.draw.circle(window, RED, (int(dot_pos.x), int(dot_pos.y)), dot_size)


def draw_dots(window, food_dots, offset):
    for dot_pos in food_dots:
        dot_position = dot_pos - offset
        pygame.draw.circle(window, RED, (int(dot_position.x),
                           int(dot_position.y)), dot_size)


def regenerate_food(dot_pos, snake_body, window_width, window_height, food_dots):
    food_dots.remove(dot_pos)
    food_dots.append(get_random_dot_position(
        snake_body, window_width, window_height))


def handle_keys(snake_direction, turn_speed, camera_offset, snake_head):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_direction.rotate_ip(-turn_speed)
    if keys[pygame.K_RIGHT]:
        snake_direction.rotate_ip(turn_speed)
    return snake_direction


def handle_mouse(snake_direction, turn_speed, camera_offset, snake_head):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    center_x, center_y = window_width / 2, window_height / 2
    dx, dy = mouse_x - center_x, mouse_y - center_y

    # Calculate the angle only if the mouse is away from the center to prevent stuttering
    if dx**2 + dy**2 > 100:  # Using 100 pixels as a threshold for sensitivity
        angle = math.atan2(dy, dx)
        snake_direction = pygame.math.Vector2(math.cos(angle), math.sin(angle))
    else:
        # Continue in the same direction if the mouse is too close to the center
        snake_direction = snake_head - pygame.math.Vector2(center_x, center_y)
        if snake_direction.length() > 0:
            snake_direction = snake_direction.normalize()

    return snake_direction


def get_random_dot_position(snake_body, window_width, window_height):
    while True:
        pos = pygame.math.Vector2(random.randint(dot_size, window_width - dot_size),
                                  random.randint(dot_size, window_height - dot_size))
        if not any(segment.distance_to(pos) < dot_size for segment in snake_body):
            return pos


def check_collision_with_dot(snake_head, dot_pos):
    return snake_head.distance_to(dot_pos) < dot_size*2


def check_collision_with_self(snake_body):
    return any(segment.distance_to(snake_body[0]) < dot_size for segment in snake_body[1:])


def check_boundary_collision(snake_head, boundary_rect):
    # This checks the actual game world position, not affected by camera
    # return not boundary_rect.contains(snake_head.get_rect(10))
    return not boundary_rect.collidepoint(snake_head.x, snake_head.y)


def check_level_progression(start_time, level_duration, level, snake_speed):
    if (pygame.time.get_ticks() - start_time) / 1000 > level_duration:
        level += 1
        # Increase speed, with a max limit for balance
        return level, pygame.time.get_ticks(), min(10, snake_speed + 1)
    return level, start_time, snake_speed


def get_camera_offset(snake_head, window_width, window_height):
    return snake_head - pygame.math.Vector2(window_width / 2, window_height / 2)

# Update drawing functions to offset positions based on camera


def draw_snake(window, snake_body, viewport, camera_offset):
    for segment in snake_body:
        # Adjust segment positions based on the camera_offset for drawing
        adjusted_pos = (segment.x - camera_offset.x,
                        segment.y - camera_offset.y)
        pygame.draw.circle(window, GREEN, adjusted_pos, dot_size)

# Similarly adjust drawing functions for food dots and the boundary


def draw_dot(window, dot_pos, viewport):
    if viewport.collidepoint(dot_pos.x, dot_pos.y):
        adjusted_pos = (dot_pos.x - viewport.x, dot_pos.y - viewport.y)
        pygame.draw.circle(window, RED, adjusted_pos, dot_size)


def listen_for_clients():
    while True:
        data, addr = server_socket.recvfrom(BUFFER_SIZE)
        if addr not in clients:
            clients.append(addr)
            game_state['players'][addr] = {
                'x': 400, 'y': 300}  # Initial player position
            print(f"New client connected: {addr}")

        received_data = pickle.loads(data)
        if 'position' in received_data:
            game_state['players'][addr] = received_data['position']

        broadcast_game_state()


# Define foods
# Initialize multiple food dots
food_dots = [get_random_dot_position(
    # Start with 10 dots
    snake_body, window_width, window_height) for _ in range(10)]


def broadcast_game_state():
    for client in clients:
        server_socket.sendto(pickle.dumps(game_state), client)


# Start listening for clients in a new thread
thread = threading.Thread(target=listen_for_clients)
thread.start()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))  # Clear screen
    # Render game state
    for player in game_state['players'].values():
        pygame.draw.circle(window, (0, 255, 0), (player['x'], player['y']), 10)

    # send game state to clients
    broadcast_game_state()
    pygame.display.flip()
    pygame.time.wait(10)

# Clean up
pygame.quit()
server_socket.close()
sys.exit()
