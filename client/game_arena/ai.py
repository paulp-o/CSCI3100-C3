import pygame
import random


def play_ai(ai, players, food_dots):
    randomness = 45  # Base level of randomness in AI movement
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
        mode = "aggressive"
    else:
        mode = "passive"

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
                if distance < 100:  # Too close to another body part
                    avoid_dir = ai.body[0] - segment
                    direction += avoid_dir.normalize() * (100 - distance) / \
                        100  # Weighted by proximity

    # Normalize the final direction to ensure consistent movement speed
    ai.direction = direction.normalize()
