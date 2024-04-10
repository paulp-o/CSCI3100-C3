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
        self.color_rank_2 =pygame.Color('azure2')
        self.color_rank_3 =pygame.Color('burlywood2')
        self.color_rank_rest =pygame.Color('azure3')
        self.color_user =pygame.Color('white')
        
        # rect for ranking
        self.rect_rank_1 = pygame.Rect((Game.SCREEN_WIDTH)/2-110,30,40,40)
        self.rect_rank_2 = pygame.Rect((Game.SCREEN_WIDTH)/2-110,80,40,40)
        self.rect_rank_3 = pygame.Rect((Game.SCREEN_WIDTH)/2-110,130,40,40)
        self.rect_rank_4 = pygame.Rect((Game.SCREEN_WIDTH)/2-110,180,40,40)
        self.rect_rank_5 = pygame.Rect((Game.SCREEN_WIDTH)/2-110,230,40,40)
        self.rect_rank_6 = pygame.Rect((Game.SCREEN_WIDTH)/2-110,280,40,40)
        self.rect_rank_7 = pygame.Rect((Game.SCREEN_WIDTH)/2-110,330,40,40)
        self.rect_rank_8 = pygame.Rect((Game.SCREEN_WIDTH)/2-110,380,40,40)
        self.rect_rank_9 = pygame.Rect((Game.SCREEN_WIDTH)/2-110,430,40,40)
        self.rect_rank_10 = pygame.Rect((Game.SCREEN_WIDTH)/2-110,480,40,40)
        self.rect_rank_user = pygame.Rect((Game.SCREEN_WIDTH)/2-110,530,40,40)
        
        # rect for username
        self.rect_id_1 = pygame.Rect((Game.SCREEN_WIDTH)/2-60,30,100,40)
        self.rect_id_2 = pygame.Rect((Game.SCREEN_WIDTH)/2-60,80,100,40)
        self.rect_id_3 = pygame.Rect((Game.SCREEN_WIDTH)/2-60,130,100,40)
        self.rect_id_4 = pygame.Rect((Game.SCREEN_WIDTH)/2-60,180,100,40)
        self.rect_id_5 = pygame.Rect((Game.SCREEN_WIDTH)/2-60,230,100,40)
        self.rect_id_6 = pygame.Rect((Game.SCREEN_WIDTH)/2-60,280,100,40)
        self.rect_id_7 = pygame.Rect((Game.SCREEN_WIDTH)/2-60,330,100,40)
        self.rect_id_8 = pygame.Rect((Game.SCREEN_WIDTH)/2-60,380,100,40)
        self.rect_id_9 = pygame.Rect((Game.SCREEN_WIDTH)/2-60,430,100,40)
        self.rect_id_10 = pygame.Rect((Game.SCREEN_WIDTH)/2-60,480,100,40)
        self.rect_id_user = pygame.Rect((Game.SCREEN_WIDTH)/2-60,530,100,40)
        
        # rect for score
        self.rect_score_1 = pygame.Rect((Game.SCREEN_WIDTH)/2+50,30,70,40)
        self.rect_score_2 = pygame.Rect((Game.SCREEN_WIDTH)/2+50,80,70,40)
        self.rect_score_3 = pygame.Rect((Game.SCREEN_WIDTH)/2+50,130,70,40)
        self.rect_score_4 = pygame.Rect((Game.SCREEN_WIDTH)/2+50,180,70,40)
        self.rect_score_5 = pygame.Rect((Game.SCREEN_WIDTH)/2+50,230,70,40)
        self.rect_score_6 = pygame.Rect((Game.SCREEN_WIDTH)/2+50,280,70,40)
        self.rect_score_7 = pygame.Rect((Game.SCREEN_WIDTH)/2+50,330,70,40)
        self.rect_score_8 = pygame.Rect((Game.SCREEN_WIDTH)/2+50,380,70,40)
        self.rect_score_9 = pygame.Rect((Game.SCREEN_WIDTH)/2+50,430,70,40)
        self.rect_score_10 = pygame.Rect((Game.SCREEN_WIDTH)/2+50,480,70,40)
        self.rect_score_user = pygame.Rect((Game.SCREEN_WIDTH)/2+50,530,70,40)
        
        
        # Button
        self.back_button = Button.Button(Game.SCREEN_WIDTH - 60, 5, self.back_icon, 0.5)
        
        # Text
        self.rect_title = pygame.Rect(20,10,200,40)
        self.title_leaderboard = title_font.render('Leaderboard', False, 'white')
        self.title_leaderboard_rect = self.title_leaderboard.get_rect()
        self.title_leaderboard_rect.center = self.rect_title.center
        
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
        self.text_rank_user = text_font.render('Me', False, 'black')        
        self.text_rank_user_rect = self.text_rank_user.get_rect()
        self.text_rank_user_rect.center = self.rect_rank_user.center
        
        
        # Button action
        self.back_button.action = lambda: self.gameStateManager.set_state('main')
        
        
    def run(self):
        Game.screen.fill((200, 200, 180))
        
        self.back_button.draw()
        
        Game.screen.blit(self.title_leaderboard, self.title_leaderboard_rect)
        
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
        pygame.draw.rect(Game.screen, self.color_user, self.rect_rank_user)
        
        # draw id box
        pygame.draw.rect(Game.screen, self.color_rank_1, self.rect_id_1)
        pygame.draw.rect(Game.screen, self.color_rank_2, self.rect_id_2)
        pygame.draw.rect(Game.screen, self.color_rank_3, self.rect_id_3)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_id_4)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_id_5)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_id_6)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_id_7)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_id_8)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_id_9)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_id_10)
        pygame.draw.rect(Game.screen, self.color_user, self.rect_id_user)
        
        # draw score box
        pygame.draw.rect(Game.screen, self.color_rank_1, self.rect_score_1)
        pygame.draw.rect(Game.screen, self.color_rank_2, self.rect_score_2)
        pygame.draw.rect(Game.screen, self.color_rank_3, self.rect_score_3)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_score_4)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_score_5)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_score_6)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_score_7)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_score_8)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_score_9)
        pygame.draw.rect(Game.screen, self.color_rank_rest, self.rect_score_10)
        pygame.draw.rect(Game.screen, self.color_user, self.rect_score_user)
        
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
        Game.screen.blit(self.text_rank_user, self.text_rank_user_rect)