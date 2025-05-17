import pygame
import sys

# https://it.wikipedia.org/wiki/Urto_elastico

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
FPS = 60
BG_COLOR = (30, 30, 30)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Template")

# Clock for controlling FPS
clock = pygame.time.Clock()

x = 10  # Initial x position

# Main loop
running = True
while running:
    clock.tick(FPS)  # Limit the frame rate

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic here
    x += 5  # Move the square to the right

    # Drawing
    screen.fill(BG_COLOR)  # Fill the screen with background color

    # Draw a square                          X, Y, WIDTH, HEIGHT
    pygame.draw.rect(screen, (255, 255, 255), (x, 2, 10, 10))

    # Update display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
