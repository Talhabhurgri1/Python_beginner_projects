import pygame
class Ship:
    '''All about ship'''
    def __init__(self,screen,setting):
        
        self.screen = screen
        self.right = False
        self.left = False
        self.setting = setting 
        #loading the ship and get its rect

        self.image = pygame.image.load('D:\Python\Pygame\\alien_invasion\images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #making x and y attribute
        
        #positioning the ship
        self.rect.center = self.screen_rect.center
        self.rect.bottom = self.screen_rect.bottom
        self.center = self.rect.centerx
        
    def update(self,setting):

        #updating the game 
        '''if the ship is at the bottom left or right of screen it will not move or disappear'''        
        if self.right and self.rect.right < self.screen_rect.right:
            self.center = self.center + setting.speed
        
        if self.left and self.rect.left >0 :
            self.center = self.center - setting.speed
        
        self.rect.centerx=self.center 
    #method to display the ship on the screen
        
    def blit(self):
        self.screen.blit(self.image,self.rect)
