from constants import SCREEN_WIDTH

class Square:
    def __init__(self, side_length, color, init_velocity, x, y):
        self.side_length = side_length
        self.color = color
        self.init_velocity = init_velocity
        self.curr_velocity = init_velocity
        self.x = x
        self.y = y
        
    def update_x_position(self, delta_time):
        self.x += self.curr_velocity * delta_time
    
    def is_colliding(self, other):
        # Check if the squares are colliding
        if self.x < other.x + other.side_length and self.x + self.side_length > other.x:
            return True

    def wall_collision(self):
        # Check for wall collision
        if self.x <= 0 or self.x + self.side_length >= SCREEN_WIDTH:
            self.curr_velocity = -self.curr_velocity
    
    def change_direction(self, other):
        if self.is_colliding(other):
            self.curr_velocity = -self.curr_velocity
            other.curr_velocity = -other.curr_velocity
        else:
            self.wall_collision()
            other.wall_collision()