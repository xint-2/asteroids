import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot


def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock() # fps control
    dt = 0

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)


    entity = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) #instance of class Player, it is an object
    asteroid_field = AsteroidField() # new instance (object) of class AsteroidField
   


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black") #adds "black" too screen method

        for obj in updatable: #for any object in updatatable group
            obj.update(dt) # update
        for obj in drawable:
            obj.draw(screen)



        for asteroid in asteroids: # for any class instance of asteroid in group asteroids
       # calls .collides_with method from circleshape class CircleShape. self = asteroid, other = entity
            if asteroid.collides_with(entity): 
                print("Game over!")
                sys.exit() # exit game


        pygame.display.flip()
        dt = clock.tick(60) / 1000 #fps control


if __name__ == "__main__":
    main()

# this line ensures that main() is only called when this fule is run directly
# it wont run it it's imported as a module