import pygame
from settings import WORDLE_SCREEN_WIDTH, WORDLE_SCREEN_HEIGHT
from gamestate import PlayState

pygame.init()
screen = pygame.display.set_mode((WORDLE_SCREEN_WIDTH, WORDLE_SCREEN_HEIGHT))
pygame.display.set_caption("WORDLE")
clock = pygame.time.Clock()

current_state = PlayState(None)

running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    current_state.handle_events(events)
    current_state.update()
    current_state.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()