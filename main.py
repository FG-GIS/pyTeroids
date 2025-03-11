import sys
import pygame
from asteroid import Asteroid
from player import Player
from shot import Shot
from asteroidfield import AsteroidField
from constants import *

TICK = 120

def main():
    print("Starting Asteroids!")
    counts = pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (updatable,drawable,asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (bullets,updatable,drawable)


    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(x=SCREEN_WIDTH/2,y=SCREEN_HEIGHT/2)
    field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color="#000000")
        updatable.update(dt)

        for a in asteroids:
             if a.check_collisions(player):
                 sys.exit("Game over!")

        for a in asteroids:
            for b in bullets:
                if a.check_collisions(b):
                    a.split()
                    b.kill()

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(TICK)/1000

if __name__ == "__main__":
    main()