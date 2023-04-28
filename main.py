import time
from game_setup import load_game, load_rooms, load_objects
from main_room import main_room
from terminal import clear_screen, menu, start_screen


def loading_screen():
    # Display loading screen animation
    print("Loading game...")
    for i in range(1, 11):
        time.sleep(0.5)
        print("Loading" + "." * i)
    print("Game loaded!")


def main():
    loading_screen()
    menu()
    if start_screen():
        start_game()


def start_game():
    game_data = load_game("game.Json")
    rooms = load_rooms(game_data)
    objects = load_objects(game_data)
    current_room = rooms[game_data["Current Room"]]
    inventory = []

    while True:
        if current_room.get_index() == 0:
            current_room = main_room(current_room, rooms, objects, inventory)

        if current_room.get_index() == 1:
            print("Next Room")

        print("game exiting")
        break


if __name__ == "__main__":
    main()
