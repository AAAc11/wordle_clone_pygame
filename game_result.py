import pygame

WINDOW_COLOR = (31, 27, 27)
WHITE = (255, 255, 255)

pygame.init()
pygame.font.init()

class Result:
    def __init__(self):
        self.RESULT_SCREEN_WIDTH = 250
        self.RESULT_SCREEN_HEIGHT = 250
        self.running = True

    def creating_window(self):
        main_window = pygame.display.set_mode((self.RESULT_SCREEN_WIDTH, self.RESULT_SCREEN_HEIGHT))
        main_window.fill(WINDOW_COLOR)
        pygame.display.set_caption("RESULT")

        return main_window

    def printing_result(self, result, rows, gameplay_time, key):
        main_window = self.creating_window()
        font = pygame.font.SysFont(None, 65)

        if result == "win":
            result_text = font.render('YOU WON!', True, WHITE)
        else:
            result_text = font.render('YOU LOST!', True, WHITE)
        result_rect = result_text.get_rect(center=(self.RESULT_SCREEN_WIDTH // 2, 50))

        font = pygame.font.SysFont(None, 25)

        info = f"It took you {gameplay_time} seconds"
        result_info = font.render(info, True, WHITE)
        info_rect = result_info.get_rect(center=(self.RESULT_SCREEN_WIDTH // 2, 100))

        result_key = font.render(f"Key: {key}", True, WHITE)
        key_rect = result_key.get_rect(center=(self.RESULT_SCREEN_WIDTH // 2, 130))

        while self.running:
            main_window.fill(WINDOW_COLOR)
            main_window.blit(result_text, result_rect)
            main_window.blit(result_info, info_rect)
            main_window.blit(result_key, key_rect)

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False