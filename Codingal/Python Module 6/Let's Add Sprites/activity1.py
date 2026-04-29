import pygame
import random
pygame.init()
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT+1
BACKGROUD_COLOR_CHANGE_EVENT = pygame.USEREVENT+2
BLUE=pygame.Color('blue')
LIGHTBLUE=pygame.Color('lightblue')
DARKBLUE=pygame.Color('doarkblue')
YELLOW=pygame.Color('yellow')
MAGENTA=pygame.Color('magenta')
ORANGE=pygame.Color('orange')
WHITE=pygame.Color('white')
class Sprite (pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super ().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]), random.choice([-1,1])]
    def update(self):
        self.rect.move.ip(self.velocity)
        