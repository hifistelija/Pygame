import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((500, 500), flags=0, depth=32)
pygame.display.set_caption("Hello Keyboard")
screen.fill((0, 0, 0))

sprite1 = pygame.image.load("images/butterfly.png")
sprite1 = pygame.transform.scale(sprite1, (32, 32))
sprite_width = sprite1.get_width()
sprite_height = sprite1.get_height()
x, y = (0, 0)
clock = pygame.time.Clock()

game_over = False
while not game_over:

    dt = clock.tick(100)
    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEMOTION:
            # Get the current mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Adjust the sprite position based on the mouse position
            x = mouse_x - sprite_width / 2
            y = mouse_y - sprite_height / 2

    # Detect keypress
    if pressed[K_UP]:
        y -= 0.5 * dt
    if pressed[K_DOWN]:
        y += 0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if pressed[K_SPACE]:
        x = 0
        y = 0

    # Create boundaries
    if x > screen.get_width() - sprite_width:
        x = screen.get_width() - sprite_width
    if x < 0:
        x = 0
    if y > screen.get_height() - sprite_height:
        y = screen.get_height() - sprite_height
    if y < 0:
        y = 0

    screen.fill((0, 0, 0))  # refresh the screen after each frame
    screen.blit(sprite1,(x, y))
    pygame.display.update()

pygame.quit()
