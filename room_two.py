from language_parser import *
from room_setup import *


def room_two(room, rooms, objects, inventory):
    available_nav, available_objs, object_names = room_setup_objs(room, objects)
    print_room_details(rooms, available_nav, available_objs, room)
    print_interactive_objs(objects, room.get_index())

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



