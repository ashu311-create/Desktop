import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Custom Event Example")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
class Box(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.color = color
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def change_color(self, new_color):
        self.color = new_color
        self.image.fill(new_color)
sprite1 = Box(BLUE, 100, 100, 150, 250)
sprite2 = Box(RED, 100, 100, 500, 250)
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)
CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CHANGE_COLOR:
            sprite1.change_color(GREEN)
            sprite2.change_color(YELLOW)
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()
sys.exit()