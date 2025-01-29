from circleshape import *
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED


class Shot(CircleShape):
    def __init__(self, x, y):
      super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), SHOT_RADIUS, 1)

    def update(self, dt):
        self.position += self.velocity * dt