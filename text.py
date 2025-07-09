import pygame
import sys

pygame.init()

width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Display Text on screen")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

font = pygame.font.SysFont(None, 36)

text_surface = font.render("Hello Pygame!", True, BLUE)

text_rect = text_surface.get_rect(center =(width//2, height//2))

running = True
while running:
    screen.fill(WHITE)
    
    screen.blit(text_surface, text_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()
    
pygame.quit()
sys.exit()
    