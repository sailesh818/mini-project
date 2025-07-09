import pygame
import sys

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Drawing shapes and circles")

RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (160, 32, 240)

running = True
while running:
    screen.fill(WHITE)
    
    pygame.draw.rect(screen, RED, (50, 50, 100, 60))
    pygame.draw.circle(screen, GREEN, (200, 200), 40)
    pygame.draw.line(screen, BLUE, (300, 300), (500, 100), 5)
    pygame.draw.ellipse(screen, PURPLE, (100, 250, 150, 80))
    pygame.draw.polygon(screen, YELLOW, [(400, 300), (450, 250), (500, 300)])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()
    
    
pygame.quit()
sys.exit()
    