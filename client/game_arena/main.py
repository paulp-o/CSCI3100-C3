import pygame
import sys
import math
import random
import threading
import socket
import time
from ai import play_ai

# Initialize Pygame
pygame.init()

# Networking setup
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)

# other players
# dictionary of players, key is their id, value is their info (snake_body(list))
other_players = {}


def server_communication():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server address and port
    server_address = ('localhost', 12345)

    # Connect to the server
    s.connect(server_address)

    while True:
        # Receive data from the server
        data = s.recv(1024)
        # TODO: Process the received data
        # print(f"Received data from server: {data.decode()}")


# Create a new thread that runs the server communication function
t = threading.Thread(target=server_communication)

# Start the new thread
# t.start()

# Set the dimensions of the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
input_method = 'mouse'  # or keyboard

# Define arena bounds
arena_width = 1000
arena_height = 1000
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
background = pygame.image.load('game_arena/background_image.jpg').convert()
background_rect = background.get_rect()

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
ORANGE = (255, 165, 0)


class Snake:
    def __init__(self, position, length, id):
        # start with length segments.
        self.id = id
        self.body = [position] * length
        self.length = length
        self.direction = pygame.math.Vector2(1, 0)
        self.speed = 3
        self.score = 100
        self.turn_speed = 5
        for i in range(1, length):
            self.body[i] = self.body[i-1] - self.direction
            # make the snake longer
            self.grow()

    def update(self):
        self.check_boundary_collision(arena_rect)
        self.check_food_collisions(food_dots)
        self.move()

    def move(self):
        new_body = [self.body[0] + self.direction * self.speed]
        new_body.extend(self.body[:-1])
        self.body = new_body

    def draw(self, window, camera_offset, color=GREEN):
        for segment in self.body:
            adjusted_pos = (segment.x - camera_offset.x,
                            segment.y - camera_offset.y)
            pygame.draw.circle(window, color, adjusted_pos, snake_dot_size)

    def grow(self):
        # Add a new segment to the snake
        self.score += 10
        self.body.append(self.body[-1])

    def rotate_vector(vector, angle):
        """Rotate a vector by a given angle."""
        rad_angle = math.radians(angle)
        cos_theta = math.cos(rad_angle)
        sin_theta = math.sin(rad_angle)
        rotated_x = vector.x * cos_theta - vector.y * sin_theta
        rotated_y = vector.x * sin_theta + vector.y * cos_theta
        return pygame.math.Vector2(rotated_x, rotated_y)

    def check_boundary_collision(self, boundary_rect):
        # This checks the actual game world position, not affected by camera
        return not boundary_rect.collidepoint(self.body[0].x, self.body[0].y)

    def check_food_collisions(snake, food_dots):
        for food in food_dots[:]:  # Copy to avoid modification during iteration
            if snake.body[0].distance_to(food) < snake_dot_size:
                snake.grow()
                food_dots.remove(food)
                # Add new food dot to replace the eaten one
                food_dots.append(get_random_dot_position(
                    snake.body, window_width, window_height))


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
        snake_direction = pygame.math.Vector2(
            math.cos(angle), math.sin(angle))
    else:
        # Continue in the same direction if the mouse is too close to the center
        snake_direction = snake_head - \
            pygame.math.Vector2(center_x, center_y)
        if snake_direction.length() > 0:
            snake_direction = snake_direction.normalize()

    return snake_direction


# define food number
food_num = 30

# make a player snake.
player = Snake(pygame.math.Vector2(400, 400), 5, 'player')

# make an AI snake.
ai = Snake(pygame.math.Vector2(600, 600), 5, 'ai')
ai2 = Snake(pygame.math.Vector2(200, 200), 5, 'ai2')
ai3 = Snake(pygame.math.Vector2(800, 800), 5, 'ai3')
ai4 = Snake(pygame.math.Vector2(100, 100), 5, 'ai4')


# Initialize level progression
level_duration = 60  # Seconds
level = 1
start_time = pygame.time.get_ticks()

