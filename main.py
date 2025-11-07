# Import necessary libraries and modules
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()   # Initialize pygame modules

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Creates screen object
    clock = pygame.time.Clock() # Create a Clock object to manipulate FPS in game
    dt = 0  # Initial delta time set to zero

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True: # Game loop
        for event in pygame.event.get():    # Event loop. Checks for events (like player inputs) to modify the game world
            if event.type == pygame.QUIT:
                return  # Exits main()

        screen.fill("black")  # Calling screen's method "fill" to set the black screen on the game window
        updateable.update(dt)
        for item in drawable:
            item.draw(screen)
        for item in asteroids:
            if item.check_collisions(player):
                sys.exit("Game over!")
        for item in asteroids:
            for bullet in shots:
                if item.check_collisions(bullet):
                    item.split()
        pygame.display.flip()   # Flips the back buffer (in memory) with a finished game scene to the front buffer where the player can see changes
        dt = clock.tick(60) / 1000  # Limits FPS to 60 and saves delta time from a previous scene into a variable

if __name__ == "__main__":
    main()

# pygame is a library which has modules (e.g. display or event). If you want to call a function specific to the module, we first
# call the library, then the module in question, and at last the function, for example pygame.display.flip(). screen is an object created
# by me, so it's functions are called like methods from a class, instead of using logic from above. 
# Regarding flip(): firstly, a buffer is a region in memory where pixel data is stored. pygame uses two buffers: back and front. Back buffer is
# hidden from a player, game screen is updated there with each line of code. Then, at the end of the game loop, we use flip() to flip that back
# buffer onto the front buffer where player can see changees. It is a useful mechanism, because we show the player the scene, once it's ready.
