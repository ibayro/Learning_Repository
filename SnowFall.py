import pygame
import random
import sys
import time

MAX_X = 1920
MAX_Y = 1080
bg_color = (255, 255, 255)
IMG_SIZE = 50
max_snow = 100
SNOW_SIZE = 64


class Snow:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(2, 3)
        self.img_num = random.randint(2, 3)
        self.image_filename = "snow" + str(self.img_num) + ".png"
        self.image = pygame.image.load(self.image_filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (SNOW_SIZE, SNOW_SIZE))

    def move_snow(self):
        self.y = self.y + self.speed
        if self.y > MAX_Y:
            self.y = (0 - SNOW_SIZE)

        i = random.randint(1, 3)
        if i == 1:  # move right
            self.x += 1
            if self.x > MAX_X:
                self.x = (0 - SNOW_SIZE)
        elif i == 2:  # move left
            self.x -= 1
            if self.x < (0 - SNOW_SIZE):
                self.x = MAX_X

    def draw_snow(self):
        screen.blit(self.image, (self.x, self.y))


def initialize_snow(max_snow, snowfall):
    for i in range(0, max_snow):
        xx: int = random.randint(0, MAX_X)
        yy: int = random.randint(0, MAX_Y)
        snowfall.append(Snow(xx, yy))


def initialize_pygame(max_x, max_y):
    pygame.init()
    screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)


def check_for_exit():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()


# ------------------MAIN GAME------------------------

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
bg_color = (255, 255, 255)
initialize_pygame(MAX_X, MAX_X)
snowfall = []
initialize_snow(max_snow, snowfall)

while True:
    screen.fill(bg_color)
    check_for_exit()
    for i in snowfall:
        i.move_snow()
        i.draw_snow()
    time.sleep(0.0020)
    pygame.display.flip()
