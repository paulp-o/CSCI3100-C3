import pygame
import sys
from pygame import mixer

settingblock_blue = pygame.transform.scale(pygame.image.load('img/settingblock_blue.png'), (700, 150))
settingblock_white = pygame.transform.scale(pygame.image.load('img/settingblock_white.png'), (700, 150))
settingbutton_blue = pygame.transform.scale(pygame.image.load('img/settingbutton_blue.png'), (320, 60))
settingbutton_white = pygame.transform.scale(pygame.image.load('img/settingbutton_white.png'), (320, 60))
returnbutton = pygame.transform.scale(pygame.image.load('img/return.png'), (50, 50))
startbutton = pygame.image.load('img/start_btn.png')
tosettingbutton = pygame.image.load('img/setting_btn.png')

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

class Game:
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 2, 512)
        mixer.init()
        pygame.init()
        Game.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake.io')
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('customization')
        self.main = Main(Game.screen, self.gameStateManager)
        self.setting = Setting(Game.screen, self.gameStateManager)
        self.customization = Customization(Game.screen, self.gameStateManager)
        self.game_arena = GameArena(Game.screen, self.gameStateManager)

        self.play = Play(Game.screen, self.gameStateManager)
        self.bgm = pygame.mixer.Sound('sound/bgm.mp3')
        self.bgm.set_volume(0.05)

        self.states = {'setting': self.setting,
                       'main': self.main,
                       'customization': self.customization,
                       'game_arena': self.game_arena}

    def run(self):
        while True:
            self.bgm.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.quit()

            self.states[self.gameStateManager.get_state()].run()
            pygame.display.update()
            self.clock.tick(60)


class Main:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.background = pygame.image.load('img/background.jpg')
        title_font = pygame.font.Font(None, 120)
        text_font = pygame.font.Font(None, 35)
        self.text_title = title_font.render('Snake.io', False, 'white')
        self.start_button = Button(250, 300, startbutton, 0.8, self.go_to_play)
        self.tosetting_button = Button(120, 450, tosettingbutton, 0.1, self.to_setting)

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


class Setting:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        title_font = pygame.font.Font(None, 50)
        text_font = pygame.font.Font(None, 35)

        self.background = pygame.image.load('img/background.jpg')
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

        self.return_button = Button(675, 30, returnbutton, 1, self.return_to_main)

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

        if self.return_button.back():
            self.return_button.action()  # Call the action function on button click

    def return_to_main(self):
        self.gameStateManager.set_state('main')


class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState

    def get_state(self):
        return self.currentState

    def set_state(self, state):
        self.currentState = state


