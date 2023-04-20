import json
import os
import time
from Room import Room


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
    # This just shows that each room is an object in the rooms list.
    for index, room in enumerate(rooms):
        print(index, room)

    while True:
        user_input = input("What do you want to do?: ")
        if user_input.lower() == 'q':
            break

    # TODO Room Navigation Parser


def load_game(json_file):
    try:
        file = open(json_file, "r")
        data = json.load(file)
        file.close()
        return data

    except FileNotFoundError:
        raise FileNotFoundError

    except PermissionError:
        raise PermissionError


def load_rooms(game_data):
    rooms = []
    for room in game_data["Rooms"]:
        room_name = room["name"]
        short_desc = room["short desc"]
        long_desc = room["long desc"]
        is_locked = True if room["is locked"] == "True" else False
        new_room = Room(room_name, short_desc, long_desc, is_locked)
        rooms.append(new_room)
    return rooms


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
