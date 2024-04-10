import pygame
import Game
import Button

settingblock_blue = pygame.transform.scale(pygame.image.load('Assets/Settings/settingblock_blue.png'), (700, 150))
settingblock_white = pygame.transform.scale(pygame.image.load('Assets/Settings/settingblock_white.png'), (700, 150))
settingbutton_blue = pygame.transform.scale(pygame.image.load('Assets/Settings/settingbutton_blue.png'), (320, 60))
settingbutton_white = pygame.transform.scale(pygame.image.load('Assets/Settings/settingbutton_white.png'), (320, 60))
returnbutton = pygame.transform.scale(pygame.image.load('Assets/Settings/return.png'), (50, 50))

class Settings:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        title_font = pygame.font.Font(None, 50)
        text_font = pygame.font.Font(None, 35)

        self.background = pygame.image.load('Assets/Main Menu/background.jpg')
        self.text_setting = title_font.render('Setting', False, 'white')

        self.text_Audio = text_font.render('Audio', False, 'white')
        self.text_Music = text_font.render('Music', False, 'white')
        self.text_SFX = text_font.render('SFX', False, 'white')

        self.text_GameControl = text_font.render('Game Control', False, '#4d70d1')
        self.text_Mouse = text_font.render('Mouse', False, '#4d70d1')
        self.text_Keyboard = text_font.render('Keyboard', False, '#4d70d1')

        self.text_Language = text_font.render('Language', False, 'white')
        self.text_Chinese = text_font.render('Chinese', False, 'white')
        self.text_English = text_font.render('English', False, 'white')

        self.return_button = Button.Button(675, 30, returnbutton, 1, self.return_to_main)

    def run(self):
        Game.screen.blit(self.background, (0, 0))
        Game.screen.blit(self.text_setting, (330, 30))
        Game.screen.blit(settingblock_white, (30, 50))
        Game.screen.blit(settingblock_blue, (30, 220))
        Game.screen.blit(settingblock_white, (30, 390))
        Game.screen.blit(settingbutton_blue, (50, 125))
        Game.screen.blit(settingbutton_blue, (385, 125))
        Game.screen.blit(settingbutton_white, (50, 295))
        Game.screen.blit(settingbutton_white, (385, 295))
        Game.screen.blit(settingbutton_blue, (50, 465))
        Game.screen.blit(settingbutton_blue, (385, 465))

        Game.screen.blit(self.text_Audio, (115, 75))
        Game.screen.blit(self.text_Music, (175, 145))
        Game.screen.blit(self.text_SFX, (525, 145))

        Game.screen.blit(self.text_GameControl, (70, 240))
        Game.screen.blit(self.text_Mouse, (170, 310))
        Game.screen.blit(self.text_Keyboard, (510, 310))

        Game.screen.blit(self.text_Language, (80, 410))
        Game.screen.blit(self.text_Chinese, (170, 480))
        Game.screen.blit(self.text_English, (510, 480))

        if self.return_button.draw():
            self.return_button.action()  # Call the action function on button click

    def return_to_main(self):
        self.gameStateManager.set_state('main')