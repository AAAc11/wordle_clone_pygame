import pygame
from settings import WORDLE_SCREEN_WIDTH, WORDLE_SCREEN_HEIGHT
from gamestate import MenuState

pygame.init()
screen = pygame.display.set_mode((WORDLE_SCREEN_WIDTH, WORDLE_SCREEN_HEIGHT))
pygame.display.set_caption("WORDLE")
clock = pygame.time.Clock()

current_state = MenuState(None)

running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    new_state = current_state.handle_events(events)
    if new_state:
        current_state = new_state

    current_state.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()