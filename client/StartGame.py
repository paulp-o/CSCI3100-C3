import pygame, sys, requests, json
import Game
import Button
import game_arena
import subprocess

class StartGame:
    def __init__(self, display, gameStateManager):
        self.clock = pygame.time.Clock()
        self.loop = True
        
        self.display = display
        self.gameStateManager = gameStateManager
        self.title_font = pygame.font.SysFont("comicsansms", 40)
        self.text_font = pygame.font.SysFont("comicsansms", 22)
        
        # Icon / Image
        self.back_icon = pygame.image.load("Assets/Settings/return.png").convert_alpha()
        
        self.ip_box = pygame.Rect((Game.SCREEN_WIDTH)/2-150,150,100,40)
        self.port_box = pygame.Rect((Game.SCREEN_WIDTH)/2,150,80,40)
        self.color_active = pygame.Color('lightskyblue3')
        self.color_passive = pygame.Color('#10c239')
        self.ip_box_color = self.color_passive
        self.port_box_color = self.color_passive
        
        self.join_box = pygame.Rect((Game.SCREEN_WIDTH)/2-100,250,200,40)
        self.join_box_color = 'white'
        self.host_box = pygame.Rect((Game.SCREEN_WIDTH)/2-100,350,200,40)
        self.host_box_color = 'white'
        
        self.ip_active = False
        self.port_active = False
        
        # Button
        self.back_button = Button.Button(Game.SCREEN_WIDTH - 60, 5, self.back_icon, 0.5)
        self.back_button.action = lambda:   self.gameStateManager.set_state('main'); self.loop = False
        
        # Text
        self.text_title = self.title_font.render('Join / Host Game', False, 'white')
        self.text_ip = self.text_font.render('Enter IP', False, 'white')
        self.text_port = self.text_font.render('Enter Port', False, 'white')
        self.text_join = self.text_font.render('Join', False, 'blue')
        self.text_host = self.text_font.render('Host', False, 'blue')
        self.text_or = self.text_font.render('--------or--------', False, 'white')
        
        # Text on functional buttons
        self.text_join_rect = self.text_join.get_rect()
        self.text_join_rect.center = self.join_box.center
        self.text_host_rect = self.text_host.get_rect()
        self.text_host_rect.center = self.host_box.center
        
        # input text
        self.text_input_ip = ''
        self.text_input_port = ''
        self.text_input_ip_surface = self.text_font.render(self.text_input_ip, True, 'black')
        self.text_input_port_surface = self.text_font.render(self.text_input_port, True, 'black')
        

    def run(self):
        
        Game.screen.fill((200, 200, 180))
        self.back_button.draw()
        
        # Text
        Game.screen.blit(self.text_title, ((Game.SCREEN_WIDTH)/2-180,50))
        Game.screen.blit(self.text_ip, (self.ip_box.x, self.ip_box.y-30))
        Game.screen.blit(self.text_port, (self.port_box.x, self.port_box.y-30))
        Game.screen.blit(self.text_or, ((Game.SCREEN_WIDTH)/2-90,300))
        
        # Button
        
        pygame.draw.rect(Game.screen, self.ip_box_color, self.ip_box)
        pygame.draw.rect(Game.screen, self.port_box_color, self.port_box)
        pygame.draw.rect(Game.screen, self.join_box_color, self.join_box)
        pygame.draw.rect(Game.screen, self.host_box_color, self.host_box)
        
        Game.screen.blit(self.text_input_ip_surface, (self.ip_box.x+5, self.ip_box.y+5))
        Game.screen.blit(self.text_input_port_surface, (self.port_box.x+5, self.port_box.y+5))
        Game.screen.blit(self.text_join, self.text_join_rect)
        Game.screen.blit(self.text_host, self.text_host_rect)
        self.loop = True
        while self.loop:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.ip_box.collidepoint(event.pos):
                        self.ip_active = True
                        self.port_active = False
                    elif self.port_box.collidepoint(event.pos):
                        self.ip_active = False
                        self.port_active = True
                    elif self.join_box.collidepoint(event.pos):
                        # need to verify
                        # subprocess.call(['python', 'game_arena/main.py'])
                        self.gameStateManager.set_state('gameover')
                        self.loop = False
                        result = subprocess.run(['python', 'game_arena/main.py'], capture_output="True", text="True")
                        output = result.stdout
                        process = subprocess.Popen(['python', 'Gameover.py'], stdin=subprocess.PIPE)
                        process.communicate(input=output.encode('utf-8'))
                        
                    elif self.host_box.collidepoint(event.pos):
                        # need to host game
                        self.gameStateManager.set_state('gameover')
                        self.loop = False
                    else:
                        self.ip_active = False
                        self.port_active = False
                
                if event.type == pygame.KEYDOWN:
                    if self.ip_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.text_input_ip = self.text_input_ip[:-1]
                        else:
                            self.text_input_ip += event.unicode
                    elif self.port_active:
                        if event.key == pygame.K_BACKSPACE:
                            self.text_input_port = self.text_input_port[:-1]
                        else:
                            self.text_input_port += event.unicode
            
            if self.ip_active:
                self.ip_box_color = self.color_active
            else:
                self.ip_box_color = self.color_passive
            if self.port_active:
                self.port_box_color = self.color_active
            else:
                self.port_box_color = self.color_passive

            pygame.draw.rect(Game.screen, self.ip_box_color, self.ip_box)
            pygame.draw.rect(Game.screen, self.port_box_color, self.port_box)
            pygame.draw.rect(Game.screen, self.join_box_color, self.join_box)
            pygame.draw.rect(Game.screen, self.host_box_color, self.host_box)
            
            self.text_input_ip_surface = self.text_font.render(self.text_input_ip, True, 'white')
            self.text_input_port_surface = self.text_font.render(self.text_input_port, True, 'white')
            Game.screen.blit(self.text_input_ip_surface, (self.ip_box.x+5, self.ip_box.y+5))
            Game.screen.blit(self.text_input_port_surface, (self.port_box.x+5, self.port_box.y+5))
            Game.screen.blit(self.text_join, self.text_join_rect)
            Game.screen.blit(self.text_host, self.text_host_rect)

            self.ip_box.w = max(100, self.text_input_ip_surface.get_width()+10)
            self.port_box.w = max(100, self.text_input_port_surface.get_width()+10)
            
            pygame.display.flip()
            self.clock.tick(60)   