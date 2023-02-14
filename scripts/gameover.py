import pygame
from scripts.animatedbg import AnimatedBg
from scripts.scene import Scene
from scripts.text import Text


class GameOver(Scene):

    def __init__(self):
        super().__init__()

        self.bg = AnimatedBg("assets/menu/bg.png",[0,0],[0,-720],[self.all_sprites])
        self.title = Text("assets/fonts/airstrike.ttf", 50,"GameOver", "white", [501,350])
    
    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False
        return super().events(event)

    def update(self):

        self.bg.update()
        self.title.drawFade()
        return super().update()