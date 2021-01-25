import pygame
import random
import math
from pygame.sprite import Group
from pygame.sprite import Sprite
class Alien(Sprite):
    '''Making a class for alien in python'''
    def __init__(self,screen,setting):
        super(Alien,self).__init__()

        self.image = pygame.image.load('images/ufo.png') 
        self.rect = self.image.get_rect()
        self.screen = screen 
        self.setting = setting
        self.screen_rect =  self.screen.get_rect()
        self.rect.x = random.randint(0,500)
        self.rect.y = random.randint(50,150)
        #positions
        self.speed = 1
        self.speedy = 40
        self.x =float(self.rect.x)
        
    def update(self):   
        self.x = self.x + self.speed
        self.rect.x = self.x
        if self.rect.x >= 736:    
            self.speed = -0.2 
            self.rect.y = self.rect.y + self.speedy
           
        if self.rect.x <= 0:
            self.speed = 0.5
            self.rect.y = self.rect.y + self.speedy
                       
    def blit(self):
        self.screen.blit(self.image,self.rect)
                

    
        