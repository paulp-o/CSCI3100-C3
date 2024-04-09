import pygame, sys
import Game
import Button

button_blue = pygame.transform.scale(pygame.image.load('Assets/Settings/settingbutton_blue.png'), (320, 60))


base_font = pygame.font.Font(None,32)
user_id = ''
user_password = ''
id_rect = pygame.Rect(330, 90, 140, 32)
password_rect = pygame.Rect(330, 130, 140, 32)

color_active = pygame.Color("white")
color_passive = pygame.Color("gray15")
color_id = color_passive
color_password = color_passive

active_id = False
active_password = False

class Login:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        self.background = pygame.image.load('Assets/Main Menu/background.jpg')
        title_font = pygame.font.Font(None, 120)  
        
        self.text_login = title_font.render('Login', False, 'white')
        
        self.text_verify = base_font.render('Register', False, 'white')
        self.verify_button = Button.Button(330, 180, button_blue, 1, self.try_login)
        
    def run(self):
         
        Game.screen.blit(self.background, (0, 0))
        Game.screen.blit(self.text_login, (330, 30))
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if id_rect.collidepoint(event.pos):
                        active_id = True
                    else:
                        active_id = False
                    
                    if password_rect.collidepoint(event.pos):
                        active_password = True
                    else:
                        active_password = False
                    
                    if event.type == pygame.KEYDOWN:
                        if active_id == True:
                            if event.key == pygame.K_BACKSPACE:
                                user_id = user_id[0:-1]
                            else:
                                user_id += event.unicode
                        elif active_password == True:
                            if event.key == pygame.K_BACKSPACE:
                                user_password = user_id[0:-1]
                            else:
                                user_password += event.unicode
            if active_id:
                color_id = color_active
            else:
                color_id = color_passive
            if active_password:
                color_password = color_active
            else:
                color_password = color_passive 
            
            Game.screen.blit(id_rect, (330, 90))
            Game.screen.blit(password_rect, (330, 130))
            
            id_surface = base_font.render(user_id,True,(255,255,255))
            password_surface = base_font.render(user_password,True,(255,255,255))
            
            Game.screen.blit(id_surface, (id_rect.x + 5, id_rect.y + 5))
            Game.screen.blit(password_surface, (password_rect.x + 5, password_rect.y + 5))
            
            id_rect.w = max (100, id_surface.get_width()+10)
            password_rect.w = max (100, password_surface.get_width()+10)

            pygame.display.flip()
        
        if self.verify_button.back():
            self.verify_button.action()
        
    
    def try_login(self):
        #need verify procedure
        if True:
            self.gameStateManager.set_state('main')
            