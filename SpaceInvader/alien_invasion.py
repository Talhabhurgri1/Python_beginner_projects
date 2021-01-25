import pygame
#import sys
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from scoreboard import ScoreBoard

def run_game():
    '''
    main method for the game!
         '''
    setting = Settings()
    
    #initiaze and create an game object
    pygame.init()
    #screen
    screen = pygame.display.set_mode((setting.screen_width,setting.screen_height))
    
    ship = Ship(screen,setting)
    
    gf.background_music()
    bullets = Group()
    aliens = Group()
    sb = ScoreBoard(setting,screen)
    #create the fleet of aliens
    gf.create_fleet(aliens,screen,setting)
    
    alien = Alien(screen,setting)
    pygame.display.set_caption('Alien Invasion')
    #start the main loop for the game

    while True:  
        gf.check_events(ship,setting,screen,bullets)
        bullets.update()
        #it helps whatever is in the group it deletes the remaning value so it does not consume more memory
        ship.update(setting)
        #gf.hit(ship,aliens,screen,setting)
        
        gf.update_bullets(bullets,aliens,setting,screen,sb)
        aliens.update()
            
        gf.update_screen(setting,screen,ship,bullets,aliens,sb)
run_game()