import pygame
from physics import *
from constants import *


screen = pygame.display.set_mode((screen_width, screen_height))


game_objects = []


player = RigidBody(50, 50)
player.position = (250, 250)

game_objects.append(player)








pygame.init()

def main():
    running = True
    clock = pygame.time.Clock()


    gravityForce = 0
    acceleration = 8

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        Physics.addGravity(game_objects, gravityForce)
        screen.fill("white")

        if gravityForce < 4:
            gravityForce += acceleration

    

        screen.blit(player.image, (player.position))
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    exit()

    

main()