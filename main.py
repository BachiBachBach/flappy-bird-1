import pygame
from physics import *
from constants import *


screen = pygame.display.set_mode((screen_width, screen_height))


game_objects = []


player = RigidBody(50, 50, game_objects)
player.position = (250, 250)

player2 = RigidBody(25, 25, game_objects)
player2.position = (100, 100)







def draw():
    for object in game_objects:
        screen.blit(object.image, (object.position))
        





pygame.init()

def main():
    running = True
    clock = pygame.time.Clock()


    gravityForce = 0
    acceleration = 8

    while running:
        screen.fill("white")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        Physics.addGravity(game_objects, gravityForce)


        if gravityForce < 4:
            gravityForce += acceleration

    

        draw()
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    exit()

    
# This is the function that starts the game
main()