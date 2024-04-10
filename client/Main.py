import pygame
import Game
import Button

startbutton = pygame.image.load('Assets/Main Menu/start_btn.png')
tosettingbutton = pygame.image.load('Assets/Main Menu/setting_icon.png')
tocustombutton = pygame.image.load('Assets/Main Menu/shopping_icon.png')
toleaderbutton = pygame.image.load('Assets/Main Menu/leaderboard_icon.png')
exitbutton = pygame.image.load('Assets/Main Menu/exit_icon.png')


class Main:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.background = pygame.image.load('Assets/Main Menu/background.jpg')
        title_font = pygame.font.Font(None, 120)
        text_font = pygame.font.Font(None, 35)
        self.text_en_title = title_font.render('Snake.io', False, 'white')
        self.text_ch_title = title_font.render('chinese Snake.io', False, 'white')

        self.start_button = Button.Button(
            250, 300, startbutton, 0.8, self.go_to_play)
        self.tosetting_button = Button.Button(
            120, 450, tosettingbutton, 0.1, self.to_setting)
        self.tocustom_button = Button.Button(
            300, 450, tocustombutton, 0.1, self.to_custom)
        self.toleaderboard_button = Button.Button(
            500, 450, toleaderbutton, 0.1, self.to_leaderboard)
        self.exit_button = Button.Button(600, 40, exitbutton, 0.05, self.exit)


    def run(self):
            Game.screen.blit(self.background, (0, 0))
            Game.screen.blit(self.text_en_title, (200, 90))
            if self.start_button.draw():
                self.start_button.action()

            if self.tosetting_button.draw():
                self.tosetting_button.action()

            if self.tocustom_button.draw():
                self.tocustom_button.action()

            if self.toleaderboard_button.draw():
                self.toleaderboard_button.action()

            if self.exit_button.draw():
                self.exit_button.action()



    def go_to_play(self):
        self.gameStateManager.set_state('start_game')

    def to_setting(self):
        self.gameStateManager.set_state('settings')

    def to_custom(self):
        self.gameStateManager.set_state('customization')

    def to_leaderboard(self):
        self.gameStateManager.set_state('leaderboard')

    def exit(self):
        pygame.quit()
        sys.exit()
