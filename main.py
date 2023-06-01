from game_setup import load_game, load_rooms, load_objects
from room_one import room_env
from terminal import *
import time


def main():
    clear_screen()
    #loading_screen()
    clear_screen()
    menu()
    choice = start_screen()
    if choice:
        start_game()
    elif choice == "2":
        start_game(True)


def start_game(load=False):
    """
    The main function that reads loads all the game information from the JSON file to initialize game objects.
    """
    #if not load:
     #   intro()

    inventory = []
    game_data = load_game("game.Json")
    rooms = load_rooms(game_data)
    objects = load_objects(game_data, inventory)
    current_room = rooms[game_data["Current Room"]]

    while current_room is not None:

        current_room = room_env(current_room, rooms, objects, inventory, load)
        if load:
            load = False

    print(" Exiting Game")


def intro():
    print("\n Headline: Still No Deal On Debt Ceiling")
    time.sleep(3)
    clear_screen()
    print("\n      Headline: What Will Be The Next COVID?")
    time.sleep(3)
    clear_screen()
    print("\n Headline: America Is More Polarized Than Ever")
    time.sleep(3)
    clear_screen()
    print("\n      Headline: Interest Rates Hit Record Highs")
    time.sleep(2)
    clear_screen()
    print("\n    Headline: This Generation Worse Off Than Previous Generation")
    time.sleep(2)
    clear_screen()
    print("\n Headline: Click to See Which Food is Actually BAD For You!")
    time.sleep(2)
    clear_screen()
    print("\n     Headline: Click to See Which Food is Actually GOOD For You!")
    time.sleep(1)
    clear_screen()
    print("\n Headline: Video Games Good For Mental Health")
    time.sleep(1)
    clear_screen()
    print("\n     Headline: Are Video Games the Cause of Increased Violence?")
    time.sleep(1)
    clear_screen()
    print("\n Headline: People Less Trustful Than Ever")
    time.sleep(1)
    clear_screen()
    print("\n     Headline: People Are Lonelier Than Ever")
    time.sleep(1)
    clear_screen()
    print("\n Headline: People Are More Depressed Than Ever")
    time.sleep(1)
    clear_screen()
    print("")
    time.sleep(3)
    clear_screen()
    print("\n The time would not pass. Somebody was playing with the clocks, "
          "and not only the electronic clocks but the wind-up kind too. The "
          "second hand on my watch would twitch once, and a year would pass, "
          "and then it would twitch again. There was nothing I could do "
          "about it. As an Earthling I had to believe whatever clocks said "
          "-and calendars.\n\n ― Kurt Vonnegut, Slaughterhouse-Five ")
    time.sleep(10)
    clear_screen()
    print("\n You slept better last night than you have in a very long time.")
    time.sleep(3)
    clear_screen()
    print("\n You slowly open your eyes . . .")
    time.sleep(3)
    clear_screen()



if __name__ == "__main__":
    main()
