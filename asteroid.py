import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

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
    def split(self, ):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        self.vect_1 = self.velocity.rotate(random_angle)
        self.vect_2 = self.velocity.rotate(random_angle * -1)
        self.new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, self.new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, self.new_radius)
        new_asteroid_1.velocity = self.vect_1 * 1.2
        new_asteroid_2.velocity = self.vect_2 * 1.2


