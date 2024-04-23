import pygame
import Game


class Button:
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
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
                if self.action:
                    self.action()  # Call the action function if provided

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        Game.screen.blit(self.image, (self.rect.x, self.rect.y))

        return action


class RatioButton:
    def __init__(self, x, y, image, scale, action=None, selected=False, locked=False):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.action = action
        self.selected = selected
        self.locked = locked
        self.tick_icon = pygame.image.load("Assets/Customisation/tick.png").convert_alpha()
        self.lock_icon = pygame.image.load("Assets/Customisation/lock.png").convert_alpha()

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.selected == False and self.locked == False:
                # if selected
                self.selected = True
                action = True
                if self.action:
                    self.action()  # Call the action function if provided

        Game.screen.blit(self.image, (self.rect.x, self.rect.y))

        if self.locked:
            SIZE = 25
            Game.screen.blit(pygame.transform.scale(self.lock_icon, (SIZE, SIZE)),
                             (self.rect.topleft[0] + SIZE, self.rect.topleft[1]))  # Draw the tick image

        if self.selected == True:
            # If the option is selected
            SIZE = 25
            Game.screen.blit(pygame.transform.scale(self.tick_icon, (SIZE, SIZE)),
                             (self.rect.topleft[0] + SIZE, self.rect.topleft[1]))  # Draw the tick image

        return action


class RatioButtonsGroup:
    def __init__(self, buttons):
        self.buttons = buttons   # a list of buttons
        self.cur_selected_button = None
        self.selected_button_count = 0   # this must be 1 to ensure only 1 button is selected in the button group
        self.find_selected_button(self.buttons)

    def update(self):
        self.cur_selected_button.selected = False
        self.selected_button_count = 0
        self.find_selected_button(self.buttons)

    def draw(self):
        for button in self.buttons:
            button.draw()

    def find_selected_button(self, buttons):
        for button in buttons:
            if button.selected and self.selected_button_count <= 0:
                self.selected_button_count = self.selected_button_count + 1
                self.cur_selected_button = button
            elif button.selected and self.selected_button_count > 0:
                print("Warning: multiple buttons is selected initially!")
        # print(self.selected_button_count)


