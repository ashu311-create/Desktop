import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
rect_width = 150
rect_height = 100
rect_x = (640 - rect_width) // 2
rect_y = (480 - rect_height) // 2
font = pygame.font.Font(None, 36)
text = font.render("Welcome to Pygame!", True, BLACK)
running = True
while running:
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE,
                     (rect_x, rect_y, rect_width, rect_height))
    screen.blit(text, (180, 50))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
sys.exit()