import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite): #CircleShape class is a sprite
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
         #initialize CircleShape as a sprite

        self.position = pygame.Vector2(x, y) # position of self is a vector on cartesian plane
        self.velocity = pygame.Vector2(0, 0) # velocity is none for now
        self.radius = radius #radius is input radius

    def draw(self, screen): #for drawing the player, this gets overridden
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def collides_with(self, other): #collision method, determines if radius of self overlaps with anything, returns bool
        return self.position.distance_to(other.position) <= self.radius + other.radius

    def update(self, dt): #override me
        pass