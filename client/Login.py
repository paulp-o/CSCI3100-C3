import pygame, sys, requests, json
import Game
import Button

domain = '127.0.0.1:8000'

class Login:
    def __init__(self, display, gameStateManager):
        self.clock = pygame.time.Clock()
        self.loop = True
        
        self.display = display
        self.gameStateManager = gameStateManager
        self.text_font = pygame.font.SysFont("comicsansms",22)
        self.title_font = pygame.font.SysFont("comicsansms", 40)  

        # Icon / Image
        self.snake_icon = pygame.image.load("Assets/Login/snake.png").convert_alpha()
        
        self.id_box = pygame.Rect(300,140,100,40)
        self.pwd_box = pygame.Rect(300,190,100,40)
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('#10c239')
        self.id_box_color = self.color_passive
        self.pwd_box_color = self.color_passive
        
        self.login_box = pygame.Rect(50,250,200,40)
        self.login_box_color = 'white'
        self.guest_login_box = pygame.Rect(50,400,200,40)
        self.guest_login_box_color = 'white'
        self.register_box = pygame.Rect(50, 550, 200, 40)
        self.register_box_color = 'white'
        
        self.id_active = False
        self.pwd_active = False
        
        # Text
        self.text_title = self.title_font.render('Login', False, '#10c239')
        self.text_id = self.text_font.render('Enter your id', False, '#10c239')
        self.text_password = self.text_font.render('Enter your password', False, '#10c239')
        self.text_guest = self.text_font.render('Play as a guest', False, '#10c239')
        self.text_login = self.text_font.render('login',False,'#10c239')
        self.text_guest_login = self.text_font.render('guest login',False,'#10c239')
        self.text_register = self.text_font.render('register',False,'#10c239')
        
        # Text on functional buttons
        self.text_login_rect = self.text_login.get_rect()
        self.text_login_rect.center = self.login_box.center
        self.text_guest_login_rect = self.text_guest_login.get_rect()
        self.text_guest_login_rect.center = self.guest_login_box.center
        self.text_register_rect = self.text_register.get_rect()
        self.text_register_rect.center = self.register_box.center
        
        # input text
        self.text_input_id = ''
        self.text_input_pwd = ''
        self.text_input_id_surface = self.text_font.render(self.text_input_id, True, (255,255,255))
        self.text_input_pwd_surface = self.text_font.render(self.text_input_pwd, True, (255,255,255))
        
        # Button
        
                
    def run(self):
        self.loop = True
        Game.screen.fill((200, 200, 180))
        self.draw_check_pattern()
        self.snake_icon.set_colorkey((255, 255, 255))
        Game.screen.blit(self.snake_icon, ((Game.SCREEN_WIDTH)/2, (Game.SCREEN_HEIGHT)/2-100))
        
        # Text
        Game.screen.blit(self.text_title, (50,50))
        Game.screen.blit(self.text_id, (50, 150))
        Game.screen.blit(self.text_password, (50,200))
        Game.screen.blit(self.text_guest, (50,360))
            
            
        # Button

        pygame.draw.rect(Game.screen,self.id_box_color,self.id_box)
        pygame.draw.rect(Game.screen,self.pwd_box_color,self.pwd_box)
        pygame.draw.rect(Game.screen,self.login_box_color,self.login_box)
        pygame.draw.rect(Game.screen,self.guest_login_box_color,self.guest_login_box)
        pygame.draw.rect(Game.screen,self.register_box_color,self.register_box)
            
        Game.screen.blit(self.text_input_id_surface, (self.id_box.x+5,self.id_box.y+5))
        Game.screen.blit(self.text_input_pwd_surface, (self.pwd_box.x+5,self.pwd_box.y+5))
        Game.screen.blit(self.text_login, self.text_login_rect)
        Game.screen.blit(self.text_guest_login, self.text_guest_login_rect)
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
                    elif self.pwd_box.collidepoint(event.pos):
                        self.id_active = False
                        self.pwd_active = True
                    elif self.login_box.collidepoint(event.pos):
                        # need verification method, currently no verification
                        if self.try_login() == True:
                            self.gameStateManager.set_state('main')
                            self.loop = False
                        else:
                            self.text_input_id = ''
                            self.text_input_pwd = ''
                            
                    elif self.guest_login_box.collidepoint(event.pos):
                        self.try_guest_login()
                        self.loop = False
                    elif self.register_box.collidepoint(event.pos):
                        self.gameStateManager.set_state('register')
                        self.loop = False
                    else:
                        self.id_active = False
                        self.pwd_active = False
                
                if event.type == pygame.KEYDOWN:
                    if self.id_active == True:
                        if event.key == pygame.K_BACKSPACE:
                            self.text_input_id = self.text_input_id[0:-1]
                        else:
                            self.text_input_id += event.unicode
                    elif self.pwd_active == True:
                        if event.key == pygame.K_BACKSPACE:
                            self.text_input_pwd = self.text_input_pwd[0:-1]
                        else:
                            self.text_input_pwd += event.unicode  
            
            if self.id_active:
                self.id_box_color = self.color_active
            else:
                self.id_box_color = self.color_passive
            
            if self.pwd_active:
                self.pwd_box_color = self.color_active
            else:
                self.pwd_box_color = self.color_passive
            
            pygame.draw.rect(Game.screen,self.id_box_color,self.id_box)
            pygame.draw.rect(Game.screen,self.pwd_box_color,self.pwd_box)
            pygame.draw.rect(Game.screen,self.login_box_color,self.login_box)
            pygame.draw.rect(Game.screen,self.guest_login_box_color,self.guest_login_box)
            pygame.draw.rect(Game.screen,self.register_box_color,self.register_box)
            
            self.text_input_id_surface = self.text_font.render(self.text_input_id, True, (255,255,255))
            self.text_input_pwd_surface = self.text_font.render(self.text_input_pwd, True, (255,255,255))
            Game.screen.blit(self.text_input_id_surface, (self.id_box.x+5,self.id_box.y+5))
            Game.screen.blit(self.text_input_pwd_surface, (self.pwd_box.x+5,self.pwd_box.y+5))
            Game.screen.blit(self.text_login, self.text_login_rect)
            Game.screen.blit(self.text_guest_login, self.text_guest_login_rect)
            Game.screen.blit(self.text_register, self.text_register_rect)
            
            self.id_box.w = max (100, self.text_input_id_surface.get_width() + 10)
            self.pwd_box.w = max (100, self.text_input_pwd_surface.get_width() + 10)

            pygame.display.flip()
            self.clock.tick(60)    
        
                
    
    def try_login(self):
        # need verify procedure
        url = 'http://{}/api/auth/login/'.format(domain)
        h = {}
        d = {'username': self.text_input_id, 'password': self.text_input_pwd} # {'username': id, 'password': pwd}
        res = requests.post(url, json=d, headers=h )
        try:
            if "token" in res.json():
                return True
            else:
                return False
        except ValueError:
            # Handle the case when the response is not valid JSON
            return False
        
    def try_guest_login(self):
        self.gameStateManager.set_state('main') # go to main menu
        
    def draw_check_pattern(self):
        # Draw a check pattern with green and red colors
        for x in range(0, Game.SCREEN_WIDTH, 70):
            for y in range(0, Game.SCREEN_HEIGHT, 70):
                if (x // 70) % 2 == (y // 70) % 2:
                    pygame.draw.rect(Game.screen, '#eff2d8' , (x, y, 70, 70))
                else:
                    pygame.draw.rect(Game.screen, '#e4ebb2', (x, y, 70, 70))