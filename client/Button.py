import pygame
import Game

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
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                action = True
                if self.action:
                    self.action()  # Call the action function if provided

        Game.screen.blit(self.image, (self.rect.x, self.rect.y))

        return action