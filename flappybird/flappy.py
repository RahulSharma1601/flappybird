import pygame as pg
import sys,time
from bird import Bird
from pipe import Pipe
pg.init()

class game:
    def __init__(self):
        self.width=600
        self.height=768
        self.scale_factor=1.5
        self.birdscale_factor=0.1
        self.win=pg.display.set_mode((self.width,self.height))
        self.clock=pg.time.Clock()
        self.move_speed=250
        self.bird=Bird(self.birdscale_factor)
        self.is_enter_pressed=False
        self.pipes=[]
        self.pipe_generate_counter=71
        self.setupbackground()
         
        self.gameLoop()



    def gameLoop(self):
        last_time=time.time()
        while True:
            new_time=time.time()
            dt=new_time-last_time
            last_time=new_time

            for event in pg.event.get():
                if event.type==pg.QUIT:
                    pg.quit()     
                    sys.exit()
                if event.type==pg.KEYDOWN:
                    if event.key==pg.K_RETURN:
                        self.is_enter_pressed=True
                    if event.key==pg.K_SPACE and self.is_enter_pressed :
                        self.bird.flap(dt)

            self.updateEverything(dt)
            self.drowimages()
            pg.display.update()
            self.clock.tick(60)

    def updateEverything(self,dt):
        if self.is_enter_pressed:

            self.ground1_rect.x-=int(self.move_speed*dt)
            self.ground2_rect.x-=int(self.move_speed*dt)

            if self.ground1_rect.right<0:
                self.ground1_rect.x=self.ground2_rect.right
            if self.ground2_rect.right<0:
                self.ground2_rect.x=self.ground1_rect.right

            if self.pipe_generate_counter>70:
                self.pipes.append(Pipe(self.scale_factor,self.move_speed))
                self.pipe_generate_counter=0
            self.pipe_generate_counter+=1

            for pipe in self,pipes:
                pipe.update(dt)
            self.bird.update(dt)

    def drowimages(self):
        self.win.blit(self.bg_img,(0,-300))
        for pipe in self.pipes :
            pipe.drawpipe(self.win)
        self.win.blit(self.ground1_img,self.ground1_rect)
        self.win.blit(self.ground2_img,self.ground2_rect)
        self.win.blit(self.bird.image,self.bird.rect)
        
    def setupbackground(self):
        self.bg_img=pg.transform.scale(pg.image.load("gallery/background1.png").convert(),(600,1066))
        self.ground1_img=pg.transform.scale_by(pg.image.load("gallery/base.png").convert(),self.scale_factor)
        self.ground2_img=pg.transform.scale_by(pg.image.load("gallery/base.png").convert(),self.scale_factor)

        self.ground1_rect=self.ground1_img.get_rect()
        self.ground2_rect=self.ground2_img.get_rect()

        self.ground1_rect.x=0
        self.ground2_rect.x=self.ground1_rect.right
        self.ground1_rect.y=568
        self.ground2_rect.y=568 

Game=game()