from language_parser import *
from terminal import clear_screen, newline


def room_one(room, rooms, objects, inventory):
    available_nav = []
    available_objs = [item for item in objects if item.get_location() == 1]
    object_names = [item.get_name().lower() for item in available_objs]
    clear_screen()
    newline()
    print('', room.get_desc())
    describe_walls()
    describe_features(available_objs, room.get_index())

    # This is for locking the main room. Try it out.
    if not room.already_visited():
        rooms[0].lock_room()

    room.set_visited_true()

    while True:
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
                    describe_exit(inventory)
                    return next_room

            else:
                try_action(available_nav, rooms, room, action_type, option, objects, object_names, inventory)


def navigate(desired_location, rooms):
    if desired_location.isnumeric():
        door_index = int(desired_location)
        if door_index is 1:
            room = rooms[0]
            return approach_door(room)
        else:
            print("That option does not exist.")


def describe_walls():
    newline()
    print(" You are also aware of the door that will lead you back to the main room: ")
    print(f" Navigation Option (1) :  The door heading back to the main room that is located south.")
    newline()


def describe_exit(inventory):
    inv_names = [obj.get_name().lower() for obj in inventory]
    clear_screen()
    if "remote" not in inv_names:
        print("As you leave the room you have the feeling that you may have forgotten something.")
    else:
        print("As you leave the main room . . . description.")
    time.sleep(3)
