import pygame
from pygame.font import Font
class Settings():
    
    '''The class to store all the settings
        so we do not have to redo all the work'''
        
    def __init__(self):
        '''Initilize the game settings'''
        
        self.screen_width = 800
        self.screen_height = 600
        self.b_color = (230,230,230)
        self.speed = 1.5
        #bullet

        self.width = 3
        self.height = 15 
        self.speed =1 
        self.bullet_color = 60,60,60
        self.move = False
        self.bullet_allowed = 3

        #alien speed 
        self.alien_speed = 1

        #score 
        self.score = 0
        #ship limit 
        self.ship_limit = 3 

        #game_over 
     
       
       