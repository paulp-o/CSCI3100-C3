import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

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


def handle_keys(snake_direction, turn_speed):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_direction.rotate_ip(-turn_speed)
    if keys[pygame.K_RIGHT]:
        snake_direction.rotate_ip(turn_speed)
    return snake_direction


def get_random_dot_position(snake_body, window_width, window_height):
    while True:
        pos = pygame.math.Vector2(random.randint(dot_size, window_width - dot_size),
                                  random.randint(dot_size, window_height - dot_size))
        if not any(segment.distance_to(pos) < dot_size for segment in snake_body):
            return pos


def check_collision_with_dot(snake_head, dot_pos):
    return snake_head.distance_to(dot_pos) < dot_size


def check_collision_with_self(snake_body):
    return any(segment.distance_to(snake_body[0]) < dot_size for segment in snake_body[1:])


def check_level_progression(start_time, level_duration, level, snake_speed):
    if (pygame.time.get_ticks() - start_time) / 1000 > level_duration:
        level += 1
        # Increase speed, with a max limit for balance
        return level, pygame.time.get_ticks(), min(10, snake_speed + 1)
    return level, start_time, snake_speed


def get_camera_offset(snake_head, window_width, window_height):
    return snake_head - pygame.math.Vector2(window_width / 2, window_height / 2)

# Update drawing functions to offset positions based on camera


def draw_snake(window, snake_body, offset):
    for segment in snake_body:
        segment_pos = segment - offset
        pygame.draw.circle(
            window, GREEN, (int(segment_pos.x), int(segment_pos.y)), 10)


def draw_dot(window, dot_pos, offset):
    dot_position = dot_pos - offset
    pygame.draw.circle(window, RED, (int(dot_position.x),
                       int(dot_position.y)), dot_size)


def draw_background(window, offset):
    # Calculate the new top-left position of the background
    new_bg_x = -offset.x % background.get_width()
    new_bg_y = -offset.y % background.get_height()

    # Blit the background at the new position
    window.blit(background, (new_bg_x, new_bg_y))
    window.blit(background, (new_bg_x - background.get_width(), new_bg_y))
    window.blit(background, (new_bg_x, new_bg_y - background.get_height()))
    window.blit(background, (new_bg_x - background.get_width(),
                new_bg_y - background.get_height()))


# Define foods
# Initialize multiple food dots
food_dots = [get_random_dot_position(
    # Start with 10 dots
    snake_body, window_width, window_height) for _ in range(10)]

# Main game loop
running = True
while running:
    # Get camera offset
    camera_offset = get_camera_offset(
        snake_body[0], window_width, window_height)
    window.fill((0, 0, 0))  # Optional based on background coverage
    draw_background(window, camera_offset)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle keys
    snake_direction = handle_keys(snake_direction, turn_speed)

    # Move the snake
    snake_body = move_snake(snake_body, snake_direction, snake_speed)

    # Check for collisions
    if check_collision_with_dot(snake_body[0], dot_pos):
        # Or more, depending on your growth logic
        grow_snake(snake_body, additional_segments=1)
        dot_pos = get_random_dot_position(
            snake_body, window_width, window_height)

    # if check_collision_with_self(snake_body):
    #     print("Game Over")  # Placeholder for game over logic
    #     running = False

    # Update the collision check in the game loop
    for dot_pos in food_dots[:]:  # Copy the list to avoid modification issues
        if check_collision_with_dot(snake_body[0], dot_pos):
            grow_snake(snake_body, additional_segments=1)
            regenerate_food(dot_pos, snake_body, window_width,
                            window_height, food_dots)

    # Draw everything
    draw_snake(window, snake_body, camera_offset)
    draw_dots(window, food_dots, camera_offset)

    # Check level progression
    level, start_time, snake_speed = check_level_progression(
        start_time, level_duration, level, snake_speed)

    # Refresh the display
    pygame.display.flip()

    # Frame Per Second /Refresh Rate
    pygame.time.Clock().tick(60)

    # print snake position
    print(snake_body[0])

# Quit the game
pygame.quit()
sys.exit()
