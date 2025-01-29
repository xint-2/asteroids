import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS) #inheret x, y from CircleShape and inherit PLAYER_RADIUS from constants
        self.rotation = 0 #new class variable for rotation, instantiated with nothing

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c] # returns corners of a triangle
    
    def rotate(self, dt): #rotation speed
       self.rotation +=  PLAYER_TURN_SPEED * dt 

    def update(self, dt):
        keys = pygame.key.get_pressed() #keys variable = key getting pressed on keyboard

        if keys[pygame.K_w]: #if (input) key pressed
            self.move(dt) # do this (in this case move forward)
        if keys[pygame.K_s]:
            self.move(dt * -1) # move forward except it's negative, so backwards then
        if keys[pygame.K_a]:
            self.rotate(dt * -1) # subtracts from players rotation
        if keys[pygame.K_d]:
            self.rotate(dt) # adds to the players rotation
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) #move up 1 on y-axis, 0 on x-axis (cartesian plane).
        # .rotate(self.rotation) determines the (x, y) axis relative to self (a.k.a the player)
        self.position += forward * PLAYER_SPEED * dt # updated self.position to the new position

    def shoot(self):
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED # move (0, 1) from players position
        my_shot = Shot(self.position.x, self.position.y) # new Shot class instance (my_shot = object)
        # starts the shot at the players location (self = player object position)
        my_shot.velocity = velocity # adds velocity to my_shot class instance
        # sets the new object(my_shot of Class Shot) velocity(position) equal to the velocity(position)
        # this maintains the velocity each frame till it goes offscreen
