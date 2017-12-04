import mainloop.py


def main():
    print("=====TESTING PLAYER MOVEMENT=====")
    testplayer = player.Player()
    print("=====POSITIVE VERTICAL MOVEMENT=====")
    testplayer.moveVer(1)
    assert testplayer.getCoords() == (0, 1)
    print("=====NEGATIVE VERTICAL MOVEMENT=====")
    testplayer.moveVer(-4)
    assert testplayer.getCoords() == (0, -3)
    print("=====ZERO VERTICAL MOVEMENT=====")
    testplayer.moveVer(0)
    assert testplayer.getCoords() == (0, -3)
    print("=====POSITIVE HORIZONTAL MOVEMENT=====")
    testplayer.moveHor(1)
    assert testplayer.getCoords() == (1, -3)
    print("=====NEGATIVE HORIZONTAL MOVEMENT=====")
    testplayer.moveHor(-4)
    assert testplayer.getCoords() == (-3, -3)
    print("=====ZERO HORIZONTAL MOVEMENT=====")
    testplayer.moveHor(0)
    assert testplayer.getCoords() == (-3, -3)
    print("=====ABILITY 1 COOLDOWN=====")
    testplayer.ability1()
    assert testplayer.ablity1Cooldown() == True
    print("=====ABILITY 2 COOLDOWN=====")
    testplayer.ability2()
    assert testplayer.ablity2Cooldown() == True
    print("=====ABILITY 3 COOLDOWN=====")
    testplayer.ability3()
    assert testplayer.ablity3Cooldown() == True
    print("=====ABILITY 4 COOLDOWN=====")
    testplayer.ability4()
    assert testplayer.ablity4Cooldown() == True


main()
