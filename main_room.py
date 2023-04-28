from language_parser import parse_input
from terminal import clear_screen, newline
import time


def main_room(homebase, rooms, objects, inventory):
    clear_screen()
    newline()
    available_nav = []
    print('', homebase.get_desc())
    describe_walls(rooms, available_nav)
    describe_features(objects)
    homebase.set_visited_true()
    # describe_features(objects)

    while True:
        newline()
        user_input = input(" What would you like to do? ").lower().strip().split()

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

            # TODO if action_type = "action"

        else:
            print("Not a recognized command")


def describe_walls(rooms, available_nav):
    newline()
    visible_rooms = 0
    print(" When you look at the walls around you, you see: ")
    newline()

    for index, room in enumerate(rooms):
        if room.is_visible():
            visible_rooms += 1
            available_nav.append(index)
            print(f" Navigation Option ({index}) : {room.get_door_desc()} that is located {room.get_direction()}.")

    if not visible_rooms:
        print("Nothing ... on the walls")


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


def describe_features(objects):
    newline()
    print(" Interactive Objects: ")
    for index, feature in enumerate(objects):
        if feature.get_location() == 0:
            print(f" Interaction Option ({index}) {feature.get_name()}")


def describe_exit():
    clear_screen()
    print("As you leave the main room . . . description.")
    time.sleep(3)



