import time

import pygame
from pygame.locals import (
    KEYDOWN,QUIT, K_ESCAPE,
    K_w, K_a, K_s, K_d
)

red = [255, 0 , 0]
green = [0, 255, 0]
black = [0, 0, 0]


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen_center = [SCREEN_HEIGHT / 2, SCREEN_HEIGHT / 2]

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
GAME_FONT = pygame.freetype.Font("AlfaSlabOne-Regular.ttf", 100)
clock = pygame.time.Clock()

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super(Snake, self).__init__()
        self.width = 30
        self.height = 10
        self.surf = pygame.Surface([self.width, self.height])
        self.surf.fill(green)
        self.rect = self.surf.get_rect()
        self.rect.center = screen_center
        self.speed = 10
    def update(self, dx, dy):
        self.rect.move_ip(dx, dy)
        print(self.rect.x)


def gameOver():
    snake.kill()
    text_surface, rect = GAME_FONT.render("Game Over!", [255, 255, 255])

    screen.blit(text_surface, [(SCREEN_WIDTH / 7), (SCREEN_HEIGHT / 2.5)])
    pygame.display.flip()
    time.sleep(3)

delta_x = 0
delta_y = 0

snake = Snake()

running = True
while running:

    for event in pygame.event.get():

        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                running = False

            if event.key == K_w:
                delta_y = -snake.speed
                delta_x= 0
            if event.key == K_s:
                delta_y = snake.speed
                delta_x = 0
            if event.key == K_a:
                delta_x = -snake.speed
                delta_y = 0
            if event.key == K_d:
                delta_x = snake.speed
                delta_y = 0
        elif event.type == QUIT:
            running = False

    if snake.rect.x <= 0 or snake.rect.x >= SCREEN_WIDTH or snake.rect.y <= 0 or snake.rect.y >= SCREEN_HEIGHT:
        gameOver()
        running = False
    screen.fill(black)
    snake.update(delta_x, delta_y)

    clock.tick(30)
    screen.blit(snake.surf, snake.rect)
    pygame.display.flip()