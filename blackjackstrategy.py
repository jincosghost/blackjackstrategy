#!/usr/bin/env python3
"""Blackjack Strategy"""

import os
import sys

PLAYING = True


class colour:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def cleanscreen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
    return


while PLAYING:
    cleanscreen()

    if (sys.version_info < (3, 0)):
        print(
            colour.RED +
            "This app requires Python 3! Please reload with: python3 perma.py" +
            colour.END)
        sys.exit(1)

    A = True
    B = False
    C = False

    SPLIT = colour.BLUE + "SPLIT" + colour.END
    HIT = colour.GREEN + "HIT" + colour.END
    STAND = colour.YELLOW + "STAND" + colour.END
    DOUBLE = colour.PURPLE + "DOUBLE" + colour.END

    while A:
        DEALER = int(input('What is the dealers card? (Ace = 1)\n'))

        if DEALER > 10 or DEALER < 1:
            print(
                colour.RED +
                "Enter a number between 1 and 10. Ace = 1." +
                colour.END)
        else:
            A = False
            B = True

    while B:
        CARD1 = int(input('What is your first card? (Ace = 1)\n'))

        if CARD1 > 10 or CARD1 < 1:
            print(
                colour.RED +
                "Enter a number between 1 and 10. Ace = 1." +
                colour.END)
        else:
            B = False
            C = True

    while C:
        CARD2 = int(input('What is your second card? (Ace = 1)\n'))

        if CARD2 > 10 or CARD2 < 1:
            print(
                colour.RED +
                "Enter a number between 1 and 10. Ace = 1." +
                colour.END)
        else:
            C = False

        if CARD1 == CARD2 and CARD2 == 1 or CARD2 == 8:
            print(SPLIT)
        elif CARD1 == CARD2 and CARD2 == 10:
            print(STAND)
        elif CARD1 == CARD2 and CARD2 == 2 or CARD2 == 3 or CARD2 == 7:
            if DEALER >= 2 and DEALER <= 7:
                print(SPLIT)
            else:
                print(HIT)
        elif CARD1 == CARD2 and CARD2 == 4:
            if DEALER == 5 or DEALER == 6:
                print(SPLIT)
            else:
                print(HIT)
        elif CARD1 == CARD2 and CARD2 == 5:
            if DEALER == 1 or DEALER == 10:
                print(HIT)
            else:
                print(DOUBLE)
        elif CARD1 == CARD2 and CARD2 == 6:
            if DEALER <= 6:
                print(SPLIT)
            else:
                print(HIT)
        elif CARD1 == CARD2 and CARD2 == 7:
            if DEALER <= 7:
                print(SPLIT)
            else:
                print(HIT)
        elif CARD1 == CARD2 and CARD2 == 8:
            if DEALER <= 7:
                print(SPLIT)
            else:
                print(HIT)
        elif CARD1 == CARD2 and CARD2 == 9:
            if DEALER == 7 or DEALER == 10 or DEALER == 1:
                print(STAND)
            else:
                print(SPLIT)
        elif CARD1 == 1 or CARD2 == 1:
            if CARD1 >= 8 or CARD2 >= 8:
                print(STAND)
            elif CARD1 == 2 or CARD1 == 3 or CARD2 == 2 or CARD2 == 3:
                if DEALER == 5 or DEALER == 6:
                    print(DOUBLE)
                else:
                    print(HIT)
            elif CARD1 == 4 or CARD1 == 5 or CARD2 == 4 or CARD2 == 5:
                if DEALER >= 4 and DEALER <= 6:
                    print(DOUBLE)
                else:
                    print(HIT)
            elif CARD1 == 6 or CARD2 == 6:
                if DEALER >= 3 and DEALER <= 6:
                    print(DOUBLE)
                else:
                    print(HIT)
            elif CARD1 == 7 or CARD2 == 7:
                if DEALER >= 3 and DEALER <= 6:
                    print(DOUBLE)
                elif DEALER == 2 or DEALER == 7 or DEALER == 8:
                    print(STAND)
                else:
                    print(HIT)
        else:
            CARDX = CARD1 + CARD2
            if CARDX <= 8:
                print(HIT)
            elif CARDX >= 17:
                print(STAND)
            elif CARDX == 9:
                if DEALER >= 3 and DEALER <= 6:
                    print(DOUBLE)
                else:
                    print(HIT)
            elif CARDX == 10:
                if DEALER >= 2 and DEALER <= 9:
                    print(DOUBLE)
                else:
                    print(HIT)
            elif CARDX == 11:
                if DEALER >= 2 and DEALER <= 10:
                    print(DOUBLE)
                else:
                    print(HIT)
            elif CARDX == 12:
                if DEALER >= 4 and DEALER <= 6:
                    print(STAND)
                else:
                    print(HIT)
            elif CARDX >= 13 and CARDX <= 16:
                if DEALER >= 2 and DEALER <= 6:
                    print(STAND)
                else:
                    print(HIT)

    PLAYING = False

__author__ = "Jinco"
__copyright__ = "Copyright 2017, Jinco"
__license__ = "GPL-3.0"
__version__ = "0.0.1"
__maintainer__ = "Jinco"
__status__ = "Development"
