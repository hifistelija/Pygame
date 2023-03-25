import pygame

pygame.init()
screen = pygame.display.set_mode((700, 700), flags=0, depth=32)
sprite1 = pygame.image.load("images/butterfly.png")
sprite1 = pygame.transform.scale(sprite1, (32, 32))
sprite_width = sprite1.get_width()
sprite_height = sprite1.get_height()
pygame.display.set_caption("Hello Pygame")
screen.fill((0, 0, 0))
game_over = False

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # center sprite
    screen.blit(sprite1, (screen.get_width() / 2 - sprite_width / 2, screen.get_height() / 2 - sprite_height / 2))
    pygame.display.update()

pygame.quit()
