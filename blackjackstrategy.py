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
            "This app requires Python 3! Please reload with: python3 blackjackstrategy.py" +
            Colour.END)
        sys.exit(1)

    SPLIT = Colour.BLUE + Colour.BOLD + "SPLIT" + Colour.END
    HIT = Colour.GREEN + Colour.BOLD + "HIT" + Colour.END
    STAND = Colour.YELLOW + Colour.BOLD + "STAND" + Colour.END
    DOUBLE = Colour.PURPLE + Colour.BOLD + "DOUBLE" + Colour.END

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

    cleanscreen()
    print(
        Colour.DARKCYAN +
        "Dealer: {}. Cards: {} & {}.\n".format(DEALER, CARD1, CARD2) +
        Colour.END)
    print("In standard strategy with 4-8 decks, dealer stands on soft 17:")

    CARDX = CARD1 + CARD2

    # Aces
    if CARD1 == 1 or CARD2 == 1:
        if CARD1 == CARD2:
            print(SPLIT)
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
        elif CARD1 >= 8 and CARD1 <= 10 or CARD2 >= 8 and CARD2 <= 10:
            print(STAND)

    # Pairs
    elif CARD1 == CARD2:
        if CARD1 == 8:
            print(SPLIT)
        elif CARD1 == 10:
            print(STAND)
        elif CARD1 == 2 or CARD1 == 3 or CARD1 == 7:
            if DEALER >= 2 or DEALER <= 7:
                print(SPLIT)
            else:
                print(HIT)
        elif CARD1 == 4:
            if DEALER == 5 or DEALER == 6:
                print(SPLIT)
            else:
                print(HIT)
        elif CARD1 == 5:
            if DEALER >= 2 and DEALER <= 9:
                print(DOUBLE)
            else:
                print(HIT)
        elif CARD1 == 6:
            if DEALER >= 2 and DEALER <= 6:
                print(SPLIT)
            else:
                print(HIT)
        elif CARD1 == 9:
            if DEALER == 7 or DEALER == 10 or DEALER == 1:
                print(STAND)
            else:
                print(SPLIT)

    # Other
    elif CARDX >= 5 and CARDX <= 8:
        print(HIT)
    elif CARDX >= 17:
        print(STAND)
    elif CARDX >= 13 and CARDX <= 16:
        if DEALER >= 2 and DEALER <= 6:
            print(STAND)
        else:
            print(HIT)
    elif CARDX == 9:
        if DEALER >= 3 and DEALER <= 6:
            print(DOUBLE)
        else:
            print(HIT)
    elif CARDX == 10:
        if DEALER >= 3 and DEALER <= 9:
            print(DOUBLE)
        else:
            print(HIT)
    elif CARDX == 11:
        if DEALER >= 3 and DEALER <= 10:
            print(DOUBLE)
        else:
            print(HIT)
    elif CARDX == 12:
        if DEALER >= 4 and DEALER <= 6:
            print(STAND)
        else:
            print(HIT)

    # Error
    else:
        print("ERROR!")

    REPEAT = input('\nRepeat? y/n\n').lower()
    if REPEAT != "y":
        cleanscreen()
        PLAYING = False
    else:
        cleanscreen()

__author__ = "Jinco"
__copyright__ = "Copyright 2017, Jinco"
__license__ = "GPL-3.0"
__version__ = "0.0.3"
__maintainer__ = "Jinco"
__status__ = "Development"
