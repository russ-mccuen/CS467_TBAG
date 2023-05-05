from language_parser import *
from terminal import clear_screen, newline


def room_two(room, rooms, objects, inventory):
    available_nav, available_objs, object_names = room_setup(objects)
    print_room_details(available_objs, room)

    while True:
        user_input = input(" What would you like to do? ").lower().strip().split()

        if user_input[0] == 'q':
            break

        parsed_input = parse_input(user_input, inventory)

        if parsed_input is not None:
            action_type, option = parsed_input

            if action_type == "navigate":
                next_room = navigate(option, rooms)
                if next_room is not None:
                    return next_room

            else:
                try_action(available_nav, rooms, room, action_type, option, objects, object_names, inventory)


def navigate(desired_location, rooms):
    if desired_location.isnumeric():
        door_index = int(desired_location)
        if door_index is 1:
            return rooms[0]
        else:
            print("That option does not exist.")


def describe_walls():
    newline()
    print(" You are also aware of the door that will lead you back to the main room: ")
    print(f" Navigation Option (1) :  The door heading back to the main room that is located south.")
    newline()


def room_setup(objects):
    available_nav = []
    available_objs = [item for item in objects if item.get_location() == 2]
    object_names = [item.get_name().lower() for item in available_objs]
    return available_nav, available_objs, object_names


def print_room_details(available_objs, room):
    clear_screen()
    newline()
    print('', room.get_desc())
    describe_walls()
    describe_features(available_objs, room.get_index())
