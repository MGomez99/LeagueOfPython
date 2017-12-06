import pygame


def tts(screen, mytext, x, y, font_type, size=40, color=(200, 000, 000)):
    """
    Easy text to screen object
    :param screen: Screen to blit text onto
    :param mytext: whatever text you want on the screen
    :param x: x coordinate
    :param y: y coordinate
    :param size: font zise
    :param color: color of text
    :param font_type: font to use, defaults to space age
    :return: none
    """

    text = str(mytext)
    font = pygame.font.Font(font_type, size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))
    return text
