import pygame
pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My first game screen")
grey_color = (58, 58, 58)
try:
    image = pygame.image.load('image.png')
    image = pygame.transform.scale(image, (300, 300))
    image_rect = image.get_rect(center=(screen_width // 2, screen_height // 2))
except pygame.error:
    print("Image not found! Please ensure 'your_image.png' is in the folder.")
    image = None
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(grey_color)
    if image:
        screen.blit(image, image_rect)
    pygame.display.flip()
pygame.quit()