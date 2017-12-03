import mainloop
import pygame


def paused(display):
    large_text = pygame.font.Font("/assets/spaceage.tts", 115)
    text_object = large_text.render("Paused", True, "black")
    pause_surface, pause_rectangle = text_object, text_object.get_rect()
    pause_surface.center = ((display.width/2), (display.height/2))
    display.screen.blit(pause_surface, pause_rectangle)

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    pause = False
                    break
