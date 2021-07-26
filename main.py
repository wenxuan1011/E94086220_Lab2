#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import time

WIN_WIDTH = 1024
WIN_HEIGHT = 600
BTN_WIDTH = 80
BTN_HEIGHT = 80
ENEMY_WIDTH=50
ENEMY_HEIGHT=50
HP_WIDTH = 40
HP_HEIGHT = 40
FPS = 30

# color (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# initialization
pygame.init()

# load image (background, enemy, buttons)
background_image = pygame.transform.scale(pygame.image.load("images/Map.png"), (WIN_WIDTH, WIN_HEIGHT))
enemy_image=pygame.transform.scale(pygame.image.load("images/enemy.png"), (ENEMY_WIDTH, ENEMY_HEIGHT))
BTN_pause_image=pygame.transform.scale(pygame.image.load("images/pause.png"),(BTN_WIDTH,BTN_HEIGHT))
BTN_continue_image=pygame.transform.scale(pygame.image.load("images/continue.png"),(BTN_WIDTH,BTN_HEIGHT))
BTN_sound_image=pygame.transform.scale(pygame.image.load("images/sound.png"),(BTN_WIDTH,BTN_HEIGHT))
BTN_muse_image=pygame.transform.scale(pygame.image.load("images/muse.png"),(BTN_WIDTH,BTN_HEIGHT))
HP_image=pygame.transform.scale(pygame.image.load("images/hp.png"),(HP_WIDTH,HP_HEIGHT))
HP_gray_image=pygame.transform.scale(pygame.image.load("images/hp_gray.png"),(HP_WIDTH,HP_HEIGHT))

#clock
clock=pygame.time.Clock()

# set the title
pygame.display.set_caption("My first game")

#set the window
window=pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
   

class Game:
    def __init__(self):
        # hp
        self.hp = 7
        self.max_hp = 10
        pass

    def game_run(self):
        # game loop
        run = True
        while run:
            clock.tick(FPS)
            # event loop
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False

            # draw background
            window.blit(background_image,(0,0))

            # draw enemy and health bar
            window.blit(enemy_image,(30,270))  #draw enemy
            pygame.draw.rect(window,RED,[32,260,45,7])  #graw health bar

            # draw menu (and buttons)
            pygame.draw.rect(window,BLACK,[0,0,WIN_WIDTH,85])
            window.blit(BTN_pause_image,(944,4))
            window.blit(BTN_continue_image,(864,4))
            window.blit(BTN_sound_image,(784,4))
            window.blit(BTN_muse_image,(704,4))
            
            #draw HP
            for i in range(self.max_hp):
                if(i<self.hp):
                    picture=HP_image
                else:
                    picture=HP_gray_image
                if(i<self.max_hp/2):
                    window.blit(picture,(410+i*HP_WIDTH,5))
                else:
                    window.blit(picture,(410+(i-self.max_hp/2)*HP_WIDTH,45))
            
            # draw time (Bonus)
            pygame.draw.rect(window,BLACK,[0,575,52,25])  #draw a black rectangle under the time
            time_count=pygame.time.get_ticks()//1000  #count the second
            time_sec=int(time_count%60)
            time_min=int((time_count/60)%60)
            timeString=str(time_min)+':'+str(time_sec).zfill(2)  #change time into string
            font=pygame.font.Font(None, 22)  #set up the font
            text_surface=font.render(timeString,True,WHITE)  #set up the font, Ture, color
            window.blit(text_surface,(10,580))  #print the word
            
            pygame.display.update()
        pygame.quit()

if __name__ == "__main__":
    covid_game = Game()
    covid_game.game_run()


# In[ ]:




