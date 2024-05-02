import pygame
import Button
import Game
import math

""" 
    This is the customization page of the game. 
    Snake body is stored in the ${self.snake} in SnakeDemo class. 
    
    Snake color is stored in ${selected_color} as a tuple (R, G, B)
    Snake pattern is stored in ${self.snake.mode}; 0 is alternating; 1 is static; 2 is outline
    Other module can use getters to obtain the above information about the snake.
"""

class Color:
    BLACK = (0, 0, 0)
    WHITE = (255,255,255)
    SATURATED_BLUE = (30, 129, 176)
    RED = (225,55,72)
    YELLOW = (225, 219, 55)
    AQUA = (58, 223, 192)
    VIOLET = (211, 68, 216)
    DARK_BLUE = (63, 63, 192)


g_display = None
selected_color = Color.BLACK    # default color is white
mode = 0

class SnakeDemo:
    class SnakeHead:
        def __init__(self, width):
            self.snake_head = None
            self.pos = (450, 250)
            self.left_eye_pos = (460, 255)
            self.radius = 25
            self.width = width

        def draw(self):
            self.snake_head = pygame.draw.circle(g_display, selected_color, self.pos, self.radius, self.width)
            #self.snake_left_eye = pygame.draw.circle(g_display, (255, 255, 255), self.left_eye_pos, self.radius-18)
            #self.snake_left_eye_pupil = pygame.draw.circle(g_display, (0, 0, 0), self.left_eye_pos,self.radius - 20)

    class SnakeBody:
        def __init__(self, previous_part_pos, color, width):
            self.snake_body = None
            self.pos = (previous_part_pos[0] - 20, previous_part_pos[1] - 20)
            self.radius = 25
            self.color = color
            self.width = width

        def draw(self):
            self.snake_body = pygame.draw.circle(g_display, self.color, self.pos, self.radius, self.width)

    def __init__(self):
        self.radius = 30
        self.length = 20
        self.mode_list = ["static", "alternating", "outline"]
        global mode
        self.mode = mode

        if self.mode == self.mode_list.index("alternating") or self.mode == self.mode_list.index("static"):
            self.width = 0
        elif self.mode == self.mode_list.index("outline"):
            self.width = 5
        else:
            print("Mode does not exist.")
            return

        self.snake_head = self.SnakeHead(self.width)
        self.snake = [self.snake_head]  # the array that stores the snake

        for idx in range(0, self.length):
            new_pos = (self.snake[idx].pos[0],
                       math.sin(math.sin((360 / self.length) * idx)) * 360 / self.length + self.snake[0].pos[1])
            # print(new_pos)
            # ---- Check for mode of rendering ----
            if self.mode == self.mode_list.index("alternating"):
                if idx % 2 == 0:
                    self.snake.append(self.SnakeBody(new_pos, self.get_supplementary_color(), 0))
                else:
                    self.snake.append(self.SnakeBody(new_pos, self.get_main_color(), 0))
            elif self.mode == self.mode_list.index("static"):
                self.snake.append(self.SnakeBody(new_pos, self.get_main_color(), 0))
            elif self.mode == self.mode_list.index("outline"):
                self.snake.append(self.SnakeBody(new_pos, self.get_main_color(), 5))

    def get_pattern(self):
        return self.mode

    def get_color(self):
        return selected_color

    def draw(self):
        for idx in range(0, self.length):
            # draw all parts in the snake
            self.snake[self.length - idx - 1].draw()

    def set_main_color(self, color):
        global selected_color
        selected_color = color

    def get_main_color(self):
        return selected_color

    def get_supplementary_color(self):
        # return the color for alternative pattern
        return (255 - selected_color[0], 255 - selected_color[1], 255 - selected_color[2])

    def get_pattern(self):
        return mode


