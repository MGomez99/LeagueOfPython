import sys
import EEgg
import music
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

    konami_code = ['u', 'u',  'd', 'd', 'l', 'r', 'l', 'r', 'b', 'a']
    input_code = ['', '', '', '', '', '', '', '', '', '']
    easter_egg = False
    while isPaused:
        while not easter_egg:
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
                    input_code = EEgg.k_code(input_code, event)
            if input_code == konami_code:
                easter_egg = True
            pygame.event.clear()
            pygame.display.update()

        if easter_egg:
            # anything you wanna see for the easter egg goes here
            print("Konami code! Larkin is hardstuck plat 5 LUL")
            input_code = ['', '', '', '', '', '', '', '', '', '']
            music.easterEgg()
            easter_egg = False
