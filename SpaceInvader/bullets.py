import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    
    def __init__(self,setting,screen,ship):
        super(Bullet,self).__init__()
        self.screen = screen
    

        self.rect = pygame.Rect(0,0,setting.width,setting.height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        self.y = float(self.rect.y)
        
        self.color = setting.bullet_color
        self.speed_factor = setting.speed
    
    #moving the bullet up
    def update(self):
        self.y = self.y - self.speed_factor
        self.rect.y = self.y
    
    #it draws the bullets
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)



    
        
