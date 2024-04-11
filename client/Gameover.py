import pygame
import Game
import Button


class Gameover:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        title_font = pygame.font.SysFont("comicsansms", 70)
        text_font = pygame.font.SysFont("comicsansms", 35)

         # Icon / Image
        self.back_icon = pygame.image.load("Assets/Settings/return.png").convert_alpha()
        self.back_button = Button.Button(Game.SCREEN_WIDTH - 60, 5, self.back_icon, 0.5)
        self.back_button.action = lambda: self.gameStateManager.set_state('main')
        
        # title
        self.rect_title = pygame.Rect((Game.SCREEN_WIDTH)/2-100, 100, 200, 40)
        self.text_title = title_font.render('Game Over', False, 'white')
        self.text_title_rect = self.text_title.get_rect()
        self.text_title_rect.center = self.rect_title.center
        
        

    def run(self):
        Game.screen.fill((200, 200, 180))  # giving background color
        
        self.back_button.draw()
        
        Game.screen.blit(self.text_title, self.text_title_rect)
        
        
        
