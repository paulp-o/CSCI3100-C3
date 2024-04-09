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

        
        # Text
        self.text_title = title_font.render('Login', False, 'white')
        self.text_id = text_font.render('your id', False, 'white')
        self.text_password = text_font.render('your password', False, 'white')
        
        # Button
        self.LOGIN_BUTTON_POS = (50,300)
        self.login_button = Button.OptionButton(self.LOGIN_BUTTON_POS[0],
                                                self.LOGIN_BUTTON_POS[1],
                                                self.login_icon,
                                                0.05,
                                                self.try_login,
                                                )
        
                
    def run(self):
        Game.screen.fill((200, 200, 180))
        
        # Text
        Game.screen.blit(self.text_title, (50,50))
        Game.screen.blit(self.text_id, (50, 150))
        Game.screen.blit(self.text_password, (50,200))
        
        # Button
        self.login_button.draw()
        
        
    
    def try_login(self):
        #need verify procedure
        self.verify = True
        if self.verify:
            self.gameStateManager.set_state('main') # go to main menu
            
        
        
       