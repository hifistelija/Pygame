import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("Button")
text_colour = (255, 255, 255)
button_colour = (0, 0, 170)
button_over_colour = (255, 50, 50)
button_width = 100
button_height = 50
button_x = (screen.get_width() - button_width) / 2
button_y = (screen.get_height() - button_height) / 2
button_rect = [button_x, button_y, button_width, button_height]
button_font = pygame.font.SysFont("Arial", 28)
button_text = button_font.render("Quit", True, text_colour)
text_x = button_rect[0] + (button_width - button_text.get_width()) / 2
text_y = button_rect[1] + (button_height - button_text.get_height()) / 2
screen.fill((100, 100, 100))

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if(button_rect[0] <= x <= button_rect[0] + button_rect[2]
                    and button_rect[1] <= y <= button_rect[1] + button_rect[3]):
                game_over = True
        # Check if the mouse is over the button
        mouse_pos = pygame.mouse.get_pos()
        if (button_rect[0] <= mouse_pos[0] <= button_rect[0] + button_rect[2]
                and button_rect[1] <= mouse_pos[1] <= button_rect[1] + button_rect[3]):
            button_colour = button_over_colour
        else:
            button_colour = (0, 0, 170)

        # Draw the button
        pygame.draw.rect(screen, button_colour, button_rect)
        screen.blit(button_text, (text_x, text_y))
        pygame.display.update()
pygame.quit()
