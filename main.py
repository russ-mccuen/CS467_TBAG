import time
from game_setup import load_game, load_rooms, load_objects
from main_room import main_room
from room_one import room_one
from room_two import room_two
from terminal import clear_screen, menu, start_screen


def loading_screen():
    # Display loading screen animation
    print("Loading game...")
    for i in range(1, 11):
        time.sleep(0.5)
        print("Loading" + "." * i)
    print("Game loaded!")


def main():
    # Commenting out the loading screen for now. Will re implement when we have load options.
    # loading_screen()
    # menu()
    # if start_screen():
    #     start_game()
    start_game()


def start_game():
    game_data = load_game("game.Json")
    rooms = load_rooms(game_data)
    objects = load_objects(game_data)
    current_room = rooms[game_data["Current Room"]]
    inventory = []

    while current_room is not None:
        if current_room.get_index() == 0:
            current_room = main_room(current_room, rooms, objects, inventory)

        if current_room is not None and current_room.get_index() == 1:
            current_room = room_one(current_room, rooms, objects, inventory)

        if current_room is not None and current_room.get_index() == 2:
            current_room = room_two(current_room, rooms, objects, inventory)

    print(" Exiting Game")


if __name__ == "__main__":
    main()
