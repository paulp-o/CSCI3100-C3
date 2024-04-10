import pygame, sys, requests, json
import Game

domain = '127.0.0.1:8000'

class Register:
    def __init__(self, display, gameStateManager):
        self.clock = pygame.time.Clock()
        self.loop = True
        
        self.display = display
        self.gameStateManager = gameStateManager
        self.text_font = pygame.font.Font(None,32)
        self.title_font = pygame.font.Font(None, 60) 
        
        
        
