from language_parser import *
from room_setup import *
from terminal import clear_screen, newline
import time


def main_room(room, rooms, objects, inventory):
    available_nav, available_objs, object_names = room_setup_objs(room, objects)
    print_room_details(rooms, available_nav, available_objs, room)
    print_interactive_objs(objects, room.get_index())
    room.set_visited_true()

    while True:
        newline()
        user_input = input(" What would you like to do? ").lower().strip().split()
        if len(user_input) == 0:
            continue

        if user_input[0] == 'q':
            break

        parsed_input = parse_input(user_input, inventory)

        if parsed_input is not None:
            action_type, option = parsed_input

            if action_type == "navigate":
                next_room = navigate(option, rooms)
                if next_room is not None:
                    describe_exit()
                    return next_room

            else:
                try_action(available_nav, rooms, room, action_type, option, objects, object_names, inventory)


def navigate(desired_location, rooms):
    available_rooms = [room.get_index() for room in rooms if room.is_visible()]
    if desired_location.isnumeric():
        door_index = int(desired_location)
        if door_index in available_rooms:
            room = rooms[door_index]
            return approach_door(room)


def describe_exit():
    clear_screen()
    print("As you leave the main room . . . description.")
    time.sleep(3)
