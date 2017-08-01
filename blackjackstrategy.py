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

    # Make sure we're using Python 3+
    if sys.version_info < (3, 0):
        print(
            Colour.RED +
            "This app requires Python 3! Please reload with: python3 blackjackstrategy.py" +
            Colour.END)
        sys.exit(1)

    # Define our actions
    SPLIT = Colour.BLUE + Colour.BOLD + "SPLIT" + Colour.END
    HIT = Colour.GREEN + Colour.BOLD + "HIT" + Colour.END
    STAND = Colour.YELLOW + Colour.BOLD + "STAND" + Colour.END
    DOUBLE = Colour.PURPLE + Colour.BOLD + "DOUBLE" + Colour.END

    # Get inputs
    T1 = True
    T2 = False
    T3 = False

    while T1:
        try:
            DEALER = int(
                input('What is the dealer\'s card? (Ace = 1. J,Q,K = 10.)\n'))
            while DEALER not in range(1, 11):
                DEALER = input(
                    Colour.RED +
                    "Enter a number between 1 and 10. (Ace = 1; J,Q,K = 10)\n" +
                    Colour.END)
            cleanscreen()
            T1 = False
            T2 = True
        except ValueError:
            cleanscreen()
            print(Colour.RED + "Please only use numbers.\n" + Colour.END)

    while T2:
        try:
            CARD1 = int(
                input('What is your first card? (Ace = 1; J,Q,K = 10)\n'))
            while CARD1 not in range(1, 11):
                CARD1 = input(
                    Colour.RED +
                    "Enter a number between 1 and 10. (Ace = 1; J,Q,K = 10)\n" +
                    Colour.END)
            cleanscreen()
            T2 = False
            T3 = True
        except ValueError:
            cleanscreen()
            print(Colour.RED + "Please only use numbers.\n" + Colour.END)

    while T3:
        try:
            CARD2 = int(
                input('What is your second card? (Ace = 1; J,Q,K = 10)\n'))
            while CARD2 not in range(1, 11):
                CARD2 = input(
                    Colour.RED +
                    "Enter a number between 1 and 10. (Ace = 1; J,Q,K = 10)\n" +
                    Colour.END)
            cleanscreen()
            T3 = False
        except ValueError:
            cleanscreen()
            print(Colour.RED + "Please only use numbers.\n" + Colour.END)

    # Decide result
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
        elif CARD1 in (2, 3) or CARD2 in (2, 3):
            if DEALER in (5, 6):
                print(DOUBLE)
            else:
                print(HIT)
        elif CARD1 in (4, 5) or CARD2 in (4, 5):
            if DEALER in range(4, 7):
                print(DOUBLE)
            else:
                print(HIT)
        elif CARD1 == 6 or CARD2 == 6:
            if DEALER in range(3, 7):
                print(DOUBLE)
            else:
                print(HIT)
        elif CARD1 == 7 or CARD2 == 7:
            if DEALER in range(3, 7):
                print(DOUBLE)
            elif DEALER in (2, 7, 8):
                print(STAND)
            else:
                print(HIT)
        elif CARD1 in range(8, 11) or CARD2 in range(8, 11):
            print(STAND)

    # Pairs
    elif CARD1 == CARD2:
        if CARD1 == 8:
            print(SPLIT)
        elif CARD1 == 10:
            print(STAND)
        elif CARD1 in (2, 3, 8):
            if DEALER in range(2, 8):
                print(SPLIT)
            else:
                print(HIT)
        elif CARD1 == 4:
            if DEALER in (5, 6):
                print(SPLIT)
            else:
                print(HIT)
        elif CARD1 == 5:
            if DEALER in range(2, 10):
                print(DOUBLE)
            else:
                print(HIT)
        elif CARD1 == 6:
            if DEALER in range(2, 7):
                print(SPLIT)
            else:
                print(HIT)
        elif CARD1 == 9:
            if DEALER in (1, 7, 10):
                print(STAND)
            else:
                print(SPLIT)

    # Other
    elif CARDX in range(5, 9):
        print(HIT)
    elif CARDX >= 17:
        print(STAND)
    elif CARDX in range(13, 17):
        if DEALER in range(2, 7):
            print(STAND)
        else:
            print(HIT)
    elif CARDX == 9:
        if DEALER in range(3, 7):
            print(DOUBLE)
        else:
            print(HIT)
    elif CARDX == 10:
        if DEALER in range(3, 10):
            print(DOUBLE)
        else:
            print(HIT)
    elif CARDX == 11:
        if DEALER in range(3, 11):
            print(DOUBLE)
        else:
            print(HIT)
    elif CARDX == 12:
        if DEALER in range(4, 7):
            print(STAND)
        else:
            print(HIT)

    # Error
    else:
        print("ERROR!")

    REPEAT = input('\nAnother hand? y/n\n').lower()
    if REPEAT != "y":
        cleanscreen()
        PLAYING = False
    else:
        cleanscreen()

__author__ = "Jinco"
__copyright__ = "Copyright 2017, Jinco"
__license__ = "GPL-3.0"
__version__ = "0.0.4"
__maintainer__ = "Jinco"
__status__ = "Development"
