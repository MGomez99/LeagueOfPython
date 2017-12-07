import pygame


def playIntro():
    """
    plays intro song
    :return: None
    """
    pygame.mixer.music.load("assets/introsong.ogg")
    pygame.mixer.music.play(-1)


def playMain():
    """
    plays main song
    :return: None
    """
    pygame.mixer.music.load("assets/mainsong.ogg")
    pygame.mixer.music.play(-1)


def playGameOver():
    """
    plays game over song
    :return: None
    """
    pygame.mixer.music.load("assets/gameover.ogg")
    pygame.mixer.music.play(-1)


def playEasterEgg():
    """
    plays EE song
    :return: None
    """
    pygame.mixer.music.load("assets/lul.ogg")
    pygame.mixer.music.play(-1)
