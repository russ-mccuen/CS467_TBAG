from language_parser import parse_input
from terminal import clear_screen, newline


def room_two(room, rooms, objects, inventory):
    clear_screen()
    newline()
    print('', room.get_desc())
    describe_walls()
    room.set_visited_true()
    # describe_features(objects)

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
