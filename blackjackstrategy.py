#!/usr/bin/env python3
"""Blackjack Strategy"""

import os
import sys

PLAYING = True


class Colour:
    """Define text colours"""
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
    """ Clear the screen"""
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
    return


while PLAYING:
    cleanscreen()

    if sys.version_info < (3, 0):
        print(
            Colour.RED +
            "This app requires Python 3! Please reload with: python3 blackjackstrategy.py"
            + Colour.END)
        sys.exit(1)

    SPLIT = Colour.BLUE + "SPLIT" + Colour.END
    HIT = Colour.GREEN + "HIT" + Colour.END
    STAND = Colour.YELLOW + "STAND" + Colour.END
    DOUBLE = Colour.PURPLE + "DOUBLE" + Colour.END

    DEALER = int(input('What is the dealers card? (Ace = 1)\n'))

    while DEALER > 10 or DEALER < 1:
        DEALER = int(
            input(
                Colour.RED +
                "Enter a number between 1 and 10. Ace = 1.\n" +
                Colour.END))

    CARD1 = int(input('What is your first card? (Ace = 1)\n'))

    while CARD1 > 10 or CARD1 < 1:
        CARD1 = int(
            input(
                Colour.RED +
                "Enter a number between 1 and 10. Ace = 1.\n" +
                Colour.END))

    CARD2 = int(input('What is your second card? (Ace = 1)\n'))

    while CARD2 > 10 or CARD2 < 1:
        CARD2 = int(
            input(
                Colour.RED +
                "Enter a number between 1 and 10. Ace = 1.\n" +
                Colour.END))

    if CARD1 == CARD2 == 1 or CARD2 == 8:
        print(SPLIT)
    elif CARD1 == CARD2 == 10:
        print(STAND)
    elif CARD1 == CARD2 == 2 or CARD2 == 3 or 7:
        if 2 <= DEALER <= 7:
            print(SPLIT)
        else:
            print(HIT)
    elif CARD1 == CARD2 == 4:
        if DEALER == 5 or 6:
            print(SPLIT)
        else:
            print(HIT)
    elif CARD1 == CARD2 == 5:
        if DEALER == 1 or 10:
            print(HIT)
        else:
            print(DOUBLE)
    elif CARD1 == CARD2 == 6:
        if DEALER <= 6:
            print(SPLIT)
        else:
            print(HIT)
    elif CARD1 == CARD2 == 7:
        if DEALER <= 7:
            print(SPLIT)
        else:
            print(HIT)
    elif CARD1 == CARD2 == 8:
        if DEALER <= 7:
            print(SPLIT)
        else:
            print(HIT)
    elif CARD1 == CARD2 == 9:
        if DEALER == 7 or 10 or 1:
            print(STAND)
        else:
            print(SPLIT)
    elif CARD1 == 1 or CARD2 == 1:
        if CARD1 >= 8 or CARD2 >= 8:
            print(STAND)
        elif CARD1 == 2 or 3 or CARD2 == 2 or 3:
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
            if 3 <= DEALER <= 6:
                print(DOUBLE)
            elif DEALER == 2 or 7 or 8:
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
                if 3 <= DEALER <= 6:
                    print(DOUBLE)
                else:
                    print(HIT)
            elif CARDX == 10:
                if 2 <= DEALER <= 9:
                    print(DOUBLE)
                else:
                    print(HIT)
            elif CARDX == 11:
                if 2 <= DEALER <= 10:
                    print(DOUBLE)
                else:
                    print(HIT)
            elif CARDX == 12:
                if 4 <= DEALER <= 6:
                    print(STAND)
                else:
                    print(HIT)
            elif CARDX >= 13 and CARDX <= 16:
                if DEALER >= 2 and DEALER <= 6:
                    print(STAND)
                else:
                    print(HIT)

    REPEAT = input('\nRepeat? y/n\n').lower()
    if REPEAT != "y":
        cleanscreen()
        PLAYING = False
    else:
        cleanscreen()

__author__ = "Jinco"
__copyright__ = "Copyright 2017, Jinco"
__license__ = "GPL-3.0"
__version__ = "0.0.2"
__maintainer__ = "Jinco"
__status__ = "Development"
