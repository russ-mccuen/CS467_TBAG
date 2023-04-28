import os
import time
from game_setup import load_game, load_rooms, load_objects
from main_room import main_room


def loading_screen():
    # Display loading screen animation
    print("Loading game...")
    for i in range(1, 11):
        time.sleep(0.5)
        print("Loading" + "." * i)
    print("Game loaded!")


def menu():
    # Display game menu
    time.sleep(1.5)
    clear_screen()
    print("Welcome to Adam and Russ' Awesome Text-Based Adventure Game!")
    print("1. Start game")
    print("2. Options")
    print("3. Quit")


def main():
    loading_screen()
    menu()
    while True:
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            print("Starting game...")
            clear_screen()
            start_game()
            break
        elif choice == "2":
            print("Options menu...")
            # TODO: Add options code here
            break
        elif choice == "3":
            print("Exiting game...")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 3.")


def start_game():
    game_data = load_game("game.Json")
    rooms = load_rooms(game_data)
    objects = load_objects(game_data)
    current_room = rooms[game_data["Current Room"]]

    while True:
        if current_room.get_index() == 0:
            main_room(current_room, rooms)
        break



def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
