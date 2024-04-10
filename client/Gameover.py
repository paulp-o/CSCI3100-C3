import pygame
import Game


class Gameover:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.score_text_font = pygame.font.SysFont("comicsansms", 70)

        self.score_text = self.score_text_font.render('Game Over', False, 'white')
        self.score_text_rect = self.score_text.get_rect(
        # to ensure center of text at top
        center=(Game.SCREEN_WIDTH/2, 50))

    def run(self):
        Game.screen.fill((200, 200, 180))  # giving background color
        Game.screen.blit(self.score_text, self.score_text_rect)
