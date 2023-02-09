import pygame
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text

class Menu(Scene):

    def __init__(self):
        super().__init__()

        self.bg = Obj("assets/menu/bg.png",[0,0], [self.all_sprites])
        self.bg2 = Obj("assets/menu/bg.png",[0,-720], [self.all_sprites])
        self.title = Text("assets/fonts/airstrike.ttf", 50,"SpaceShip 13k", "white", [450,300])
    
    def update(self):

        self.bg.rect.y += 1
        self.bg2.rect.y += 1

        if self.bg.rect.y > HEIGHT:
            self.bg.rect.y = 0
        elif self.bg2.rect.y == 0:
            self.bg2.rect.y = -HEIGHT

        self.title.draw()
        return super().update()



