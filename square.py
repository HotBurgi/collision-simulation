from constants import SCREEN_WIDTH, FPS
import pygame

class Square:
    def __init__(self, color, init_velocity, mass, x):
        self.side_length = 10 * mass
        self.color = color
        self.init_velocity = init_velocity
        self.curr_velocity = init_velocity
        self.mass = mass
        self.x = x
        self.y = 250 - self.side_length
        self.text = f"{self.mass} Kg"
        self.total_collisions = 0
        
    def update_x_position(self):
        self.x += self.curr_velocity * 1 / FPS
    
    def is_colliding(self, other):
        # Check if the squares are colliding
        if self.x < other.x + other.side_length and self.x + self.side_length > other.x:
            self.total_collisions += 1
            return True

    def wall_collision(self):
        # Check for wall collision
        if self.x <= 0 or self.x + self.side_length >= SCREEN_WIDTH:
            self.total_collisions += 1
            self.curr_velocity = -self.curr_velocity
    
    def change_direction(self, other):
        if self.is_colliding(other):
            v1f = ((self.mass - other.mass) * self.curr_velocity + 2 * other.mass * other.curr_velocity) / (self.mass + other.mass)
            
            v2f = ((other.mass - self.mass) * other.curr_velocity + 2 * self.mass * self.curr_velocity) / (self.mass + other.mass)
            self.curr_velocity = v1f
            other.curr_velocity = v2f
        else:
            self.wall_collision()
            other.wall_collision()
        
        self.update_x_position()
        other.update_x_position()
        
    def draw_text(self, screen):
        font = pygame.font.SysFont(None, self.side_length // 2)
        neg_color = tuple(255 - c for c in self.color)
        text = font.render(f"{self.mass} Kg", True, neg_color)
        text_rect = text.get_rect(center=(self.x + (self.side_length / 2), self.y + (self.side_length / 2)))
        screen.blit(text, text_rect)
        
    def draw(self, other, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.side_length, self.side_length))
        pygame.draw.rect(screen, other.color, (other.x, other.y, other.side_length, other.side_length))
        
        self.draw_text(screen)
        other.draw_text(screen)
        
    