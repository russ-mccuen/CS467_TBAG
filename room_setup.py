from terminal import *


def describe_exit():
    newline()
    print(" You are also aware of the door that will lead you back to the main room: ")
    print(f" Navigation Option (1) :  The door heading back to the main room that is located south.")
    newline()


def room_setup_objs(room, objects):
    room_index = room.get_index()
    available_nav = []
    available_objs = [item for item in objects if item.get_location() == room_index]
    object_names = [item.get_name().lower() for item in available_objs]
    return available_nav, available_objs, object_names


def print_room_details(rooms, available_nav, available_objs, room):
    room_index = room.get_index()
    clear_screen()
    newline()
    print('', room.get_desc())
    describe_features(available_objs, room.get_index())

    if room_index == 0:
        describe_walls(rooms, available_nav)
    else:
        describe_exit()


def describe_walls(rooms, available_nav):
    newline()
    visible_rooms = 0

    for index, room in enumerate(rooms):
        if room.is_visible():
            visible_rooms += 1
            available_nav.append(index)
            print(f" Navigation Option ({index}) : {room.get_door_desc()} that is located {room.get_direction()}.")

    if not visible_rooms:
        print(" There is no door to the room. Actually, you can not see any "
              "way of either entering or "
              "exiting the room.\n There are not even any windows. You know you have a window in your room.\n "
              "At least you think you do.")


def describe_features(objects, room_num):
    print(" As you look around the room you notice: ")
    newline()
    for obj in objects:
        if obj.get_location() == room_num and not obj.is_movable():
            print(obj.get_short_desc())


def describe_exiting_room(room, inventory):
    room_index = room.get_index()
    inv_names = [obj.get_name().lower() for obj in inventory]
    clear_screen()
    if room_index == 0:
        print("You blink and suddenly everything around you has changed.")

    if room_index == 1:
        if "remote" not in inv_names:
            print(" As you leave the room you have the feeling that you may "
                  "have forgotten something.")
        else:
            print(" You would like to stay in your childhood bedroom, "
                  "but you need to figure out what is going on.")

    if room_index == 2:
        print(" You'd love to stay and dance a little more, but you know "
              "there is more to do.")

    time.sleep(1)


def navigate_from_main(desired_location, rooms):
    available_rooms = [room.get_index() for room in rooms if room.is_visible()]
    if desired_location.isnumeric():
        door_index = int(desired_location)
        if door_index in available_rooms:
            room = rooms[door_index]
            return approach_door(room)


def navigate(desired_location, rooms):
    if desired_location.isnumeric():
        door_index = int(desired_location)
        if door_index is 1:
            room = rooms[0]
            return approach_door(room)
        else:
            print("That option does not exist.")


def approach_door(room):
    if room.is_locked():
        print(" You approach the door but as you turn the handle you realize it is locked.")
        return None

    else:
        clear_screen()
        print(" You approach the door turn the handle and step into the room.")
        time.sleep(1)
        return room


def print_interactive_objs(objects, room_num):
    newline()
    print(" Interactive Objects:")
    for index, obj in enumerate(objects):
        if obj.get_location() == room_num and not obj.is_movable():
            print(f" Option: {obj.get_name()}")
