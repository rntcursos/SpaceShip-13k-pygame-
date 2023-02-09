import pygame
from scripts.animatedbg import AnimatedBg
from scripts.scene import Scene

class Game(Scene):

    def __init__(self):
        super().__init__()

        self.bg = AnimatedBg("assets/menu/bg.png",[0,0],[0,-720],[self.all_sprites])
    
    def update(self):
        self.bg.update()
        return super().update()