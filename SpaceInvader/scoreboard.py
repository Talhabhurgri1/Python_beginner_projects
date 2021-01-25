import pygame
class ScoreBoard:
    def __init__(self,setting,screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.setting = setting 
        self.score = self.setting.score
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        self.prep_score()

    def prep_score(self):
        score_str = str(self.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.setting.b_color)

        #position for the score 
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
    
    def update_score(self):
        self.score = self.score + 10

    
