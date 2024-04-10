import pygame, sys, requests, json
import Game

class StartGame:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        title_font = pygame.font.Font(None, 60)
        text_font = pygame.font.Font(None, 32)
        