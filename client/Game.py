import pygame
import sys
import Main
import Settings
import GameStateManager
import Customization
import GameArena
from pygame import mixer

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

clock = pygame.time.Clock()
states = None
gameStateManager = None
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Game:
    @staticmethod
    def __init__():
        pygame.mixer.pre_init(44100, -16, 2, 512)
        mixer.init()
        pygame.init()
        pygame.display.set_caption('Snake.io')

        # Create a dedicated channel for BGM
        bgm_channel = mixer.Channel(0)

        # Load and play the BGM
        bgm = pygame.mixer.Sound('Audio/bgm.mp3')
        bgm.set_volume(0.01)
        bgm_channel.play(bgm, loops=-1)  # -1 for continuous looping

        global gameStateManager
        gameStateManager = GameStateManager.GameStateManager('settings')
        main = Main.Main(screen, gameStateManager)
        settings = Settings.Settings(screen, gameStateManager, bgm_channel)
        customization = Customization.Customization(screen, gameStateManager)
        game_arena = GameArena.GameArena(screen, gameStateManager)



        
        global states
        states = {'settings': settings,
                       'main': main,
                       'customization': customization,
                       'game_arena': game_arena}

    @staticmethod
    def run():
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.quit()

            states[gameStateManager.get_state()].run()
            pygame.display.update()
            clock.tick(60)


if __name__ == '__main__':
    Game.__init__()
    Game.run()


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
