import pygame
import json


def show_stats(player1, player2, screen):
    textsize1 = 9  # regular stats
    textsize2 = 27  # headers
    """
    Some Larkin magic that shows stats. Player dependent stat tracking and placement
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
    title1_text = pygame.font.Font('assets/spaceage.ttf', textsize2).render("PLAYER 1", True, (255, 255, 255))
    title1_rect = title1_text.get_rect(left=100, top=350)
    screen.blit(title1_text, title1_rect)
    title2_text = pygame.font.Font('assets/spaceage.ttf', textsize2).render("PLAYER 2", True, (255, 255, 255))
    title2_rect = title2_text.get_rect(left=500, top=350)
    screen.blit(title2_text, title2_rect)

    # number of shots
    numofshots1_text = pygame.font.Font('assets/spaceage.ttf', textsize1).render(
        "Number of shots: " + str(player1.number_of_shots), True, (255, 255, 255))
    numofshots1_rect = numofshots1_text.get_rect(left=100, top=430)
    screen.blit(numofshots1_text, numofshots1_rect)
    numofshots2_text = pygame.font.Font('assets/spaceage.ttf', textsize1).render(
        "Number of shots: " + str(player2.number_of_shots), True, (255, 255, 255))
    numofshots2_rect = numofshots2_text.get_rect(left=500, top=430)
    screen.blit(numofshots2_text, numofshots2_rect)
    # number of hits
    numofhits1_text = pygame.font.Font('assets/spaceage.ttf', textsize1).render(
        "Number of hits: " + str(player1.number_of_hits), True, (255, 255, 255))
    numofhits1_rect = numofhits1_text.get_rect(left=100, top=450)
    screen.blit(numofhits1_text, numofhits1_rect)
    numofhits2_text = pygame.font.Font('assets/spaceage.ttf', textsize1).render(
        "Number of hits: " + str(player2.number_of_hits), True, (255, 255, 255))
    numofhits2_rect = numofhits2_text.get_rect(left=500, top=450)
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
    acc1_text = pygame.font.Font('assets/spaceage.ttf', textsize1).render("Accuracy: " + acc1, True, (255, 255, 255))
    acc1_rect = acc1_text.get_rect(left=100, top=470)
    screen.blit(acc1_text, acc1_rect)
    acc2_text = pygame.font.Font('assets/spaceage.ttf', textsize1).render("Accuracy: " + acc2, True, (255, 255, 255))
    acc2_rect = acc2_text.get_rect(left=500, top=470)
    screen.blit(acc2_text, acc2_rect)

    # damage taken
    dmg1_text = pygame.font.Font('assets/spaceage.ttf', textsize1).render("Damage taken: " + str(player1.damagetaken),
                                                                          True, (255, 255, 255))
    dmg1_rect = dmg1_text.get_rect(left=100, top=490)
    screen.blit(dmg1_text, dmg1_rect)
    dmg2_text = pygame.font.Font('assets/spaceage.ttf', textsize1).render("Damage taken: " + str(player2.damagetaken),
                                                                          True, (255, 255, 255))
    dmg2_rect = dmg2_text.get_rect(left=500, top=490)
    screen.blit(dmg2_text, dmg2_rect)

    # mana spent
    mana1_text = pygame.font.Font('assets/spaceage.ttf', textsize1).render("Mana spent: " + str(player1.manaspent),
                                                                           True, (255, 255, 255))
    mana1_rect = mana1_text.get_rect(left=100, top=510)
    screen.blit(mana1_text, mana1_rect)
    mana2_text = pygame.font.Font('assets/spaceage.ttf', textsize1).render("Mana spent: " + str(player2.manaspent),
                                                                           True, (255, 255, 255))
    mana2_rect = mana1_text.get_rect(left=500, top=510)
    screen.blit(mana2_text, mana2_rect)

    # final health
    hp1_text = pygame.font.Font('assets/spaceage.ttf', textsize1).render("Final health: " + str(player1.hp), True,
                                                                         (255, 255, 255))
    hp1_rect = hp1_text.get_rect(left=100, top=530)
    screen.blit(hp1_text, hp1_rect)
    hp2_text = pygame.font.Font('assets/spaceage.ttf', textsize1).render("Final health: " + str(player2.hp), True,
                                                                         (255, 255, 255))
    hp2_rect = hp2_text.get_rect(left=500, top=530)
    screen.blit(hp2_text, hp2_rect)
    pygame.display.flip()


def highScores(player, screen):
    """
        Displays high scores stored externally
        :param player: adds players high scores if any
        :param screen: pygame screen
        :return: none
    """
    data = {}
    textsize1 = 9  # regular stats
    textsize2 = 27  # headers
    with open("highscores.txt", "r") as file:
        data = json.load(file)
    with open("highscores.txt", "w") as file:
        statistics = ["number_of_shots", "number_of_hits", "accuracy", "damagetaken", "manaspent", "hp"]
        n = 0
        for stat in statistics:
            if stat in data.keys():
                if n == 0:
                    if int(data["number_of_shots"]) < int(player.number_of_shots):
                        data["number_of_shots"] = player.number_of_shots
                    n += 1
                if n == 1:
                    if int(data["number_of_hits"]) < int(player.number_of_hits):
                        data["number_of_hits"] = player.number_of_hits
                    n += 1
                if n == 2:

                    if int(data["accuracy"]) < int(player.accuracy):
                        data["accuracy"] = player.accuracy
                    n += 1
                if n == 3:
                    if int(data["damagetaken"]) < int(player.damagetaken):
                        data["damagetaken"] = player.damagetaken
                    n += 1
                if n == 4:
                    if int(data["manaspent"]) < int(player.manaspent):
                        data["manaspent"] = player.manaspent
                    n += 1
                if n == 5:
                    if int(data["hp"]) < int(player.hp):
                        data["hp"] = player.hp
                    n += 1

            else:
                if n == 0:
                    data["number_of_shots"] = player.number_of_shots
                    n += 1
                if n == 1:
                    data["number_of_hits"] = player.number_of_hits
                    n += 1
                if n == 2:
                    data["accuracy"] = player.accuracy
                    n += 1
                if n == 3:
                    data["damagetaken"] = player.damagetaken
                    n += 1
                if n == 4:
                    data["manaspent"] = player.manaspent
                    n += 1
                if n == 5:
                    data["hp"] = player.hp
        jsonstuff = json.dumps(data)
        file.write(jsonstuff)

    # header
    highscore_text = pygame.font.Font('assets/spaceage.ttf', textsize2).render("HIGH SCORES", True, (255, 255, 255))
    highscore_rect = highscore_text.get_rect(left=300, top=350)
    screen.blit(highscore_text, highscore_rect)

    # number of shots
    numofshots_text = pygame.font.Font('assets/spaceage.ttf', textsize1).render(
        "Number of shots: " + str(data["number_of_shots"]), True, (255, 255, 255))
    numofshots_rect = numofshots_text.get_rect(left=300, top=430)
    screen.blit(numofshots_text, numofshots_rect)

    # number of hits
    numofhits_text = pygame.font.Font('assets/spaceage.ttf', textsize1).render(
        "Number of hits: " + str(data["number_of_hits"]), True, (255, 255, 255))
    numofhits_rect = numofhits_text.get_rect(left=300, top=450)
    screen.blit(numofhits_text, numofhits_rect)

    # accuracy
    acc_text = pygame.font.Font('assets/spaceage.ttf', textsize1).render("Accuracy: " + str(data["accuracy"]), True,
                                                                         (255, 255, 255))
    acc_rect = acc_text.get_rect(left=300, top=470)
    screen.blit(acc_text, acc_rect)

    # damage taken
    dmg_text = pygame.font.Font('assets/spaceage.ttf', textsize1).render("Damage taken: " + str(data["damagetaken"]),
                                                                         True, (255, 255, 255))
    dmg_rect = dmg_text.get_rect(left=300, top=490)
    screen.blit(dmg_text, dmg_rect)

    # mana spent
    mana_text = pygame.font.Font('assets/spaceage.ttf', textsize1).render("Mana spent: " + str(data["manaspent"]),
                                                                          True, (255, 255, 255))
    mana_rect = mana_text.get_rect(left=300, top=510)
    screen.blit(mana_text, mana_rect)

    # final health
    hp_text = pygame.font.Font('assets/spaceage.ttf', textsize1).render("Final health: " + str(data["hp"]), True,
                                                                        (255, 255, 255))
    hp_rect = hp_text.get_rect(left=300, top=530)
    screen.blit(hp_text, hp_rect)
    pygame.display.flip()
