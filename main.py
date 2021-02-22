import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()

        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

running = True

while running:
    screen.fill((0, 0, 0))
    surf = pygame.Surface((50, 50))
    surf.fill((255, 255, 255))
    rect = surf.get_rect()
    surf_center = (
        (SCREEN_WIDTH - surf.get_width()) / 2,
        (SCREEN_HEIGHT - surf.get_height()) / 2
    )
    screen.blit(surf, surf_center)
    pygame.display.flip()
    for event in pygame.event.get():


        if event.type == KEYDOWN:
            if event.type == K_UP:
                y += 10
            elif event.type == K_DOWN:
                y -= 10
            elif event.type == K_LEFT:
                x += 10
            elif event.type == K_RIGHT:
                x += 10
            elif event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False


