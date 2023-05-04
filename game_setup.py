from Room import Room
from objects import *
import json


def load_game(json_file):
    try:
        file = open(json_file, "r")
        data = json.load(file)
        file.close()
        return data

    except FileNotFoundError:
        raise FileNotFoundError

    except PermissionError:
        raise PermissionError


def load_rooms(game_data):
    rooms = []
    for index, room in enumerate(game_data["Rooms"]):
        room_index = index
        room_name = room["name"]
        door_desc = room["door desc"]
        short_desc = room["short desc"]
        long_desc = room["long desc"]
        is_locked = room["is locked"]
        feature_one = room["feature one"]
        feature_two = room["feature two"]
        is_visible = room["is visible"]
        direction = room["direction"]
        new_room = Room(index, room_name, door_desc, short_desc, long_desc, is_locked, feature_one,
                        feature_two, is_visible, direction)
        rooms.insert(index, new_room)
    return rooms


def load_objects(game_data, inventory):
    objects = []
    for game_obj in game_data["Game Objects"]:
        obj_name = game_obj["object name"]
        description = game_obj["description"]
        location = game_obj["location"]
        movable = game_obj["is movable"]
        if obj_name == "Tablet":
            new_obj = Tablet(obj_name, description, location, movable)

        elif obj_name == "Letter":
            new_obj = Letter(obj_name, description, location, movable)

        elif obj_name == "TV":
            new_obj = TV(obj_name, description, location, movable)

        elif obj_name == "Commodore":
            new_obj = Commodore(obj_name, description, location, movable)

        elif obj_name == "Remote":
            new_obj = Remote(obj_name, description, location, movable)

        else:
            new_obj = GameObject(obj_name, description, location, movable)
        objects.append(new_obj)
        if location == -1:
            inventory.append(new_obj)
    return objects