class Customization:
    def __init__(self, display, gameStateManager):
        global g_display
        g_display = display
        self.gameStateManager = gameStateManager
        title_font = pygame.font.Font(None, 50)
        text_font = pygame.font.Font(None, 35)

        # preparing UI elements
        # ---- ICON/IMAGE ----
        self.pattern_alternating_icon = pygame.image.load(
            "Assets/Customisation/pattern_alternating_icon.png").convert_alpha()
        self.pattern_outline_icon = pygame.image.load("Assets/Customisation/pattern_outline_icon.png").convert_alpha()
        self.pattern_static_icon = pygame.image.load("Assets/Customisation/pattern_static_icon.png").convert_alpha()
        self.color_selection_black_icon = pygame.image.load("Assets/Customisation/color_selection_black.png").convert_alpha()
        self.color_selection_white_icon = pygame.image.load("Assets/Customisation/color_selection_white.png").convert_alpha()
        self.color_selection_sblue_icon = pygame.image.load("Assets/Customisation/color_selection_saturated_blue.png").convert_alpha()

        self.color_selection_red_icon = pygame.image.load("Assets/Customisation/color_selection_red.png").convert_alpha()
        self.color_selection_yellow_icon = pygame.image.load("Assets/Customisation/color_selection_yellow.png").convert_alpha()
        self.color_selection_aqua_icon = pygame.image.load("Assets/Customisation/color_selection_aqua.png").convert_alpha()
        self.color_selection_violet_icon = pygame.image.load("Assets/Customisation/color_selection_violet.png").convert_alpha()
        self.color_selection_dblue_icon = pygame.image.load("Assets/Customisation/color_selection_dark_blue.png").convert_alpha()

        self.back_icon = pygame.image.load("Assets/Settings/return.png").convert_alpha()

        # ---- TEXT ----
        self.title_customization = title_font.render('Customization', False, 'white')
        self.text_color_selection = text_font.render('Color Selection', False, 'white')
        self.text_pattern = text_font.render('Pattern', False, 'white')
        self.text_skin_preview = text_font.render("Skin Preview", False, 'white')

        self.text_purchase = title_font.render('Purchase', False, 'white')

        # ---- BUTTON ----
        self.STATIC_BUTTON_POS = (300, 100)
        self.ALTERNATING_BUTTON_POS = (50, 500)
        self.OUTLINE_BUTTON_POS = (130, 500)

        self.COLOR_SELECTION_BLACK_BUTTON_POS = (40, 100)
        self.COLOR_SELECTION_WHITE_BUTTON_POS = (100, 100)
        self.COLOR_SELECTION_SBLUE_BUTTON_POS = (160, 100)

        self.COLOR_SELECTION_RED_BUTTON_POS = (50, 390)
        self.COLOR_SELECTION_YELLOW_BUTTON_POS = (130, 390)
        self.COLOR_SELECTION_AQUA_BUTTON_POS = (210, 390)
        self.COLOR_SELECTION_VIOLET_BUTTON_POS = (290, 390)
        self.COLOR_SELECTION_DBLUE_BUTTON_POS = (370, 390)

        self.back_button = Button.Button(Game.SCREEN_WIDTH - 60, 5, self.back_icon, 0.5)    # back button

        # Color Selection Buttons
        # self.color_selection_buttons stores a group of color selection buttons
        '''
        buttons[0] => BLACK
        buttons[1] => WHITE
        buttons[2] => LIGHT_BLUE ...
        '''
        self.color_selection_buttons = Button.RatioButtonsGroup([
            Button.RatioButton(self.COLOR_SELECTION_BLACK_BUTTON_POS[0],
                               self.COLOR_SELECTION_BLACK_BUTTON_POS[1],
                               self.color_selection_black_icon,
                               0.04,
                               self.on_color_selection_black_click,
                               True),
            Button.RatioButton(self.COLOR_SELECTION_WHITE_BUTTON_POS[0],
                               self.COLOR_SELECTION_WHITE_BUTTON_POS[1],
                               self.color_selection_white_icon,
                               0.04,
                               self.on_color_selection_white_click,
                               False),
            Button.RatioButton(self.COLOR_SELECTION_SBLUE_BUTTON_POS[0],
                               self.COLOR_SELECTION_SBLUE_BUTTON_POS[1],
                               self.color_selection_sblue_icon,
                               0.04,
                               self.on_color_selection_sblue_click,
                               False),
            Button.RatioButton(self.COLOR_SELECTION_RED_BUTTON_POS[0],
                               self.COLOR_SELECTION_RED_BUTTON_POS[1],
                               self.color_selection_red_icon,
                               0.04,
                               self.on_color_selection_red_click,
                               False),
            Button.RatioButton(self.COLOR_SELECTION_YELLOW_BUTTON_POS[0],
                               self.COLOR_SELECTION_YELLOW_BUTTON_POS[1],
                               self.color_selection_yellow_icon,
                               0.04,
                               self.on_color_selection_yellow_click,
                               False),
            Button.RatioButton(self.COLOR_SELECTION_AQUA_BUTTON_POS[0],
                               self.COLOR_SELECTION_AQUA_BUTTON_POS[1],
                               self.color_selection_aqua_icon,
                               0.04,
                               self.on_color_selection_aqua_click,
                               False),
            Button.RatioButton(self.COLOR_SELECTION_VIOLET_BUTTON_POS[0],
                               self.COLOR_SELECTION_VIOLET_BUTTON_POS[1],
                               self.color_selection_violet_icon,
                               0.04,
                               self.on_color_selection_violet_click,
                               False),
            Button.RatioButton(self.COLOR_SELECTION_DBLUE_BUTTON_POS[0],
                               self.COLOR_SELECTION_DBLUE_BUTTON_POS[1],
                               self.color_selection_dblue_icon,
                               0.04,
                               self.on_color_selection_dblue_click,
                               False)

        ]
        )

        # Pattern Selection Buttons
        self.pattern_selection_buttons = Button.RatioButtonsGroup(
            [
                Button.RatioButton(self.STATIC_BUTTON_POS[0],
                                   self.STATIC_BUTTON_POS[1],
                                   self.pattern_static_icon,
                                   0.05,
                                   self.on_static_button_click,
                                   True),
                Button.RatioButton(self.ALTERNATING_BUTTON_POS[0],
                                   self.ALTERNATING_BUTTON_POS[1],
                                   self.pattern_alternating_icon,
                                   0.05,
                                   self.on_alternating_button_click,
                                   False),
                Button.RatioButton(self.OUTLINE_BUTTON_POS[0],
                                   self.OUTLINE_BUTTON_POS[1],
                                   self.pattern_outline_icon,
                                   0.05,
                                   self.on_outline_button_click,
                                   False,
                                   True)
            ]
        )

        # ---- BUTTON ACTIONS ----
        self.back_button.action = lambda: self.gameStateManager.set_state('main')  # go back to main menu

        # ---- SNAKE ----
        self.snake = SnakeDemo()

    def reset(self):
        # reset demo snake, must call everytime there is an update for the snake skin
        del self.snake  # delete the original snake
        self.snake = SnakeDemo()

    def run(self):
        Game.screen.fill((200, 200, 180))  # giving background color

        # --- TEXT ----
        Game.screen.blit(self.title_customization, (0, 0))
        Game.screen.blit(self.text_color_selection, (20, 50))
        Game.screen.blit(self.text_pattern, (300, 50))
        Game.screen.blit(self.text_skin_preview, (20, 150))

        Game.screen.blit(self.text_purchase, (0, 280))
        Game.screen.blit(self.text_color_selection, (20, 340))
        Game.screen.blit(self.text_pattern, (20, 460))

        # ---- BUTTON ----
        self.color_selection_buttons.draw()
        self.pattern_selection_buttons.draw()
        self.back_button.draw()

        # ---- SNAKE ----
        self.snake.draw()

    def handle_color_selection(self, color):
        self.snake.set_main_color(color)
        self.color_selection_buttons.update()
        self.reset() # to refresh the snake demo

    def handle_pattern_selection(self):
        self.pattern_selection_buttons.update()
        self.reset() # to refresh the snake demo

    def on_color_selection_black_click(self):
        # Action: the black color selection button is clicked
        self.handle_color_selection(Color.BLACK)

    def on_color_selection_white_click(self):
        # Action: the white color selection button is clicked
        self.handle_color_selection(Color.WHITE)

    def on_color_selection_sblue_click(self):
        # Action: the light blue color selection button is clicked
        self.handle_color_selection(Color.SATURATED_BLUE)

    def on_color_selection_red_click(self):
        self.handle_color_selection(Color.RED)

    def on_color_selection_yellow_click(self):
        self.handle_color_selection(Color.YELLOW)

    def on_color_selection_aqua_click(self):
        self.handle_color_selection(Color.AQUA)

    def on_color_selection_violet_click(self):
        self.handle_color_selection(Color.VIOLET)

    def on_color_selection_dblue_click(self):
        self.handle_color_selection(Color.DARK_BLUE)

    def on_static_button_click(self):
        # Action: the static_button is clicked
        global mode
        mode = 0
        self.handle_pattern_selection()

    def on_alternating_button_click(self):
        # Action: the alternating_button is clicked
        global mode
        mode = 1
        self.handle_pattern_selection()

    def on_outline_button_click(self):
        # Action: the outline_button is clicked
        global mode
        mode = 2
        self.handle_pattern_selection()