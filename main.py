import pygame
pygame.init() #initialize
screen = pygame.display.set_mode((400,600))
#loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.flip()