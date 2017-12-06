import sys

import pygame

from text_to_screen import tts


def paused(display, isPaused):
    """
    This function paused the game
    :param display: pygame display
    :param isPaused: is the game paused?
    :return: boolean for going to menu, is the game paused?
    """
    text = "Paused. Press space to continue or backspace to quit."
    tts(display, text, 50, 200, 'assets/spaceage.ttf', 20, (0, 255, 0))  # lazy
    # pause_surface, pause_rectangle = text_object, text_object.get_rect()
    # pause_surface.center = ((display.width/2), (display.height/2))
    # display.screen.blit(pause_surface, pause_rectangle)

    while isPaused:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    isPaused = False
                    return False, isPaused
                if event.key == pygame.K_BACKSPACE:
                    isPaused = False
                    return True, isPaused

        pygame.display.update()
