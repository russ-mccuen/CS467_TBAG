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
        if obj.get_location() == room_num and obj.is_visible():
            print(obj.get_short_desc())


def describe_exiting_room(room, inventory):
    room_index = room.get_index()
    inv_names = [obj.get_name().lower() for obj in inventory]
    clear_screen()
    if room_index == 0:
        print(" You blink and suddenly everything around you has changed.")

    if room_index == 1:
        if "remote" not in inv_names:
            print(" As you leave the room you have the feeling that you may "
                  "have forgotten something.")
        else:
            print(" You would like to stay in your childhood bedroom, "
                  "but you need to figure out what is going on.")

    if room_index == 2:
        print(" You'd love to stay and dance, but you know "
              "there is more to do.")

    time.sleep(1)


def navigate_from_main(desired_location, rooms, from_room):
    available_rooms = [room.get_index() for room in rooms if room.is_visible()]
    if desired_location.isnumeric():
        door_index = int(desired_location)
        if door_index in available_rooms:
            room = rooms[door_index]
            return approach_door(room, from_room)


def navigate(desired_location, rooms, from_room):
    if desired_location.isnumeric():
        door_index = int(desired_location)
        if door_index is 1:
            room = rooms[0]
            return approach_door(room, from_room)
        else:
            print("That option does not exist.")


def approach_door(room, from_room):
    if room.is_locked():
        print(" You approach the door but as you turn the handle you realize it is locked.")
        if from_room == 2:
            do_dance(room)
        return None

    else:
        clear_screen()
        print(" You approach the door, turn the handle, and step into the "
              "room.")
        time.sleep(1)
        return room


def do_dance(room):
    print(" Although you want to leave, you feel like you should dance "
          "first!\n You can do the dance you watched before! Try it!\n\n"
          " Moves:\n 1 - Left Arm\n 2 - Left Leg\n 3 - Right Arm\n 4 - Right "
          "Leg\n 5 - Spin\n\n")
    correct_dance = False
    dance_sequence = [1, 3, 4, 2, 5]
    num_check = ['1', '2', '3', '4', '5']
    user_dance = []
    dance_length = len(dance_sequence)
    while not correct_dance:
        dance = input(" Enter the dance sequence one move at a time! ")
        if len(dance) > 1:
            print("\n Adam likes to enter more than one number at a time. "
                  "Don't be Adam.\n")
            continue
        if dance not in num_check:
            print("\n Please enter a number. You know, like in the "
                  "directions.\n")
            continue
        user_dance.append(int(dance))
        if len(user_dance) == dance_length:
            if user_dance == dance_sequence:
                print(" Groovy! That dance is smooth!\n\n")
                print(" You hear a sound. It sounds like a door "
                      "unlocking.\n\n")
                room.unlock_room()
                return
            else:
                print(" Wait. That's not it. Let's try again!")
                user_dance = []


def print_interactive_objs(objects, room_num):
    newline()
    print(" Interactive Objects:")
    for index, obj in enumerate(objects):
        if obj.get_location() == room_num and obj.is_visible():
            print(f" Option: {obj.get_name()}")
