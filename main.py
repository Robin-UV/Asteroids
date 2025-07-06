import pygame
import pygame.locals
import constants
from player import Player
from asteroid import *
from asteroidfield import AsteroidField
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    numpass, numfail = pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    clock = pygame.time.Clock()
    dt = 0

    # groups for managing sprites
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # assign groups to classes so instances auto-add
    Player.containers = updatable, drawable
    Asteroid.containers = asteroids, updatable, drawable
    AsteroidField.containers = updatable
    Shot.containers = updatable, drawable, shots

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))

        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.has_colided(player):
                print("Game Over!")
                exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.has_colided(asteroid):
                    shot.kill()
                    asteroid.split()
        for d in drawable:
            d.draw(screen)
            
        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
