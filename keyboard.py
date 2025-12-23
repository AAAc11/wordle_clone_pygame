import pygame

#rows of letters
def keyboard_display(window, frame_color):
    for i in range(30, 521, 50):
        pygame.draw.rect(window, frame_color, (i, 450, 40, 55), 0, border_radius=3)

    for i in range(55, 500, 50):
        pygame.draw.rect(window, frame_color, (i, 520, 40, 55), 0, border_radius=3)

    for i in range(105, 450, 50):
        pygame.draw.rect(window, frame_color, (i, 590, 40, 55), 0, border_radius=3)

    pygame.draw.rect(window, frame_color, (30, 590, 65, 55), 0, border_radius=3)
    pygame.draw.rect(window, frame_color, (455, 590, 60, 55), 0, border_radius=3)
