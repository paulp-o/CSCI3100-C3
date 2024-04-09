import pygame, sys
import Game
import Button


class Login:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        text_font = pygame.font.Font(None,32)
        title_font = pygame.font.Font(None, 60)  

        # Icon
        self.login_icon = pygame.transform.scale(pygame.image.load("Assets/Login/login_icon.png").convert_alpha(), (6000, 1500))
        self.guest_login_icon = pygame.transform.scale(pygame.image.load("Assets/Login/guest_login_icon.png").convert_alpha(), (1000, 1000))
        
        # Text
        self.text_title = title_font.render('Login', False, 'white')
        self.text_id = text_font.render('your id', False, 'white')
        self.text_password = text_font.render('your password', False, 'white')
        self.text_guest = text_font.render('Play as a guest', False, 'white')
        
        # Button
        self.LOGIN_BUTTON_POS = (50,250)
        self.login_button = Button.OptionButton(self.LOGIN_BUTTON_POS[0],
                                                self.LOGIN_BUTTON_POS[1],
                                                self.login_icon,
                                                0.05,
                                                self.try_login,
                                                )
        self.GUEST_LOGIN_BUTTON_POS = (100,450)
        self.guest_login_button = Button.OptionButton(self.GUEST_LOGIN_BUTTON_POS[0],
                                                self.GUEST_LOGIN_BUTTON_POS[1],
                                                self.guest_login_icon,
                                                0.05,
                                                self.try_guest_login,
                                                )
        
                
    def run(self):
        Game.screen.fill((200, 200, 180))
        
        # Text
        Game.screen.blit(self.text_title, (50,50))
        Game.screen.blit(self.text_id, (50, 150))
        Game.screen.blit(self.text_password, (50,200))
        Game.screen.blit(self.text_guest, (50,400))
        
        # Button
        self.login_button.draw()
        self.guest_login_button.draw()
                
        
    
    def try_login(self):
        # need verify procedure
        self.verify = True
        if self.verify:
            self.gameStateManager.set_state('main') # go to main menu
            
    def try_guest_login(self):
        self.gameStateManager.set_state('main') # go to main menu
        
       