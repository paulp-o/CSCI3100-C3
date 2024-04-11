from pygame import mixer
import StartGame
import Register
import Button
import Leaderboard
import Login
import Gameover
import Customization
import GameStateManager
import Settings
import Main
import sys
import pygame
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

clock = pygame.time.Clock()
states = None
gameStateManager = None
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
music_on = True
SFX_on = True
global mouse
mouse = True
global kb
kb = False
global chinese
chinese = False
global english
english = True


class Game:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 512)
        mixer.init()
        pygame.init()
        pygame.display.set_caption('Snake.io')

        global gameStateManager
        gameStateManager = GameStateManager.GameStateManager('login')
        main = Main.Main(screen, gameStateManager)
        settings = Settings.Settings(
            screen, gameStateManager, music_on, SFX_on, mouse, kb, chinese, english)
        customization = Customization.Customization(screen, gameStateManager)
        gameover = Gameover.Gameover(screen, gameStateManager)
        login = Login.Login(screen, gameStateManager)
        leaderboard = Leaderboard.Leaderboard(screen, gameStateManager)
        register = Register.Register(screen, gameStateManager)
        start_game = StartGame.StartGame(screen, gameStateManager)

        noBgm = no_bgm(gameStateManager)
        yesBgm = yes_bgm(gameStateManager)
        noSFX = no_SFX(gameStateManager)
        yesSFX = yes_SFX(gameStateManager)

        global states
        states = {'settings': settings,
                  'main': main,
                  'customization': customization,
                  'gameover': gameover,
                  'login': login,
                  'no_bgm': noBgm,
                  'yes_bgm': yesBgm,
                  'no_SFX': noSFX,
                  'yes_SFX': yesSFX,
                  'leaderboard': leaderboard,
                  'register': register,
                  'start_game': start_game
                  }

        Game.bgm = pygame.mixer.Sound('Audio/bgm.mp3')
        Game.bgm.set_volume(0.01)
        pygame.mixer.Sound.play(Game.bgm)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            states[gameStateManager.get_state()].run()
            pygame.display.update()
            clock.tick(60)


class no_bgm:
    def __init__(self, gameStateManager):
        self.gameStateManager = gameStateManager

    def run(self):
        Game.bgm.set_volume(0)
        self.gameStateManager.set_state('settings')


class yes_bgm:
    def __init__(self, gameStateManager):
        self.gameStateManager = gameStateManager

    def run(self):
        Game.bgm.set_volume(0.01)
        self.gameStateManager.set_state('settings')


class no_SFX:
    def __init__(self, gameStateManager):
        self.gameStateManager = gameStateManager

    def run(self):
        Settings.sfxvol = 0
        self.gameStateManager.set_state('settings')


class yes_SFX:
    def __init__(self, gameStateManager):
        self.gameStateManager = gameStateManager

    def run(self):
        Settings.sfxvol = 0.01
        self.gameStateManager.set_state('settings')


if __name__ == '__main__':
    game = Game()
    game.run()


"""
class Play:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.background = pygame.image.load('img/background.jpg')
        title_font = pygame.font.Font(None, 120)
        text_font = pygame.font.Font(None, 35)
        self.return_button = Button(675, 30, returnbutton, 1, self.return_to_main)

    def run(self):
        Game.screen.blit(self.background, (0, 0))
        if self.return_button.back():
            self.return_button.action()

    def return_to_main(self):
        self.gameStateManager.set_state('main')

"""