# Define the dot properties
dot_pos = pygame.math.Vector2(random.randrange(
    1, window_width), random.randrange(1, window_height))
snake_dot_size = 14
food_dot_size = 5

# Draw the dot


def draw_dot(window, dot_pos):
    pygame.draw.circle(window, RED, (int(dot_pos.x),
                                     int(dot_pos.y)), food_dot_size)


def draw_dots(window, food_dots, offset):
    for dot_pos in food_dots:
        dot_position = dot_pos - offset
        pygame.draw.circle(window, RED, (int(dot_position.x),
                                         int(dot_position.y)), food_dot_size)


def regenerate_food(dot_pos, snake_body, window_width, window_height, food_dots):
    food_dots.remove(dot_pos)
    food_dots.append(get_random_dot_position(
        snake_body, window_width, window_height))


def get_random_dot_position(snake_body, window_width, window_height):
    while True:
        pos = pygame.math.Vector2(random.randint(food_dot_size, window_width - food_dot_size),
                                  random.randint(food_dot_size, window_height - food_dot_size))
        if not any(pygame.math.Vector2(segment).distance_to(pos) < food_dot_size for segment in snake_body):
            return pos


def check_level_progression(start_time, level_duration, level, snake_speed):
    if (pygame.time.get_ticks() - start_time) / 1000 > level_duration:
        level += 1
        # Increase speed, with a max limit for balance
        return level, pygame.time.get_ticks(), min(10, snake_speed + 1)
    return level, start_time, snake_speed


def get_camera_offset(snake_head, window_width, window_height):
    return snake_head - pygame.math.Vector2(window_width / 2, window_height / 2)

# Update drawing functions to offset positions based on camera


def draw_background(window, offset, viewport):
    # Calculate the new top-left position of the background
    new_bg_x = -offset.x % background.get_width()
    new_bg_y = -offset.y % background.get_height()

    # Blit the background at the new position
    window.blit(background, (new_bg_x, new_bg_y))
    window.blit(background, (new_bg_x - background.get_width(), new_bg_y))
    window.blit(background, (new_bg_x, new_bg_y - background.get_height()))
    window.blit(background, (new_bg_x - background.get_width(),
                new_bg_y - background.get_height()))


def draw_boundary(window, boundary_rect, offset):
    # Apply the offset to the boundary rect for drawing
    offset_boundary_rect = boundary_rect.move(-offset.x, -offset.y)
    # 2 is the thickness of the boundary
    pygame.draw.rect(window, WHITE, offset_boundary_rect, 2)
    # Adjust the position of the boundary based on the viewport
    if viewport.colliderect(offset_boundary_rect):
        adjusted_rect = offset_boundary_rect.clip(viewport)
        adjusted_rect.move_ip(-viewport.x, -viewport.y)
        # pygame.draw.rect(window, WHITE, adjusted_rect, 2)


# Define foods
# Initialize multiple food dots
# food_dots = [get_random_dot_position(
#     # Start with 10 dots
#     snake_body, window_width, window_height) for _ in range(10)]
food_dots = [get_random_dot_position(
    # Start with 10 dots
    player.body, window_width, window_height) for _ in range(food_num)]

# Main game loop
running = True

players = [ai, ai2, ai3, ai4, player]


# store each players' deaths
for player in players:
    player.deaths = 0

# store each players' kills
for player in players:
    player.kills = 0

