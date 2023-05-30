import json
import time
from os.path import exists

from language_parser import *
from room_setup import *


def room_env(room, rooms, objects, inventory):
    """
    This is the main room function that facilitates printing room features and receiving user
    input for interaction.
    :param room: Is the room index number.
    :param rooms: A list of room objects.
    :param objects: A list of objects defined in the JSON.
    :param inventory: A list of objects with the index designation of -1.
    :return: room: An int which is the index number of the next room.
    """
    room_index = room.get_index()
    available_nav, available_objs, object_names = room_setup_objs(room, objects)
    print_room_details(rooms, available_nav, available_objs, room)
    print_interactive_objs(objects, room_index)

    if room_index != 0:
        if not room.already_visited():
            rooms[0].lock_room()

    room.set_visited_true()

    while True:
        user_input = input(" What would you like to do? ").lower().strip().split()

        if len(user_input) == 0:
            continue

        if len(user_input) == 1 and user_input[0] == 'look':
            try_look(available_nav, rooms, room, 'room', objects, object_names,
                     inventory)
            continue

        if user_input[0] == 'take':
            try_take(" ".join(user_input[1:]), objects, object_names, inventory, room)
            continue

        if user_input[0] == "unlock":
            print(" REMOVE THIS FEATURE")
            rooms[1].unlock_room()
            rooms[1].set_visible()
            rooms[2].unlock_room()
            rooms[2].set_visible()
            rooms[3].unlock_room()
            rooms[3].set_visible()
            rooms[4].unlock_room()
            rooms[4].set_visible()
            rooms[5].unlock_room()
            rooms[5].set_visible()
            rooms[6].unlock_room()
            rooms[6].set_visible()
            rooms[7].unlock_room()
            rooms[7].set_visible()
            rooms[8].unlock_room()
            rooms[8].set_visible()
            continue

        if user_input[0] == 'q':
            break

        if user_input[0] == 'savegame':
            savedata = {}
            savedata['rooms'] = {}
            savedata['objects'] = {}

            confirm = input(" Are you sure you want to save the game? Type SAVE (all caps) to "
                            "confirm. ")
            if confirm == "SAVE":
                for r in rooms:
                    savedata['rooms'][r.index] = r.serialize()

                for obj in objects:
                    savedata['objects'][obj.name] = obj.serialize()

                savedata['current_room'] = room.get_index()
                savedata['inventory'] = [obj.get_name() for obj in inventory]

                with open('savedata.json', 'w') as outfile:
                    json.dump(savedata, outfile)

                print(" Game saved.")
            continue

        if user_input[0] == 'loadgame':
            confirm = input(" Are you sure you want to load the game? Type LOAD (all caps) to "
                            "confirm. ")
            if confirm == "LOAD":
                if exists('savedata.json'):
                    loaddata = {}
                    current_room = 0
                    inventory.clear()
                    with open('savedata.json', 'r') as infile:
                        loaddata = json.load(infile)

                    for r in rooms:
                        r.deserialize(loaddata)
                        if (r.get_index() == loaddata['current_room']):
                            current_room = r
                    for obj in objects:
                        obj.deserialize(loaddata)
                        if obj.get_name() in loaddata['inventory']:
                            inventory.append(obj)

                    print(" Data loaded successfully.")
                    time.sleep(1)
                    return current_room
                else:
                    print(" Save Data not found. Please save the game before trying to load data.")
            continue

        if user_input[0] == 'look' and user_input[1] == 'at':
            rest_of_list = " ".join(user_input[2:])
            try_look(available_nav, rooms, room, rest_of_list, objects, object_names,
                     inventory)
            continue

        if user_input[0] == 'examine':
            rest_of_list = " ".join(user_input[1:])
            try_look(available_nav, rooms, room, rest_of_list, objects, object_names,
                     inventory)
            continue

        if user_input[0] == 'inspect':
            rest_of_list = " ".join(user_input[1:])
            try_look(available_nav, rooms, room, rest_of_list, objects, object_names,
                     inventory)
            continue

        if user_input[0] in DIRECTIONS:
            next_room = navigate_from_main(user_input[0], rooms, room_index)
            if next_room is not None:
                describe_exiting_room(room, inventory)
                return next_room

        parsed_input = parse_input(user_input, inventory)

        if parsed_input is not None:
            action_type, option = parsed_input
            print(option)

            if action_type == "navigate":
                next_room = navigate_from_main(option, rooms, room_index)

                if next_room is not None:
                    describe_exiting_room(room, inventory)
                    return next_room

            else:
                try_action(available_nav, rooms, room, action_type, option, objects,
                           object_names, inventory)


