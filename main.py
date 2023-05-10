from game_setup import load_game, load_rooms, load_objects
from room_one import room_one


def main():
    start_game()
    # clear_screen()
    # loading_screen()
    # menu()
    # if start_screen():
    #     start_game()


def start_game():
    inventory = []
    game_data = load_game("game.Json")
    rooms = load_rooms(game_data)
    objects = load_objects(game_data, inventory)
    current_room = rooms[game_data["Current Room"]]

    while current_room is not None:

        current_room = room_one(current_room, rooms, objects, inventory)

    print(" Exiting Game")


if __name__ == "__main__":
    main()
