#----------------------------------------------------------------------------
#                       Chapter 11 Homework: Space Invader 
#
#       Created by: Andy
#       Created on: March 11, 2020
#
#----------------------------------------------------------------------------

import pygame, sys
import time

from pygame.locals import *

def main():

    pygame.init()

    #Set the width and height of the screen [width,height]
    size = [800, 600]
    screen = pygame.display.set_mode(size)

    #Define some colors
    BLACK = (0, 0, 0)
    PURPLE = (192, 19, 187)
    BLUE = (18, 229, 226)
    YELLOW = (228, 243, 4)
    ORANGE = (243, 178, 4)
    RED = (250,0,0)

    spaceship = pygame.rect.Rect(350, 500, 50, 50)
    
    alien = pygame.rect.Rect(10, 100, 50, 50)
    alien2 = pygame.rect.Rect(110, 100, 50, 50)
    alien3 = pygame.rect.Rect(210, 100, 50, 50)
    alien4 = pygame.rect.Rect(310, 100, 50, 50)
    alien5 = pygame.rect.Rect(410, 100, 50, 50)

    #Font
    myfont = pygame.font.SysFont("COMIC SANS", 30)
    myfont2 = pygame.font.SysFont("COMIC SANS", 30)

    #Used to manage how fast the screen updates
    fps = 60
    fpsClock = pygame.time.Clock()

    #Before the loop, load the sounds:
    #click_sound = pygame.mixer.Sound("laser5.ogg")

    #Set positions of graphics
    #background_position = [0, 0]
 
    #Load and set up graphics.
    #background_image = pygame.image.load("jnmJ9pp.png").convert()
    #player_image = pygame.image.load("playerShip1_orange.png").convert()
    #player_image.set_colorkey(BLACK)

    #Hide the mouse cursor
    #pygame.mouse.set_visible(0)

    #Speed in pizels per frame
    #xspeed = 5
    #yspeed = 5

    #Main Program Loop
    while True:

        #Event Processing
        for event in pygame.event.get():
            if event.type == QUIT:
                  pygame.quit()
                  sys.exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    spaceship.x -= 10
                   
                elif event.key== pygame.K_RIGHT:
                    spaceship.x +=10
                   
                elif event.key == pygame.K_DOWN:
                    spaceship.y +=10
                    
                elif event.key == pygame.K_UP:
                    spaceship.y -=10
    

    #Score & Life
    #score = 0
    #life = 3
    
        #Redraw the screen
        screen.fill(PURPLE)

        pygame.draw.rect(screen, RED, spaceship)
        pygame.draw.rect(screen, BLUE, alien)
        pygame.draw.rect(screen, BLUE, alien2)
        pygame.draw.rect(screen, BLUE, alien3)
        pygame.draw.rect(screen, BLUE, alien4)
        pygame.draw.rect(screen, BLUE, alien5)

        #Flip screen to display
        pygame.display.flip()

        #Deny it to go fast
        time.sleep(0.05)
    
main()
