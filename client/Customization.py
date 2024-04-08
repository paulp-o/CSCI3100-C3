import pygame
import Button
import Game

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
        self.pattern_alternating_button = Button.Button(self.ALTERNATING_BUTTON_POS[0], self.ALTERNATING_BUTTON_POS[1], self.pattern_alternating_icon, 0.05)
        self.pattern_static_button = Button.Button(self.STATIC_BUTTON_POS[0], self.STATIC_BUTTON_POS[1], self.pattern_static_icon, 0.05)
        self.pattern_outline_button = Button.Button(self.OUTLINE_BUTTON_POS[0], self.OUTLINE_BUTTON_POS[1], self.pattern_outline_icon, 0.05)

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