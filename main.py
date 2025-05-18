import pygame
import sys

# Initialize Pygame
print("Initializing Pygame...")
pygame.init()
print("Pygame initialized.")

from constants import *
from square import Square


# https://it.wikipedia.org/wiki/Urto_elastico
# https://www.youmath.it/lezioni/fisica/dinamica/3000-urto-elastico-in-due-dimensioni.html

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Elastic Collision Simulation")

o1 = Square((255, 0, 0), 200, 10, 10)
o2 = Square((0, 0, 0), -200, 1, SCREEN_WIDTH - 30 * 5 - 10)

# Clock for controlling FPS
clock = pygame.time.Clock()

# Wait for spacebar to start simulation
waiting = True
text = FONT.render("Press SPACE to start", True, (0, 0, 0))
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

    #---------- Update ----------
    
    o1.change_direction(o2) # Update the squares' positions and check for collisions
    
    #---------- Drawing ----------
    screen.fill(BG_COLOR)  # Background color

    o1.draw(o2, screen) # Draw the suqares
    
    # Display collision count
    text = FONT.render(f"Collision: {o1.total_collisions + o2.total_collisions}", True, (0, 0, 0))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 5))
    screen.blit(text, text_rect)

    # Update display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
