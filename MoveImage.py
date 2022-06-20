import pygame

MAX_X = 1920
MAX_Y = 1080
game_over = False
bg_color = (255, 255, 255)
IMG_SIZE = 50

x = 100
y = 100

move_right = False
move_left = False
move_up = False
move_down = False

# ------------MAIN GAME LOOP------------------

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
pygame.display.set_caption("My first Python Game")
myImage = pygame.image.load("carv.png").convert()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                game_over = False
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

    if move_left:
        x -= 1
        if x < 0:
            x = 0
    if move_right:
        x += 1
        if x > MAX_X - IMG_SIZE:
            x = MAX_X - IMG_SIZE
    if move_up:
        y -= 1
        if y < 0:
            y = 0
    if move_down:
        y += 1
        if y > MAX_Y - IMG_SIZE:
            y = MAX_Y - IMG_SIZE

    screen.fill(bg_color)
    screen.blit(myImage, (x, y))
    pygame.display.flip()

