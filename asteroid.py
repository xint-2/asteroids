import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen): # override draw method of CircleShape with this one
        pygame.draw.circle(screen, "white",(self.position.x, self.position.y), self.radius, 2)
    # draw a small circle
    def update(self, dt):
        # sub-classes must override
        self.position += (self.velocity * dt) 
        # update override
