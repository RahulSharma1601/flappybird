import pygame as pg
from random import randint

class Pipe:
    def __init__(self,scale_factor,move_speed):
        self.img_up=pg.transform.scale_by(pg.image.load("galley/pipeup.png").convert_alpha(),scale_factor)
        self.img_up=pg.transform.scale_by(pg.image.load("galley/pipedown.png").convert_alpha(),scale_factor)
        self.rect_up=self.img_up.get_rect()
        self.rect_down=self.img_down.get_rect()
        self.pipe_distance=100

        self.rect_up.y=randint(100,400)
        self.rect_up.x=600
        self.rect_down.y=self.rect_up.y-self.pipe_distance-self.rect_up.height
        self.rect_down.x=600
        self.move_speed=move_speed

    def drawpipe(self,win):
        win.blit(self.img_up,self.rect_up)
        win.blit(self.img_down,self.rect_down)

    def update(self,dt):
        self.rect_up.x-=self.move_speed*dt
        self.rect_down.x-=self.move_speed*dt


