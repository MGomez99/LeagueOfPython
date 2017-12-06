import pygame
import player


def show_resources(players, screen):
    """
    Shows health and mana for players
    :param players: list of players
    :param screen: pygame screen
    :return: None
    """
    # player class has a coordinate pair of locations for their respective health/mana indicators based on team
    for player in players:
        health_text = pygame.font.Font('assets/spaceage.ttf', 30).render(str(round(player.hp)), True, (255, 0, 0))
        health_rect = health_text.get_rect(left=player.health_location[0], top=player.health_location[1])
        screen.blit(health_text, health_rect)

        mana1_text = pygame.font.Font('assets/spaceage.ttf', 30).render(str(round(player.mana, 2)), True, (0, 0, 255))
        mana1_rect = mana1_text.get_rect(left=player.mana_location[0], top=player.mana_location[1])
        screen.blit(mana1_text, mana1_rect)
    pygame.display.flip()
