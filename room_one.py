import json
import sys
import time
from os.path import exists
from language_parser import *
from room_setup import *
from terminal import *
from finale import *


def room_env(room, rooms, objects, inventory, load):
    """
    This is the main room function that facilitates printing room features and receiving user
    input for interaction.
    :param room: Is the room index number.
    :param rooms: A list of room objects.
    :param objects: A list of objects defined in the JSON.
    :param inventory: A list of objects with the index designation of -1.
    :return: room: An int which is the index number of the next room.
    """
    if load:
        return load_game(inventory, objects, rooms)

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

        if room_index == 9:
            if user_input[0] != 'wait':
                print("\n Patience is the key. When in doubt . . .\n")
                continue
            else:
                final_choice()
        if len(user_input) == 0:
            continue

        clear_screen()

        if len(user_input) == 1 and user_input[0] == 'look':
            try_look(available_nav, rooms, room, 'room', objects, object_names,
                     inventory)
            continue

        if user_input[0] == 'take':
            try_take(" ".join(user_input[1:]), objects, object_names, inventory, room)
            continue

        # if user_input[0] == "unlock":
        #     print(" REMOVE THIS FEATURE")
        #     rooms[1].unlock_room()
        #     rooms[1].set_visible()
        #     rooms[2].unlock_room()
        #     rooms[2].set_visible()
        #     rooms[3].unlock_room()
        #     rooms[3].set_visible()
        #     rooms[4].unlock_room()
        #     rooms[4].set_visible()
        #     rooms[5].unlock_room()
        #     rooms[5].set_visible()
        #     rooms[6].unlock_room()
        #     rooms[6].set_visible()
        #     rooms[7].unlock_room()
        #     rooms[7].set_visible()
        #     rooms[8].unlock_room()
        #     rooms[8].set_visible()
        #     continue

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
                return load_game(inventory, objects, rooms)
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

        if user_input[0] == 'jump' and room.get_index() != 8:
            print("\n Yay! You jumped so high! Good job!\n\n")
            continue

        if user_input[0] == 'eat' and (room.get_index() != 4 or
                                       room.get_index() != 7):
            print("\n Sorry. There is nothing to eat here.\n\n")
            continue

        if user_input[0] == 'wear' and room.get_index() != 7:
            print("\n You already have on clothes.\n\n")
            continue

        if user_input[0] == 'swim' and room.get_index() != 6:
            print("\n Ummmmm . . . where are you going to swim?\n\n")
            continue

        if user_input[0] == 'dance' and room.get_index() != 2:
            print("\n You bust a move.\n\n")
            continue

        if user_input[0] in ['nap', 'sleep', 'rest']:
            valid_input = False
            while not valid_input:
                rest_time = input("\n How many hours would you like to "
                                  "sleep? ")
                if rest_time.isnumeric():
                    print(f"\n You sleep for {rest_time} hours.\n\n")
                    valid_input = True
                else:
                    print("\n Seriously? Enter a number, please.\n\n")
            continue

        if user_input[0] in ['think', 'ponder', 'reminisce']:
            print("\n You are not sure how to proceed, so you decide to stop "
                  "and think about what you should do next. It works! You "
                  "now know what you have to do.\n\n")
            continue

        if (user_input[0] == "play" or user_input[0] == "use") and \
                user_input[1] == 'vhs':
            play_vhs(room, inventory)
            continue


        if user_input[0] in DIRECTIONS:
            next_room = navigate_from_main(user_input[0], rooms, room_index)
            if next_room is not None:
                describe_exiting_room(room, inventory)
                return next_room

        parsed_input = parse_input(user_input, inventory)

        if parsed_input is not None:
            action_type, option = parsed_input

            if action_type == "navigate":
                next_room = navigate_from_main(option, rooms, room_index, inventory)

                if next_room is not None:
                    return next_room

            else:
                try_action(available_nav, rooms, room, action_type, option, objects,
                           object_names, inventory)


def load_game(inventory, objects, rooms):
    if exists('savedata.json'):
        loaddata = {}
        current_room = 0
        inventory.clear()
        with open('savedata.json', 'r') as infile:
            loaddata = json.load(infile)

        for r in rooms:
            r.deserialize(loaddata)
            if r.get_index() == loaddata['current_room']:
                current_room = r
        for obj in objects:
            obj.deserialize(loaddata)
            if obj.get_name() in loaddata['inventory']:
                inventory.append(obj)

        print(" Data loaded successfully.")
        time.sleep(1)
        return current_room
    else:
        print(
            " Save Data not found. Please save the game before trying to "
            "load data.")
