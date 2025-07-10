import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Paint App")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
PURPLE = (128, 0, 128)


screen.fill(WHITE)


brush_color = BLACK
brush_size = 5
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

        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                brush_color = RED
            elif event.key == pygame.K_g:
                brush_color = GREEN
            elif event.key == pygame.K_b:
                brush_color = BLUE
            elif event.key == pygame.K_k:
                brush_color = BLACK
            elif event.key == pygame.K_p:
                brush_color = PURPLE
            elif event.key == pygame.K_c:
                screen.fill(WHITE)  
            elif event.key == pygame.K_ESCAPE:
                running = False

    
    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, brush_color, mouse_pos, brush_size)

    
    pygame.display.update()


pygame.quit()
sys.exit()
