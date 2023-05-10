from language_parser import *
from room_setup import *


def room_one(room, rooms, objects, inventory):
    available_nav, available_objs, object_names = room_setup_objs(room, objects)
    print_room_details(rooms, available_nav, available_objs, room)
    print_interactive_objs(objects, room.get_index())

    room_index = room.get_index()

    if room_index != 0:
        if not room.already_visited():
            rooms[0].lock_room()

    room.set_visited_true()

    while True:
        user_input = input(" What would you like to do? ").lower().strip().split()

        if len(user_input) == 0:
            continue

        if user_input[0] == "unlock":
            print(" REMOVE THIS FEATURE")
            rooms[0].unlock_room()
            continue

        if user_input[0] == 'q':
            break

        parsed_input = parse_input(user_input, inventory)

        if parsed_input is not None:
            action_type, option = parsed_input

            if action_type == "navigate":
                if room_index == 0:
                    next_room = navigate_from_main(option, rooms)
                else:
                    next_room = navigate(option, rooms)

                if next_room is not None:
                    describe_exiting_room(room, inventory)
                    return next_room

            else:
                try_action(available_nav, rooms, room, action_type, option, objects, object_names, inventory)


