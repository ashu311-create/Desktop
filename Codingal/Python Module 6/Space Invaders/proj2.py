import pygame
import random
import sys
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Collision Game")
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
player_image = pygame.image.load("player.png")
player_image = pygame.transform.scale(player_image, (50, 50))
enemy_image = pygame.image.load("enemy.png")
enemy_image = pygame.transform.scale(enemy_image, (50, 50))
font = pygame.font.Font(None, 36)
score = 0
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
player = GameSprite(player_image, 375, 275)
enemies = pygame.sprite.Group()
for i in range(7):
    x = random.randint(0, WIDTH - 50)
    y = random.randint(0, HEIGHT - 50)
    enemy = GameSprite(enemy_image, x, y)
    enemies.add(enemy)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemies)
running = True
while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player.rect.x += 5
    if keys[pygame.K_UP]:
        player.rect.y -= 5
    if keys[pygame.K_DOWN]:
        player.rect.y += 5
    collided_enemies = pygame.sprite.spritecollide(
        player, enemies, True
    )
    if collided_enemies:
        score += len(collided_enemies)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (20, 20))
    all_sprites.draw(screen)
    pygame.display.update()
pygame.quit()
sys.exit()