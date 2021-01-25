import pygame
import sys
from bullets import Bullet
from alien import Alien
from pygame.sprite import Sprite
from pygame.font import Font
import sys

def check_events(ship,setting,screen,bullets):   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN: 
            check_keydownevents(ship,event,bullets,setting,screen)
        if event.type == pygame.KEYUP:
            check_keyupevents(ship,event)
#check down if person is holding the button or not 
def check_keydownevents(ship,event,bullets,setting,screen):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.right = True
        elif event.key == pygame.K_LEFT:
            ship.left = True
        elif event.key == pygame.K_SPACE:
            fire_bullet(bullets,setting,screen,ship)
#all about releasing a key
def check_keyupevents(ship,event):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.right = False
        elif event.key == pygame.K_LEFT:
            ship.left = False   
#updates the screen
def update_screen(setting,screen,ship,bullets,aliens,bs):
    screen.fill(setting.b_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #this loop will get the alien to display on the screen
    ship.blit() # to display ship on screen    
    aliens.draw(screen)
    bs.show_score()
    if pygame.sprite.spritecollideany(ship, aliens):
        game_over(screen,setting)
        sys.exit()
    pygame.display.flip() #it updates the element on the screen at every frame!

def update_bullets(bullets,aliens,setting,screen,bs):
    '''It updates the bullets and saves the ram space!
    '''
    num = 0
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)

    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        explosion()
        bs.prep_score()
        bs.update_score()
    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet.
        bullets.empty()
        create_fleet(aliens,screen,setting)    
        
def fire_bullet(bullets,setting,screen,ship):
    #methods to fire the bullet up to 3 limit
    if len(bullets) < setting.bullet_allowed:
        new_bullet = Bullet(setting,screen,ship)
        bullets.add(new_bullet)
        print(bullets)
    bullet_music()

def create_fleet(aliens,screen,setting):
    
    for i in range(6):
        alien = Alien(screen,setting)
        aliens.add(alien)

def background_music():
    crash_sound = pygame.mixer.music.load("music/background.wav")
    pygame.mixer.music.play(-1)

def bullet_music():
    bullet = pygame.mixer.Sound('music/laser.wav')
    pygame.mixer.Sound.play(bullet)

def explosion():
    ex = pygame.mixer.Sound('music/explosion.wav')
    pygame.mixer.Sound.play(ex)

def game_over(screen,setting):
    screen_rect = screen.get_rect()
    
    over_text = (30, 30, 30)
    font = pygame.font.SysFont(None, 48)
    over_image = font.render('GAME OVER',True,over_text,setting.b_color)
    over_rect = over_image.get_rect()
    over_rect.center = screen_rect.center    
    screen.blit(over_image,over_rect)




    
