from Room import Room
import time
import json


def loading_screen():
    # Display loading screen animation
    print("Loading game...")
    for i in range(1, 11):
        time.sleep(0.5)
        print("Loading" + "." * i)
    print("Game loaded!")
    # Display game menu
    print("Welcome to Adam and Russ' Awesome Text-Based Adventure Game!")
    print("1. Start game")
    print("2. Options")
    print("3. Quit")


def main():
    # loading_screen()
    start_game()
    # while True:
    #     choice = input("Enter your choice (1-3): ")
    #     if choice == "1":
    #         print("Starting game...")
    #         start_game()
    #         break
    #     elif choice == "2":
    #         print("Options menu...")
    #         # TODO: Add options code here
    #         break
    #     elif choice == "3":
    #         print("Exiting game...")
    #         break
    #     else:
    #         print("Invalid input. Please enter a number between 1 and 3.")


def start_game():
    game_data = load_game("game.Json")


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


if __name__ == "__main__":
    main()
