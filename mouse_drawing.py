import pygame
import sys
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Drawing Tool")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen.fill(WHITE)
drawing = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False  
    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, BLACK, mouse_pos, 5 )
    pygame.display.update()
pygame.quit()
sys.exit()
