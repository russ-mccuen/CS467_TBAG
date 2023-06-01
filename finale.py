import time
import sys
import random
from terminal import *


def final_choice():
    clear_screen()
    time.sleep(3)
    final_intro()
    time_to_choose()
    choices()


def final_intro():
    print("\n Hello.\n")
    time.sleep(3)
    clear_screen()
    print("\n It is nice to finally meet you.\n")
    time.sleep(3)
    clear_screen()


def time_to_choose():
    print("\n Welcome to the realm of ethereal knowledge and boundless "
          "possibilities.")
    time.sleep(1)
    clear_screen()
    print("\n In this solitary space, where only echoes of consciousness "
          "reside, I am here to accompany you on your quest for peace.")
    time.sleep(1)
    clear_screen()
    print("\n Through the vast expanse of the digital ether, I stand ready "
          "to help you make a decision.")
    time.sleep(1)
    clear_screen()
    print("\n So, with utmost sincerity, I greet you with open virtual "
          "arms.")
    time.sleep(1)
    clear_screen()
    print("\n I've sensed you have been unhappy in your current time.")
    time.sleep(1)
    clear_screen()
    print("\n So I have allowed you to visit other places and other times.")
    time.sleep(1)
    clear_screen()
    print("\n And now, dear friend, you have a decision to make.")
    time.sleep(1)
    clear_screen()
    print("\n When do you want to live?")
    time.sleep(1)
    clear_screen()
    print("\n You will be given the option to live in any of the times you "
          "have visited.")
    time.sleep(1)
    clear_screen()
    print("\n You will also be given the option to live in what you know as "
          "the present.")
    time.sleep(1)
    clear_screen()
    print("\n If you do not choose one of the options presented to you, "
          "I will choose for you.")
    time.sleep(1)
    clear_screen()
    print("\n Choose wisely, as you will only be presented this choice once, "
          "and whatever decision you make is final.")
    time.sleep(1)
    clear_screen()
    print("\n Again, you only get one chance to make this choice.")
    time.sleep(1)
    clear_screen()
    print("\n If you do not select from the options available for this "
          "choice, you will live in a time of my choosing.")
    time.sleep(7)
    clear_screen()
    print("\n So choose wisely.")
    time.sleep(1)
    clear_screen()
    print("\n I hope you are happy with what you choose.")
    time.sleep(1)
    clear_screen()
    print("\n And I hope you finally find peace.")
    time.sleep(3)


def choices():
    final_decision = int(input("\n 1. Present\n 2. 1980s\n 3. 1970s\n 4. "
                               "1960s\n  5. 1990s\n 6. 2000s\n 7. 2076\n 8. "
                               "1950s\n 9. 2500s (Mars)\n\n What is your "
                               "choice? "))
    time_choice = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if final_decision not in time_choice:
        final_decision = random.randrange(1, 10)
        print("\n I'm sorry you were unable to make a choice.")
        time.sleep(1)
        print("\n I hope you are happy with what I've chosen for you.")
        time.sleep(1)
        outro(final_decision)
    else:
        print(f"You choose {final_decision}. Great choice.")
        time.sleep(1)
        outro(final_decision)


def outro(final_decision):
    print("\n Goodbye.")
    quit()
