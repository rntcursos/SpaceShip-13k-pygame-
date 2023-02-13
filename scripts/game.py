import pygame
from scripts.animatedbg import AnimatedBg
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *

class Game(Scene):

    def __init__(self):
        super().__init__()

        self.bg = AnimatedBg("assets/menu/bg.png",[0,0],[0,-720],[self.all_sprites])
        self.spaceship = SpaceShip("assets/nave/nave0.png",[600,600],[self.all_sprites])
    
    def update(self):
        self.bg.update()
        self.spaceship.input()
        return super().update()


class SpaceShip(Obj):

    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)

        self.direction = pygame.math.Vector2()
        self.speed = 5

    def input(self):

        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.direction.y = -1
        elif key[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        
        if key[pygame.K_a]:
            self.direction.x = -1
        elif key[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def limit(self):

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > WIDTH - self.image.get_width():
            self.rect.x  = WIDTH - self.image.get_width()
        
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > HEIGHT - self.image.get_height():
            self.rect.y  = HEIGHT - self.image.get_height()

    def move(self):

        self.rect.center += self.direction * self.speed
    
    def update(self):
        self.animation(8,3,"assets/nave/nave")
        self.input()
        self.limit()
        self.move()
       
        
      


