import pygame
import Button
import Game
import math

""" 
This is the customization page of the game. 
Snake body is stored in the self.snake in SnakeDemo class. 
"""

class Color:
    BLACK = (0, 0, 0)
    WHITE = (255,255,255)
    LIGHT_BLUE = (30,129,176)


g_display = None
selected_color_1 = Color.WHITE    # default color is white
# selected_color_2 = Color.BLACK    # for alternating color
# maximum_color_choice = 1  # number of colors the player can use

class SnakeDemo:
    class SnakeHead:
        def __init__(self, width):
            self.snake_head = None
            self.pos = (450, 250)
            self.radius = 25
            self.width = width

        def draw(self):
            self.snake_head = pygame.draw.circle(g_display, selected_color_1, self.pos, self.radius, self.width)
            # self.snake_left_eye = pygame.draw.circle(g_display, (0, 0, 0), self.pos, self.radius-15, self.width)

    class SnakeBody:
        def __init__(self, previous_part_pos, color, width):
            self.snake_body = None
            self.pos = (previous_part_pos[0] - 20, previous_part_pos[1] - 20)
            self.radius = 25
            self.color = color
            self.width = width

        def draw(self):
            self.snake_body = pygame.draw.circle(g_display, self.color, self.pos, self.radius, self.width)

    def __init__(self, mode):
        self.radius = 30
        self.length = 20
        self.mode_list = ["alternating", "static", "outline"]
        self.mode = mode

        if self.mode == self.mode_list.index("alternating") or self.mode == self.mode_list.index("static"):
            self.width = 0
        elif self.mode == self.mode_list.index("outline"):
            self.width = 5
        else:
            print("Mode not exist.")
            return

        self.snake_head = self.SnakeHead(self.width)
        self.snake = [self.snake_head]  # the array that stores the snake

        for idx in range(0, self.length):
            new_pos = (self.snake[idx].pos[0],
                       math.sin(math.sin((360 / self.length) * idx)) * 360 / self.length + self.snake[0].pos[1])
            print(new_pos)
            # ---- Check for mode of rendering ----
            if self.mode == self.mode_list.index("alternating"):
                if idx % 2 == 0:
                    self.snake.append(self.SnakeBody(new_pos, (255-selected_color_1[0], 255-selected_color_1[1], 255-selected_color_1[2]), 0))
                else:
                    self.snake.append(self.SnakeBody(new_pos, selected_color_1, 0))
            elif self.mode == self.mode_list.index("static"):
                self.snake.append(self.SnakeBody(new_pos, selected_color_1, 0))
            elif self.mode == self.mode_list.index("outline"):
                self.snake.append(self.SnakeBody(new_pos, selected_color_1, 5))

    def draw(self):
        for idx in range(0, self.length):
            # draw all parts in the snake
            self.snake[self.length - idx - 1].draw()


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
        self.color_selection_lblue_icon = pygame.image.load("Assets/Customisation/color_selection_light_blue.png").convert_alpha()

        self.back_icon = pygame.image.load("Assets/Settings/return.png").convert_alpha()

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
        self.COLOR_SELECTION_BLACK_BUTTON_POS = (40, 100)
        self.COLOR_SELECTION_WHITE_BUTTON_POS = (100, 100)
        self.COLOR_SELECTION_LBLUE_BUTTON_POS = (160, 100)

        self.back_button = Button.Button(Game.SCREEN_WIDTH - 60, 5, self.back_icon, 0.5)    # back button

        # Color Selection Buttons
        self.color_selection_black_button = (
            Button.OptionButton(self.COLOR_SELECTION_BLACK_BUTTON_POS[0],
                                self.COLOR_SELECTION_BLACK_BUTTON_POS[1],
                                self.color_selection_black_icon,
                                0.04,
                                self.on_color_selection_black_click,
                                True)
        )
        self.color_selection_white_button = (
            Button.OptionButton(self.COLOR_SELECTION_WHITE_BUTTON_POS[0],
                                self.COLOR_SELECTION_WHITE_BUTTON_POS[1],
                                self.color_selection_white_icon,
                                0.04,
                                self.on_color_selection_white_click,
                                False)
        )
        self.color_selection_lblue_button = (
            Button.OptionButton(self.COLOR_SELECTION_LBLUE_BUTTON_POS[0],
                                self.COLOR_SELECTION_LBLUE_BUTTON_POS[1],
                                self.color_selection_lblue_icon,
                                0.04,
                                self.on_color_selection_lblue_click,
                                False)
        )

        # Pattern Selection Buttons
        self.pattern_alternating_button = Button.OptionButton(self.ALTERNATING_BUTTON_POS[0],
                                                              self.ALTERNATING_BUTTON_POS[1],
                                                              self.pattern_alternating_icon,
                                                              0.05,
                                                              self.on_alternating_button_click,
                                                              True)
        self.pattern_static_button = Button.OptionButton(self.STATIC_BUTTON_POS[0],
                                                         self.STATIC_BUTTON_POS[1],
                                                         self.pattern_static_icon,
                                                         0.05,
                                                         self.on_static_button_click)
        self.pattern_outline_button = Button.OptionButton(self.OUTLINE_BUTTON_POS[0],
                                                          self.OUTLINE_BUTTON_POS[1],
                                                          self.pattern_outline_icon,
                                                          0.05,
                                                          self.on_outline_button_click)

        # ---- BUTTON ACTIONS ----
        self.back_button.action = lambda: self.gameStateManager.set_state('main')  # go back to main menu

        # ---- SHAPES ----
        global selected_color_1
        selected_color_1 = Color.BLACK
        self.snake = SnakeDemo(0)

    def on_color_selection_black_click(self):
        # Action: the black color selection button is clicked
        global selected_color_1

        self.color_selection_white_button.selected = False
        self.color_selection_lblue_button.selected = False
        selected_color_1 = Color.BLACK
        self.reset(self.snake.mode)


    def on_color_selection_white_click(self):
        # Action: the white color selection button is clicked
        global selected_color_1

        self.color_selection_black_button.selected = False
        self.color_selection_lblue_button.selected = False
        selected_color_1 = Color.WHITE

        self.reset(self.snake.mode)

    def on_color_selection_lblue_click(self):
        # Action: the light blue color selection button is clicked
        global selected_color_1

        self.color_selection_black_button.selected = False
        self.color_selection_white_button.selected = False
        selected_color_1 = Color.LIGHT_BLUE

        self.reset(self.snake.mode)


    def on_alternating_button_click(self):
        # Action: the alternating_button is clicked
        self.pattern_static_button.selected = False
        self.pattern_outline_button.selected = False
        self.color_selection_lblue_button.selected = False
        self.color_selection_black_button.selected = False
        self.color_selection_white_button.selected = False
        self.reset(0)
        global maximum_color_choice
        # maximum_color_choice = 1
        """
        if selected_color_1 == Color.BLACK:
            self.color_selection_black_button.selected = True
        if selected_color_1 == Color.WHITE:
            self.color_selection_white_button.selected = True
        if selected_color_1 == Color.LIGHT_BLUE:
            self.color_selection_lblue_button.selected = True
        """

        print("Clicked Alternating Button")

    def on_static_button_click(self):
        # Action: the static_button is clicked
        self.pattern_alternating_button.selected = False
        self.pattern_outline_button.selected = False
        self.reset(1)
        global maximum_color_choice
        # maximum_color_choice = 1
        print("Clicked Static Button")

    def on_outline_button_click(self):
        # Action: the outline_button is clicked
        self.pattern_alternating_button.selected = False
        self.pattern_static_button.selected = False
        self.reset(2)
        global maximum_color_choice
        # maximum_color_choice = 1
        print("Clicked Outline Button")

    def reset(self, mode):
        # reset demo snake
        del self.snake  # delete the original snake
        self.snake = SnakeDemo(mode)

    def run(self):
        Game.screen.fill((200, 200, 180))  # giving background color

        # --- TEXT ----
        Game.screen.blit(self.title_customization, (0, 0))
        Game.screen.blit(self.text_color_selection, (20, 50))
        Game.screen.blit(self.text_pattern, (300, 50))
        Game.screen.blit(self.text_skin_preview, (20, 150))

        # ---- BUTTON ----
        self.color_selection_black_button.draw()
        self.color_selection_white_button.draw()
        self.color_selection_lblue_button.draw()
        self.pattern_static_button.draw()
        self.pattern_alternating_button.draw()
        self.pattern_outline_button.draw()
        self.back_button.draw()

        # ---- SNAKE ----
        self.snake.draw()
