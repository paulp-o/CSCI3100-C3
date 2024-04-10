import pygame, sys, requests, json
import Game
import Button

domain = '127.0.0.1:8000'

class Register:
    def __init__(self, display, gameStateManager):
        self.clock = pygame.time.Clock()
        self.loop = True
        
        self.display = display
        self.gameStateManager = gameStateManager
        self.text_font = pygame.font.Font(None,32)
        self.title_font = pygame.font.Font(None, 60) 
        
        # Icon / Image
        self.back_icon = pygame.image.load("Assets/Settings/return.png").convert_alpha()
        
        self.id_box = pygame.Rect(300,140,100,40)
        self.pwd_box = pygame.Rect(300,190,100,40)
        self.confirm_pwd_box = pygame.Rect(300,240,100,40)
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('gray15')
        self.id_box_color = self.color_passive
        self.pwd_box_color = self.color_passive
        self.confirm_pwd_box_color = self.color_passive
        
        self.register_box = pygame.Rect(50,300,200,40)
        self.register_box_color = 'white'
        self.back_to_login_box = pygame.Rect(50, 450, 200, 40)
        self.back_to_login_box_color = 'white'
        
        self.id_active = False
        self.pwd_active = False
        self.confirm_pwd_active = False
        
        # Button
        self.back_button = Button.Button(Game.SCREEN_WIDTH - 60, 5, self.back_icon, 0.5)
        self.back_button.action = lambda:   self.gameStateManager.set_state('login'); self.loop = False
        
        # Text
        self.text_title = self.title_font.render('Register', False, 'white')
        self.text_id = self.text_font.render('Enter your id', False, 'white')
        self.text_pwd = self.text_font.render('Enter your password', False, 'white')
        self.text_confirm_pwd = self.text_font.render('Confirm your password', False, 'white')
        self.text_register = self.text_font.render('register', False, 'black')
        
        # Text on functional buttons
        self.text_register_rect = self.text_register.get_rect()
        self.text_register_rect.center = self.register_box.center
        
        # input text
        self.text_input_id = ''
        self.text_input_pwd = ''
        self.text_input_confirm_pwd = ''
        self.text_input_id_surface = self.text_font.render(self.text_input_id, True, 'white')
        self.text_input_pwd_surface = self.text_font.render(self.text_input_pwd, False, 'white')
        self.text_input_confirm_pwd_surface = self.text_font.render(self.text_input_confirm_pwd, False, 'white')
        
        
    def run(self):
        
        Game.screen.fill((200, 200, 180))
        self.back_button.draw()
        
        # Text
        Game.screen.blit(self.text_title, (50,50))
        Game.screen.blit(self.text_id, (50, 150))
        Game.screen.blit(self.text_pwd, (50,200))
        Game.screen.blit(self.text_confirm_pwd, (50,250))
        
        # Button
        
        pygame.draw.rect(Game.screen,self.id_box_color,self.id_box)
        pygame.draw.rect(Game.screen,self.pwd_box_color,self.pwd_box)
        pygame.draw.rect(Game.screen,self.confirm_pwd_box_color,self.confirm_pwd_box)
        pygame.draw.rect(Game.screen,self.register_box_color,self.register_box)
        
        Game.screen.blit(self.text_input_id_surface, (self.id_box.x+5, self.id_box.y+5))
        Game.screen.blit(self.text_input_pwd_surface, (self.pwd_box.x+5, self.pwd_box.y+5))
        Game.screen.blit(self.text_input_confirm_pwd_surface, (self.confirm_pwd_box.x+5, self.confirm_pwd_box.y+5))
        Game.screen.blit(self.text_register, self.text_register_rect)
            
        while self.loop:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.id_box.collidepoint(event.pos):
                        self.id_active = True
                        self.pwd_active = False
                        self.confirm_pwd_active = False
                    elif self.pwd_box.collidepoint(event.pos):
                        self.id_active = False
                        self.pwd_active = True
                        self.confirm_pwd_active = False
                    elif self.confirm_pwd_box.collidepoint(event.pos):
                        self.id_active = False
                        self.pwd_active = False
                        self.confirm_pwd_active = True
                    elif self.register_box.collidepoint(event.pos):
                        if self.try_register():
                            self.gameStateManager.change_state('login')
                            self.loop = False
                        else:
                            self.text_input_id = ''
                            self.text_input_pwd = ''
                            self.text_input_confirm_pwd = ''
                    else:
                        self.id_active = False
                        self.pwd_active = False
                        self.confirm_pwd_active = False
                
                if event.type == pygame.KEYDOWN:
                    if self.id_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.text_input_id = self.text_input_id[:-1]
                        else:
                            self.text_input_id += event.unicode
                    elif self.pwd_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.text_input_pwd = self.text_input_pwd[:-1]
                        else:
                            self.text_input_pwd += event.unicode
                        
                    elif self.confirm_pwd_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.text_input_confirm_pwd = self.text_input_confirm_pwd[:-1]
                        else:
                            self.text_input_confirm_pwd += event.unicode
            
            if self.id_active:
                self.id_box_color = self.color_active
            else:
                self.id_box_color = self.color_passive
            if self.pwd_active:
                self.pwd_box_color = self.color_active
            else:
                self.pwd_box_color = self.color_passive
            if self.confirm_pwd_active:
                self.confirm_pwd_box_color = self.color_active
            else:
                self.confirm_pwd_box_color = self.color_passive
        
            pygame.draw.rect(Game.screen,self.id_box_color,self.id_box)
            pygame.draw.rect(Game.screen,self.pwd_box_color,self.pwd_box)
            pygame.draw.rect(Game.screen,self.confirm_pwd_box_color,self.confirm_pwd_box)
            pygame.draw.rect(Game.screen,self.register_box_color,self.register_box)
            
            self.text_input_id_surface = self.text_font.render(self.text_input_id, True, 'white')
            self.text_input_pwd_surface = self.text_font.render(self.text_input_pwd, True, 'white')
            self.text_input_confirm_pwd_surface = self.text_font.render(self.text_input_confirm_pwd, True, 'white')
            Game.screen.blit(self.text_input_id_surface, (self.id_box.x+5, self.id_box.y+5))
            Game.screen.blit(self.text_input_pwd_surface, (self.pwd_box.x+5, self.pwd_box.y+5))
            Game.screen.blit(self.text_input_confirm_pwd_surface, (self.confirm_pwd_box.x+5, self.confirm_pwd_box.y+5))
            Game.screen.blit(self.text_register, self.text_register_rect)
            
            self.id_box.w = max (100, self.text_input_id_surface.get_width()+10)
            self.pwd_box.w = max (100, self.text_input_pwd_surface.get_width()+10)
            self.confirm_pwd_box.w = max (100, self.text_input_confirm_pwd_surface.get_width()+10)
            
            pygame.display.flip()
            self.clock.tick(60)

    
    def try_register(self):
        if self.text_input_id == '':
            return False
        if self.text_input_pwd == '':
            return False
        if self.text_input_confirm_pwd == '':
            return False
        if self.text_input_pwd != self.text_input_confirm_pwd:
            return False
        
        url = 'http://{}/api/auth/register/'.format(domain)
        h = {}
        d = {'username': self.text_input_id, 'password': self.text_input_pwd}
        res = requests.post(url, json=d, headers=h )
        try:
            if "username" in res.json():
                return True
            else:
                return False
        except ValueError:
            # Handle the case when the response is not valid JSON
            return False
        
        