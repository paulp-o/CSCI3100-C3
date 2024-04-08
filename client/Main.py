import pygame
import Game
import Button

startbutton = pygame.image.load('img/start_btn.png')
tosettingbutton = pygame.image.load('img/setting_btn.png')

class Main:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.background = pygame.image.load('img/background.jpg')
        title_font = pygame.font.Font(None, 120)
        text_font = pygame.font.Font(None, 35)
        self.text_title = title_font.render('Snake.io', False, 'white')
        self.start_button = Button.Button(250, 300, startbutton, 0.8, self.go_to_play)
        self.tosetting_button = Button.Button(120, 450, tosettingbutton, 0.1, self.to_setting)

    def run(self):
        Game.screen.blit(self.background, (0, 0))
        Game.screen.blit(self.text_title, (200, 90))
        if self.start_button.back():
            self.start_button.action()

        if self.tosetting_button.back():
            self.tosetting_button.action()

    def go_to_play(self):
        self.gameStateManager.set_state('play')

    def to_setting(self):
        self.gameStateManager.set_state('setting')