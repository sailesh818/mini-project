import pygame
import sys

# Initialize Pygame
pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Paint App")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
PURPLE = (128, 0, 128)

# Start with white screen
screen.fill(WHITE)

# Initial brush settings
brush_color = BLACK
brush_size = 5
drawing = False

# Main loop
running = True
while running:
    for event in pygame.event.get():
        # Quit event
        if event.type == pygame.QUIT:
            running = False

        # Mouse button pressed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True

        # Mouse button released
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        # Keyboard input
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
                screen.fill(WHITE)  # Clear screen
            elif event.key == pygame.K_ESCAPE:
                running = False

    # Drawing when mouse is held down
    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen, brush_color, mouse_pos, brush_size)

    # Update screen
    pygame.display.update()

# Exit
pygame.quit()
sys.exit()
