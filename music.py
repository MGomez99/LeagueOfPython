import pygame


class Music:
    def playIntro(self):
        # plays the intro song
        pygame.mixer.music.load("assets/introsong.mp3")
        pygame.mixer.music.play(-1)

    def playMain(self):
        # plays the main song for the game
        pygame.mixer.music.load("assets/mainsong.mp3")
        pygame.mixer.music.play(-1)