start_time = time.time()
loop = 0
while running:
    # print time passed every 100 loops
    loop += 1
    if loop % 100 == 0:
        # print(f'time passed: {time.time() - start_time}')
        pass

    # Get camera offset
    # camera_offset = get_camera_offset(
    #     snake_body[0], window_width, window_height)
    camera_offset = get_camera_offset(
        player.body[0], window_width, window_height)
    window.fill((0, 0, 0))  # Optional based on background coverage
    draw_background(window, camera_offset, viewport)
    draw_boundary(window, arena_rect, camera_offset)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pause the game and show the game over screen
            running = False
            break

    # # Handle keys
    # if input_method == 'keyboard':
    #     snake_direction = handle_keys(
    #         snake_direction, turn_speed, camera_offset, snake_body[0])
    # elif input_method == 'mouse':
    #     snake_direction = handle_mouse(
    #         snake_direction, turn_speed, camera_offset, snake_body[0])

    # Handle keys for only player
    # In the game loop, right before updating movements
    if input_method == 'mouse':
        player.direction = handle_mouse(
            player.direction, player.turn_speed, camera_offset, player.body[0])
    elif input_method == 'keyboard':
        player.direction = handle_keys(
            player.direction, player.turn_speed, camera_offset, player.body[0])
    player.update()  # Update player based on the new direction

    play_ai(ai, players, food_dots)
    play_ai(ai2, players, food_dots)
    play_ai(ai3, players, food_dots)
    play_ai(ai4, players, food_dots)

    ai.update()
    ai2.update()
    ai3.update()
    ai4.update()

    # Check for collisions
    # if check_collision_with_dot(player.body[0], dot_pos):
    #     # Or more, depending on your growth logic
    #     player.grow()
    #     dot_pos = get_random_dot_position(
    #         player.body, window_width, window_height)
    # Check for collisions for all players
    for player in players:
        if player.body[0].distance_to(dot_pos) < snake_dot_size:
            player.grow()
            dot_pos = get_random_dot_position(
                player.body, window_width, window_height)

    # Draw everything
    draw_dots(window, food_dots, camera_offset)

    # check if one of the player's head collides with other player's body. If so, that player loses.
    for player in players:
        for other_player in players:
            if player == other_player:
                continue
            for segment in other_player.body[1:]:
                if player.body[0].distance_to(segment) < snake_dot_size:
                    # print(f'{player.id} loses!')
                    # resume the game and respawn the dead player, in a place where there is no other player
                    player.body[0] = get_random_dot_position(
                        player.body, window_width, window_height)
                    player.body = [player.body[0]] * player.length
                    # increase the deaths of the dead player
                    player.deaths += 1
                    # decrease the score of the dead player
                    player.score *= 0.9
                    # increase the kills of the killer
                    other_player.kills += 1
                    # increase the score of the killer
                    other_player.score *= 1.03

    # check if one of the player's head collides with the boundary. If so, that player loses.
    for player in players:
        if player.check_boundary_collision(arena_rect):
            # print(f'{player.id} loses!')
            # resume the game and respawn the dead player, in a place where there is no other player
            player.body[0] = get_random_dot_position(
                player.body, window_width, window_height)
            player.body = [player.body[0]] * player.length
            # increase the deaths of the dead player
            player.deaths += 1
            # decrease the score of the dead player
            player.score *= 0.9

    # if someone reaches 10 deaths, the game ends
    for player in players:
        if player.deaths >= 10:
            # print(f'{player.id} has reached 10 deaths. Game over!')
            running = False

    # draw all players, with all different colors
    colors = [GREEN, BLUE, YELLOW, PURPLE, ORANGE]
    for i, player in enumerate(players):
        player.draw(window, camera_offset, colors[i])

    # Check level progression
    level, start_time, snake_speed = check_level_progression(
        start_time, level_duration, level, player.speed)

    # show each player's deaths, kills and score in the bottom left corner
    for i, player in enumerate(players):
        font = pygame.font.Font(None, 25)
        text = font.render(
            f'{player.id}: deaths: {player.deaths}, kills: {player.kills}, score: {round(player.score)}', True, (255, 255, 255))
        textRect = text.get_rect()
        textRect.topleft = (10, 10 + i * 20)
        window.blit(text, textRect)
    # Refresh the display
    pygame.display.flip()

    # Frame Per Second /Refresh Rate
    pygame.time.Clock().tick(60)

# print out the game result including each player's deaths, kills and score in dictionary format
result = {}
for player in players:
    result[player.id] = {'deaths': player.deaths,
                         'kills': player.kills, 'score': player.score}
print(result)
# Quit the game
pygame.quit()
sys.exit()
