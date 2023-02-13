import pygame
from scripts.animatedbg import AnimatedBg
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *
from scripts.text import Text

class Menu(Scene):

    def __init__(self):
        super().__init__()

        self.bg = AnimatedBg("assets/menu/bg.png",[0,0],[0,-720],[self.all_sprites])
        self.title = Text("assets/fonts/airstrike.ttf", 50,"SpaceShip 13k", "white", [448,288])
        self.text_info = Text("assets/fonts/airstrike.ttf", 21,"Press Start To Play", "white", [508,513])
    
    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False
        return super().events(event)

    def update(self):

        self.bg.update()
        self.title.draw()
        self.text_info.drawFade()
        return super().update()




