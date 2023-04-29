from language_parser import parse_input, describe_walls, describe_features, try_action
from terminal import clear_screen, newline
import time


def main_room(homebase, rooms, objects, inventory):
    available_nav = []
    available_objs = [item for item in objects if item.get_location() == 0]
    object_names = [item.get_name().lower() for item in available_objs]
    clear_screen()
    newline()
    print('', homebase.get_desc())
    describe_walls(rooms, available_nav)
    describe_features(available_objs, homebase.get_index())
    homebase.set_visited_true()
    # describe_features(objects)

    while True:
        newline()
        user_input = input(" What would you like to do? ").lower().strip().split()
        if len(user_input) == 0:
            continue

        if user_input[0] == 'q':
            break

        parsed_input = parse_input(user_input)

        if parsed_input is not None:
            action_type, option = parsed_input

            if action_type == "navigate":
                next_room = navigate(option, available_nav, rooms)
                if next_room is not None:
                    describe_exit()
                    return next_room

            else:
                try_action(available_nav, rooms, homebase, action_type, option, objects, object_names, inventory)

        else:
            print("Not a recognized command")


def navigate(desired_location, available_nav, rooms):
    if desired_location.isnumeric():
        door_index = int(desired_location)
        if door_index in available_nav:
            room = rooms[door_index]
            return approach_door(room)


def approach_door(room):
    if room.is_locked():
        print(" You approach the door but as you turn the handle you realize it is locked.")
        return None

    else:
        print(" You approach the door turn the handle and step into the room.")
        return room


def describe_exit():
    clear_screen()
    print("As you leave the main room . . . description.")
    time.sleep(3)
