import pygame


def k_code(input_code, event):
    """
    Easter Egg
    :param input_code: input from before
    :param event: current event that occurred
    :return: input from before + new input(if any)
    """

    if event.key == pygame.K_UP:
        if input_code.count('u') == 2:
            return input_code
        elif input_code[0] != 'u':
            input_code[0] = 'u'
        elif input_code[1] != 'u':
            input_code[1] = 'u'

    elif event.key == pygame.K_DOWN:
        if input_code.count('d') == 2:
            return input_code
        elif input_code[2] != 'd':
            input_code[2] = 'd'
        elif input_code[3] != 'd':
            input_code[3] = 'd'

    elif event.key == pygame.K_LEFT:
        if input_code.count('l') == 2:
            return input_code
        elif input_code[4] != 'l':
            input_code[4] = 'l'
        elif input_code[6] != 'l':
            input_code[6] = 'l'

    elif event.key == pygame.K_RIGHT:
        if input_code.count('r') == 2:
            return input_code
        elif input_code[5] != 'r':
            input_code[5] = 'r'
        elif input_code[7] != 'r':
            input_code[7] = 'r'

    elif event.key == pygame.K_b:
        if input_code.count('b') == 1:
            return input_code
        elif input_code[8] != 'b':
            input_code[8] = 'b'

    elif event.key == pygame.K_a:
        if input_code.count('a') == 1:
            return input_code
        elif input_code[9] != 'a':
            input_code[9] = 'a'

    elif event.key == pygame.K_CAPSLOCK:
        input_code = []

    return input_code
