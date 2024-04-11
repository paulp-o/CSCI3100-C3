import pygame
import random
import math


MAX_ANGLE_CHANGE = 30  # Maximum angle change in degrees per update


def angle_between_vectors(v1, v2):
    """Calculate the angle in degrees between two vectors."""
    angle_rad = math.atan2(v2.y, v2.x) - math.atan2(v1.y, v1.x)
    angle_deg = math.degrees(angle_rad)
    return angle_deg % 360


def play_ai(ai, players, food_dots):
    randomness = 25  # Base level of randomness in AI movement
    aggression_threshold = 250  # Distance within which the AI considers being aggressive

    # Determine AI's current length and the nearest player
    ai_length = len(ai.body)
    nearest_player = min(players, key=lambda x: ai.body[0].distance_to(
        x.body[0]) if x != ai else float('inf'))
    nearest_player_distance = ai.body[0].distance_to(nearest_player.body[0])
    average_length_other_snakes = sum(
        len(player.body) for player in players if player != ai) / (len(players) - 1)

    # Decide on aggression based on AI's length relative to others and proximity to the nearest player
    if ai_length > average_length_other_snakes and nearest_player_distance < aggression_threshold:
        # 10% chance to be aggressive if conditions are met
        mode = "aggressive" if random.random() < 0.1 else "passive"
    else:
        # 1% chance to be aggressive if conditions are not met
        mode = "aggressive" if random.random() < 0.01 else "passive"

    # Find the nearest food
    nearest_food = min(food_dots, key=lambda x: ai.body[0].distance_to(x))

    # Determine target based on mode
    if mode == "aggressive":
        target = nearest_player.body[0]
    else:  # Default to nearest food if passive or no clear aggressive target
        target = nearest_food

    # Calculate base direction towards target
    direction = target - ai.body[0] + pygame.math.Vector2(
        random.uniform(-randomness, randomness), random.uniform(-randomness, randomness))

    # Avoidance behavior - steer away from other snakes
    for player in players:
        if player != ai:  # Don't consider self
            # Skip the head for less jittery avoidance
            for segment in player.body[1:]:
                distance = ai.body[0].distance_to(segment)
                if distance < 150:  # Too close to another body part
                    avoid_dir = ai.body[0] - segment
                    direction += avoid_dir.normalize() * (100 - distance) / \
                        1000  # Weighted by proximity

    # Limit the angle change to the maximum allowed
    current_direction_angle = math.atan2(ai.direction.y, ai.direction.x)
    new_direction_angle = math.atan2(direction.y, direction.x)
    angle_change = math.degrees(
        new_direction_angle - current_direction_angle) % 360
    angle_change = (angle_change + 180) % 360 - 180  # Normalize to [-180, 180]

    # Apply maximum angle change
    if angle_change > MAX_ANGLE_CHANGE:
        angle_change = MAX_ANGLE_CHANGE
    elif angle_change < -MAX_ANGLE_CHANGE:
        angle_change = -MAX_ANGLE_CHANGE

    # Calculate new limited direction
    limited_angle_rad = current_direction_angle + math.radians(angle_change)
    limited_direction = pygame.math.Vector2(
        math.cos(limited_angle_rad), math.sin(limited_angle_rad))

    ai.direction = limited_direction.normalize()
