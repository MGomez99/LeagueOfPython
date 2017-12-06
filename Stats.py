import player
import pygame


def show_stats(player1, player2, screen):
    """
    Some Larkin magic that shows stats
    :param player1: player 1
    :param player2: player2
    :param screen: pygame screen
    :return: none
    """
    if player1.hp <= 0:
        game_over_bg = pygame.image.load("assets/player2win.png")

    elif player2.hp <= 0:
        game_over_bg = pygame.image.load("assets/player1win.png")
    screen.blit(game_over_bg, game_over_bg.get_rect())
    # statistics
    title1_text = pygame.font.Font('assets/spaceage.ttf', 30).render("PLAYER 1", True, (0, 0, 0))
    title1_rect = title1_text.get_rect(left=100, top=350)
    screen.blit(title1_text, title1_rect)
    title2_text = pygame.font.Font('assets/spaceage.ttf', 30).render("PLAYER 2", True, (0, 0, 0))
    title2_rect = title2_text.get_rect(left=600, top=350)
    screen.blit(title2_text, title2_rect)
    # number of shots
    numofshots1_text = pygame.font.Font('assets/spaceage.ttf', 10).render(
        "Number of shots: " + str(player1.number_of_shots), True, (0, 0, 0))
    numofshots1_rect = numofshots1_text.get_rect(left=100, top=400)
    screen.blit(numofshots1_text, numofshots1_rect)
    numofshots2_text = pygame.font.Font('assets/spaceage.ttf', 10).render(
        "Number of shots: " + str(player2.number_of_shots), True, (0, 0, 0))
    numofshots2_rect = numofshots2_text.get_rect(left=600, top=400)
    screen.blit(numofshots2_text, numofshots2_rect)
    # number of hits
    numofhits1_text = pygame.font.Font('assets/spaceage.ttf', 10).render(
        "Number of hits: " + str(player1.number_of_hits), True, (0, 0, 0))
    numofhits1_rect = numofhits1_text.get_rect(left=100, top=410)
    screen.blit(numofhits1_text, numofhits1_rect)
    numofhits2_text = pygame.font.Font('assets/spaceage.ttf', 10).render(
        "Number of hits: " + str(player2.number_of_hits), True, (0, 0, 0))
    numofhits2_rect = numofhits2_text.get_rect(left=600, top=410)
    screen.blit(numofhits2_text, numofhits2_rect)
    # accuracy
    if player1.number_of_shots > 0:
        acc1 = str(round(player1.number_of_hits / player1.number_of_shots, 2) * 100) + "%"
    else:
        acc1 = "N/A"
    if player2.number_of_shots > 0:
        acc2 = str(round(player2.number_of_hits / player2.number_of_shots, 2) * 100) + "%"
    else:
        acc2 = "N/A"
    acc1_text = pygame.font.Font('assets/spaceage.ttf', 10).render("Accuracy: " + acc1, True, (0, 0, 0))
    acc1_rect = acc1_text.get_rect(left=100, top=420)
    screen.blit(acc1_text, acc1_rect)
    acc2_text = pygame.font.Font('assets/spaceage.ttf', 10).render("Accuracy: " + acc2, True, (0, 0, 0))
    acc2_rect = acc2_text.get_rect(left=600, top=420)
    screen.blit(acc2_text, acc2_rect)
    # damage taken
    dmg1_text = pygame.font.Font('assets/spaceage.ttf', 10).render("Damage taken: " + str(player1.damagetaken),
                                                                   True, (0, 0, 0))
    dmg1_rect = acc1_text.get_rect(left=100, top=430)
    screen.blit(dmg1_text, dmg1_rect)
    dmg2_text = pygame.font.Font('assets/spaceage.ttf', 10).render("Damage taken: " + str(player2.damagetaken),
                                                                   True, (0, 0, 0))
    dmg2_rect = acc1_text.get_rect(left=600, top=430)
    screen.blit(dmg2_text, dmg2_rect)
    # mana spent
    mana1_text = pygame.font.Font('assets/spaceage.ttf', 10).render("Mana spent: " + str(player1.manaspent),
                                                                    True, (0, 0, 0))
    mana1_rect = mana1_text.get_rect(left=100, top=440)
    screen.blit(mana1_text, mana1_rect)
    mana2_text = pygame.font.Font('assets/spaceage.ttf', 10).render("Mana spent: " + str(player2.manaspent),
                                                                    True, (0, 0, 0))
    mana2_rect = mana1_text.get_rect(left=600, top=440)
    screen.blit(mana2_text, mana2_rect)
    # final health
    hp1_text = pygame.font.Font('assets/spaceage.ttf', 10).render("Final health: " + str(player1.hp), True,
                                                                  (0, 0, 0))
    hp1_rect = hp1_text.get_rect(left=100, top=450)
    screen.blit(hp1_text, hp1_rect)
    hp2_text = pygame.font.Font('assets/spaceage.ttf', 10).render("Final health: " + str(player2.hp), True,
                                                                  (0, 0, 0))
    hp2_rect = hp2_text.get_rect(left=600, top=450)
    screen.blit(hp2_text, hp2_rect)
    pygame.display.flip()
