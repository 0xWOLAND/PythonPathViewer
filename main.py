import pygame
from pygame.locals import *

pygame.init()
WHITE = pygame.Color(255,255,255)
DISPLAYSURF = pygame.display.set_mode((1000,1000))
for i in range(0, 750, 50):
    for j in range(0, 500, 50):
        pygame.draw.rect(DISPLAYSURF, WHITE, (i + 125, j + 250, 40, 40), 0)



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
