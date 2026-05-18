import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sprite Movement Example")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def move(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change
player1 = Player(BLUE, 60, 60, 100, 100)
player2 = Player(RED, 60, 60, 500, 300)
all_sprites = pygame.sprite.Group()
all_sprites.add(player1)
all_sprites.add(player2)
running = True
while running:
    screen.fill(WHITE)
    x_change = 0
    y_change = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_change = -5
    if keys[pygame.K_RIGHT]:
        x_change = 5
    if keys[pygame.K_UP]:
        y_change = -5
    if keys[pygame.K_DOWN]:
        y_change = 5
    player1.move(x_change, y_change)
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()
sys.exit()