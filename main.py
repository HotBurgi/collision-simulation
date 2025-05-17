from constants import *
from square import Square
import pygame
import sys

# https://it.wikipedia.org/wiki/Urto_elastico

# Initialize Pygame
print("Initializing Pygame...")
pygame.init()
print("Pygame initialized.")

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Elastic Collision Simulation")

o1 = Square(50, (0, 0, 0), 200, 10, 175)
o2 = Square(50, (0, 0, 0), -200, 340, 175)

# Clock for controlling FPS
clock = pygame.time.Clock()

# Wait for spacebar to start simulation
waiting = True
font = pygame.font.SysFont(None, 48)
text = font.render("Press SPACE to start", True, (0, 0, 0))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

while waiting:
    screen.fill(BG_COLOR)
    screen.blit(text, text_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            waiting = False

# Main loop
running = True
while running:
    clock.tick(FPS)  # Limit the frame rate

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic here
    o1.update_x_position(1/FPS)
    o2.update_x_position(1/FPS)

    o1.change_direction(o2)
    
    # Drawing
    screen.fill(BG_COLOR)  # Fill the screen with background color

    # Draw a square                          X, Y, WIDTH, HEIGHT
    pygame.draw.rect(screen, o1.color, (o1.x, o1.y, o1.side_length, o1.side_length))
    pygame.draw.rect(screen, o2.color, (o2.x, o2.y, o2.side_length, o2.side_length))
    

    # Update display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
