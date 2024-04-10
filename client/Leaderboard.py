import pygame, sys, requests, json
import Game
import Button

class Leaderboard:
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
        title_font = pygame.font.Font(None, 50)
        text_font = pygame.font.Font(None, 35)
        
        # Icon / Image
        self.back_icon = pygame.image.load("Assets/Settings/return.png").convert_alpha()
        
        self.color_rank_1 =pygame.Color('gold')
        self.color_rank_2 =pygame.Color('silver')
        self.color_rank_3 =pygame.Color('copper')
        self.color_rank_rest =pygame.Color('gray')
        
        # rect for ranking
        self.rect_rank_1 = pygame.Rect(50,100,40,40)
        self.rect_rank_2 = pygame.Rect(50,150,40,40)
        self.rect_rank_3 = pygame.Rect(50,200,40,40)
        self.rect_rank_4 = pygame.Rect(50,250,40,40)
        self.rect_rank_5 = pygame.Rect(50,300,40,40)
        self.rect_rank_6 = pygame.Rect(50,350,40,40)
        self.rect_rank_7 = pygame.Rect(50,400,40,40)
        self.rect_rank_8 = pygame.Rect(50,450,40,40)
        self.rect_rank_9 = pygame.Rect(50,500,40,40)
        self.rect_rank_10 = pygame.Rect(50,550,40,40)
        
        # rect for username
        self.rect_id_1 = pygame.Rect(100,100,100,40)
        self.rect_id_2 = pygame.Rect(100,150,100,40)
        self.rect_id_3 = pygame.Rect(100,200,100,40)
        self.rect_id_4 = pygame.Rect(100,250,100,40)
        self.rect_id_5 = pygame.Rect(100,300,100,40)
        self.rect_id_6 = pygame.Rect(100,350,100,40)
        self.rect_id_7 = pygame.Rect(100,400,100,40)
        self.rect_id_8 = pygame.Rect(100,450,100,40)
        self.rect_id_9 = pygame.Rect(100,500,100,40)
        self.rect_id_10 = pygame.Rect(100,550,100,40)
        
        # rect for score
        self.rect_score_1 = pygame.Rect(210,100,70,40)
        self.rect_score_2 = pygame.Rect(210,150,70,40)
        self.rect_score_3 = pygame.Rect(210,200,70,40)
        self.rect_score_4 = pygame.Rect(210,250,70,40)
        self.rect_score_5 = pygame.Rect(210,300,70,40)
        self.rect_score_6 = pygame.Rect(210,350,70,40)
        self.rect_score_7 = pygame.Rect(210,400,70,40)
        self.rect_score_8 = pygame.Rect(210,450,70,40)
        self.rect_score_9 = pygame.Rect(210,500,70,40)
        self.rect_score_10 = pygame.Rect(210,550,70,40)
        
        
        
        # Button
        self.back_button = Button.Button(Game.SCREEN_WIDTH - 60, 5, self.back_icon, 0.5)
        
        # Text
        self.title_customization = title_font.render('Leaderboard', False, 'white')
        
        self.text_rank_1 = text_font.render('1', False, 'white')        
        self.text_rank_1_rect = self.text_rank_1.get_rect()
        self.text_rank_1_rect.center = self.rect_rank_1.center
        self.text_rank_2 = text_font.render('2', False, 'white')        
        self.text_rank_2_rect = self.text_rank_2.get_rect()
        self.text_rank_2_rect.center = self.rect_rank_2.center
        self.text_rank_3 = text_font.render('3', False, 'white')        
        self.text_rank_3_rect = self.text_rank_3.get_rect()
        self.text_rank_3_rect.center = self.rect_rank_3.center
        self.text_rank_4 = text_font.render('4', False, 'white')        
        self.text_rank_4_rect = self.text_rank_4.get_rect()
        self.text_rank_4_rect.center = self.rect_rank_4.center
        self.text_rank_5 = text_font.render('5', False, 'white')        
        self.text_rank_5_rect = self.text_rank_5.get_rect()
        self.text_rank_5_rect.center = self.rect_rank_5.center
        self.text_rank_6 = text_font.render('6', False, 'white')        
        self.text_rank_6_rect = self.text_rank_6.get_rect()
        self.text_rank_6_rect.center = self.rect_rank_6.center
        self.text_rank_7 = text_font.render('7', False, 'white')        
        self.text_rank_7_rect = self.text_rank_7.get_rect()
        self.text_rank_7_rect.center = self.rect_rank_7.center
        self.text_rank_8 = text_font.render('8', False, 'white')        
        self.text_rank_8_rect = self.text_rank_8.get_rect()
        self.text_rank_8_rect.center = self.rect_rank_8.center
        self.text_rank_9 = text_font.render('9', False, 'white')        
        self.text_rank_9_rect = self.text_rank_1.get_rect()
        self.text_rank_9_rect.center = self.rect_rank_9.center
        self.text_rank_10 = text_font.render('10', False, 'white')        
        self.text_rank_10_rect = self.text_rank_10.get_rect()
        self.text_rank_10_rect.center = self.rect_rank_10.center
        
        
        # Button action
        self.back_button.action = lambda: self.gameStateManager.set_state('main')
        
        
    def run(self):
        Game.screen.fill((200, 200, 180))
        
        self.back_button.draw()
        
        # draw rank box
        pygame.draw.rect(Game.screen, self.color_rank_1, self.rect_rank_1)
        pygame.draw.rect(Game.screen, self.color_rank_2, self.rect_rank_2)
        pygame.draw.rect(Game.screen, self.color_rank_3, self.rect_rank_3)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_rank_4)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_rank_5)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_rank_6)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_rank_7)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_rank_8)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_rank_9)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_rank_10)
        
        # draw rank num in rank box
        Game.screen.blit(self.text_rank_1, self.text_rank_1_rect)
        Game.screen.blit(self.text_rank_2, self.text_rank_2_rect)
        Game.screen.blit(self.text_rank_3, self.text_rank_3_rect)
        Game.screen.blit(self.text_rank_4, self.text_rank_4_rect)
        Game.screen.blit(self.text_rank_5, self.text_rank_5_rect)
        Game.screen.blit(self.text_rank_6, self.text_rank_6_rect)
        Game.screen.blit(self.text_rank_7, self.text_rank_7_rect)
        Game.screen.blit(self.text_rank_8, self.text_rank_8_rect)
        Game.screen.blit(self.text_rank_9, self.text_rank_9_rect)
        Game.screen.blit(self.text_rank_10, self.text_rank_10_rect)