class Button():
    def __init__(self, x, y, image, scale, action=None):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.action = action

    def back(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                if self.action:
                    self.action()  # Call the action function if provided

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        Game.screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


class Customization:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        title_font = pygame.font.Font(None, 50)
        text_font = pygame.font.Font(None, 35)

        # ---- ICON/IMAGE ----
        self.pattern_alternating_icon = pygame.image.load(
            "Assets/Customisation/pattern_alternating_icon.png").convert_alpha()
        self.pattern_outline_icon = pygame.image.load("Assets/Customisation/pattern_outline_icon.png").convert_alpha()
        self.pattern_static_icon = pygame.image.load("Assets/Customisation/pattern_static_icon.png").convert_alpha()
        self.tick_icon = pygame.image.load("Assets/Customisation/tick.png").convert_alpha()


        # preparing UI elements
        # ---- TEXT ----
        self.title_customization = title_font.render('Customization', False, 'white')
        self.text_color_selection = text_font.render('Color Selection', False, 'white')
        self.text_pattern = text_font.render('Pattern', False, 'white')
        self.text_skin_preview = text_font.render("Skin Preview", False, 'white')

        self.text_purchase = title_font.render('Purchase', False, 'white')




        # ---- BUTTON ----
        self.ALTERNATING_BUTTON_POS = (300, 100)
        self.STATIC_BUTTON_POS = (400, 100)
        self.OUTLINE_BUTTON_POS = (500, 100)
        self.alternating_button_clicked = False
        self.static_button_clicked = False
        self.outline_button_clicked = False
        self.pattern_alternating_button = Button(self.ALTERNATING_BUTTON_POS[0], self.ALTERNATING_BUTTON_POS[1], self.pattern_alternating_icon, 0.05)
        self.pattern_static_button = Button(self.STATIC_BUTTON_POS[0], self.STATIC_BUTTON_POS[1], self.pattern_static_icon, 0.05)
        self.pattern_outline_button = Button(self.OUTLINE_BUTTON_POS[0], self.OUTLINE_BUTTON_POS[1], self.pattern_outline_icon, 0.05)

    def run(self):
        Game.screen.fill((200, 200, 180))  # giving background color

        # --- TEXT ----
        Game.screen.blit(self.title_customization, (0, 0))
        Game.screen.blit(self.text_color_selection, (20, 50))
        Game.screen.blit(self.text_pattern, (300, 50))
        Game.screen.blit(self.text_skin_preview, (20, 150))

        # ---- BUTTON ----
        self.pattern_static_button.back()
        # self.pattern_alternating_button.draw()
        self.pattern_outline_button.back()


        # ---- IMAGE ----
        SIZE = 25
        if self.pattern_alternating_button.back() and self.alternating_button_clicked == False:
            print("Clicked")
            self.alternating_button_clicked = True
            Game.screen.blit(pygame.transform.scale(self.tick_icon, (SIZE, SIZE)),
                             (self.ALTERNATING_BUTTON_POS[0]+SIZE, self.ALTERNATING_BUTTON_POS[1]))


class GameArena:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.score_text_font = pygame.font.Font(None, 80)

        self.score_text = self.score_text_font.render('Score', False, 'white')
        self.score_text_rect = self.score_text.get_rect(center=(SCREEN_WIDTH/2, 50))  # to ensure center of text at top

    def run(self):
        Game.screen.fill((200, 200, 180))  # giving background color
        Game.screen.blit(self.score_text, self.score_text_rect)


if __name__ == '__main__':
    game = Game()
    game.run()


"""
import pygame
import sys

settingblock_blue = pygame.transform.scale(pygame.image.load('settingblock_blue.png'), (700, 150))
settingblock_white = pygame.transform.scale(pygame.image.load('settingblock_white.png'), (700, 150))
settingbutton_blue = pygame.transform.scale(pygame.image.load('settingbutton_blue.png'), (320, 60))
settingbutton_white = pygame.transform.scale(pygame.image.load('settingbutton_white.png'), (320, 60))
returnbutton = pygame.transform.scale(pygame.image.load('return.png'), (50, 50))

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800


class Game:
    def __init__(self):
        pygame.init()
        Game.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake.io')
        self.clock = pygame.time.Clock()

        self.gameStateManager = GameStateManager('customization')   # Initial State
        self.main = Main(Game.screen, self.gameStateManager)
        self.setting = Setting(Game.screen, self.gameStateManager)
        self.customization = Customization(Game.screen, self.gameStateManager)
        self.game_arena = GameArena(Game.screen, self.gameStateManager)

        self.states = {'setting': self.setting,
                       'main': self.main,
                       'customization': self.customization,
                       'game_arena': self.game_arena}

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.quit()

            self.states[self.gameStateManager.get_state()].run()
            pygame.display.update()
            self.clock.tick(60)


class Main:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager

    def run(self):
        self.display.fill('#4d70d1')



class Customization:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        title_font = pygame.font.Font(None, 50)
        text_font = pygame.font.Font(None, 35)

        # ---- ICON/IMAGE ----
        self.pattern_alternating_icon = pygame.image.load(
            "Assets/Customisation/pattern_alternating_icon.png").convert_alpha()
        self.pattern_outline_icon = pygame.image.load("Assets/Customisation/pattern_outline_icon.png").convert_alpha()
        self.pattern_static_icon = pygame.image.load("Assets/Customisation/pattern_static_icon.png").convert_alpha()
        self.tick_icon = pygame.image.load("Assets/Customisation/tick.png").convert_alpha()


        # preparing UI elements
        # ---- TEXT ----
        self.title_customization = title_font.render('Customization', False, 'white')
        self.text_color_selection = text_font.render('Color Selection', False, 'white')
        self.text_pattern = text_font.render('Pattern', False, 'white')
        self.text_skin_preview = text_font.render("Skin Preview", False, 'white')

        self.text_purchase = title_font.render('Purchase', False, 'white')




        # ---- BUTTON ----
        self.ALTERNATING_BUTTON_POS = (300, 100)
        self.STATIC_BUTTON_POS = (400, 100)
        self.OUTLINE_BUTTON_POS = (500, 100)
        self.alternating_button_clicked = False
        self.static_button_clicked = False
        self.outline_button_clicked = False
        self.pattern_alternating_button = Button(self.ALTERNATING_BUTTON_POS[0], self.ALTERNATING_BUTTON_POS[1], self.pattern_alternating_icon, 0.05)
        self.pattern_static_button = Button(self.STATIC_BUTTON_POS[0], self.STATIC_BUTTON_POS[1], self.pattern_static_icon, 0.05)
        self.pattern_outline_button = Button(self.OUTLINE_BUTTON_POS[0], self.OUTLINE_BUTTON_POS[1], self.pattern_outline_icon, 0.05)

    def run(self):
        Game.screen.fill((200, 200, 180))  # giving background color

        # --- TEXT ----
        Game.screen.blit(self.title_customization, (0, 0))
        Game.screen.blit(self.text_color_selection, (20, 50))
        Game.screen.blit(self.text_pattern, (300, 50))
        Game.screen.blit(self.text_skin_preview, (20, 150))

        # ---- BUTTON ----
        self.pattern_static_button.draw()
        # self.pattern_alternating_button.draw()
        self.pattern_outline_button.draw()


        # ---- IMAGE ----
        SIZE = 25
        if self.pattern_alternating_button.draw() and self.alternating_button_clicked == False:
            print("Clicked")
            self.alternating_button_clicked = True
            Game.screen.blit(pygame.transform.scale(self.tick_icon, (SIZE, SIZE)),
                             (self.ALTERNATING_BUTTON_POS[0]+SIZE, self.ALTERNATING_BUTTON_POS[1]))


class GameArena:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.score_text_font = pygame.font.Font(None, 80)

        self.score_text = self.score_text_font.render('Score', False, 'white')
        self.score_text_rect = self.score_text.get_rect(center=(SCREEN_WIDTH/2, 50))  # to ensure center of text at top

    def run(self):
        Game.screen.fill((200, 200, 180))  # giving background color
        Game.screen.blit(self.score_text, self.score_text_rect)







class Setting:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        title_font = pygame.font.Font(None, 50)
        text_font = pygame.font.Font(None, 35)

        self.background = pygame.image.load('background.jpg')
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

        self.return_button = Button(675, 30, returnbutton, 1, self.return_to_main)

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


class GameStateManager:
    def __init__(self, currentState):
        self.currentState = currentState

    def get_state(self):
        return self.currentState

    def set_state(self, state):
        self.currentState = state


class Button():
    def __init__(self, x, y, image, scale, action=None):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.action = action

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                if self.action:
                    self.action()  # Call the action function if provided

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        Game.screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


if __name__ == '__main__':
    game = Game()
    game.run()


import pygame
import sys

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_WIDTH))
pygame.display.set_caption("Game Demo")

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int (height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        pos = pygame.mouse.get_pos()  # get mouse position

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos): # if the mouse cursor is hovering the button
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        
        # draw the button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Customization():
    @staticmethod
    class IconCollection():
        # Collection of icon images that acts as the global collection of this class
        pattern_alternating_icon = pygame.image.load(
            "Assets/Customisation/pattern_alternating_icon.png").convert_alpha()
        pattern_outline_icon = pygame.image.load("Assets/Customisation/pattern_outline_icon.png").convert_alpha()
        pattern_static_icon = pygame.image.load("Assets/Customisation/pattern_static_icon.png").convert_alpha()

    # load images
    def __init__(self):
        return

    @staticmethod
    def create_button():
        buttons = []    # initialize a buttons array
        # create buttons
        pattern_alternating_button = Button(300, 50, Customization.IconCollection.pattern_alternating_icon, 0.05)
        pattern_static_button = Button(400, 50, Customization.IconCollection.pattern_static_icon, 0.05)
        pattern_outline_button = Button(500, 50, Customization.IconCollection.pattern_outline_icon, 0.05)

        # put all buttons to buttons array
        buttons.append(pattern_alternating_button)
        buttons.append(pattern_static_button)
        buttons.append(pattern_outline_button)

        return buttons

    @staticmethod
    def draw_ui(buttons):
        # draw all the UI elements here
        for button in buttons:
            button.draw()


run = True
buttons = Customization.create_button() # create buttons one time only
while run:
    screen.fill((202, 228, 241))    # default background color

    Customization.draw_ui(buttons)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
"""
