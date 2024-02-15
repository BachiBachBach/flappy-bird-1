import pygame

screen_width = 400
screen_height = 700

FPS = 60

screen = pygame.display.set_mode((screen_width, screen_height))





pygame.init()

def main():
    running = True
    clock = pygame.time.Clock()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        screen.fill("white")
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    exit()

    

main()