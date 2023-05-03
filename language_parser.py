import time

from terminal import newline, clear_screen
# define possible directions to move
DIRECTIONS = {
    "north": ["n", "north"],
    "south": ["s", "south"],
    "east": ["e", "east"],
    "west": ["w", "west"],
    "up": ["u", "up"],
    "down": ["d", "down"]
}

# define possible verbs
VERBS = {
    "go": ["move", "walk", "run", "travel"],
    "take": ["get", "grab", "pick up"],
    "drop": ["put down", "release"],
    "look": ["examine", "inspect"],
    "hit": ["attack", "strike", "punch"],
    "pull": ["drag", "tug"],
    "push": ["shove", "press"],
    "eat": ["consume", "devour"],
    "use": ["activate", "operate"],
    "talk": ["speak", "converse"]
}


def parse_input(user_input, inventory):
    length = len(user_input)

    if len(user_input) == 1:
        if user_input[0] == 'inventory':
            print_inventory(inventory)
            return
        elif user_input[0] == 'help':
            print_help()
            return

        elif user_input[0] == 'clear':
            clear_screen()
            return


    if length != 2:
        print(" Only two word commands are accepted.")
        return

    if user_input[0] == "clear" and user_input[1] == "screen":
        clear_screen()

    else:
        parsed_verb = parse_verb(user_input[0])
        if parsed_verb is None:
            return None

        verb, verb_type = parsed_verb

        if verb:
            if verb_type == "navigate":
                return navigate(verb_type, user_input[1])

            if verb_type == "action":
                return verb, user_input[1]

        return None


def navigate(verb_type, desired_direction):
    if desired_direction.isnumeric():
        return verb_type, desired_direction
    cardinal = parse_direction(desired_direction)
    if cardinal is not None:
        return verb_type, cardinal


def parse_verb(verb):
    for action, synonyms in VERBS.items():
        if verb in action or verb in synonyms:

            if verb == "go" or verb in VERBS["go"]:
                return verb, "navigate"

            if verb == "look" or verb in VERBS["look"]:
                return "look", "action"

            if verb == "take" or verb in VERBS["take"]:
                return "take", "action"

            if verb == "use" or verb in VERBS["use"]:
                return "use", "action"

            if verb == "drop" or verb in VERBS["drop"]:
                return "drop", "action"

            return None


def parse_direction(user_direction):
    for direction, aliases in DIRECTIONS.items():
        if user_direction in aliases:
            return direction
    return None


def describe_walls(rooms, available_nav):
    newline()
    visible_rooms = 0
    newline()

    for index, room in enumerate(rooms):
        if room.is_visible():
            visible_rooms += 1
            available_nav.append(index)
            print(f" Navigation Option ({index}) : {room.get_door_desc()} that is located {room.get_direction()}.")

    if not visible_rooms:
        print(" Except . . . there is no door to the room. Actually, you can not see any way of either entering or "
              "exiting the room.\n There are not even any windows. You know you have a window in your room.\n "
              "At least you think you do.")


def describe_features(objects, room_num):
    newline()
    print(" Interactive Objects: ")
    for index, feature in enumerate(objects):
        if feature.get_location() == room_num:
            print(f" Interaction Option:  {feature.get_name()}")


def try_action(available_nav, rooms, room, action, item, objects, object_names, inventory):
    if action == "look":
        try_look(available_nav, rooms, room, item, objects, object_names, inventory)

    if action == "take":
        try_take(item, objects, object_names, inventory)

    if action == "use":
        try_use(item, objects, object_names, inventory, rooms, room)

    if action == "drop":
        try_drop(item, inventory, room)


def try_take(item, objects, object_names, inventory):
    if item not in object_names:
        print(f" You cannot take {item}")

    for obj in objects:
        obj_in_room = obj.get_name().lower()
        movable = obj.is_movable()
        if item == obj_in_room and movable:
            inventory.append(obj)
            obj.set_object_location(-1)
            print(f" {item} is now in your inventory.")
            break

        if item == obj_in_room and not movable:
            print(f" You cannot move the {item}.")


def try_drop(item, inventory, room):
    for inv_item in inventory:
        if inv_item.get_name().lower() == item:
            inv_item.set_object_location(room.get_index())
            inventory.remove(inv_item)
            print(f" You removed {item} from your inventory and is now in this room.")
            return

    print(f" You dont have {item} to drop.")


def try_look(available_nav, rooms, room, item, objects, object_names, inventory):
    if item == "room":
        print(room.get_long_desc())
        describe_walls(rooms, available_nav)
        describe_features(objects, room.get_index())

    elif item == "desk":
        print(" On the desk you see: ")
        for obj in objects:
            name = obj.get_name()
            if obj.get_location() == room.get_index() and name != "Poster" and name != "Desk":
                print(obj.get_obj_description())

    elif item == "inventory":
        print_inventory(inventory)

    elif item not in object_names:
        for inv_item in inventory:
            if item == inv_item.get_name().lower():
                print(inv_item.get_obj_description())
                return
        print(f" {item} not in your inventory nor this room.")

    else:
        for obj in objects:
            if item == obj.get_name().lower():
                print(obj.get_obj_description())


def try_use(item, objects, object_names, inventory, rooms, room):
    for obj in objects:
        if item == obj.get_name().lower() and (obj.get_location() == room.get_index() or obj.get_location() == -1):
            if item == "tablet":
                use_tablet(obj, rooms, objects, inventory)
                return

            elif item == "tv":
                use_tv(obj)
                return

            elif item == "commodore":
                use_commodore(obj, rooms[0])
                return

            elif item == "remote":
                use_remote(obj)
                return

    print(f" Can't use {item}.")


def use_tablet(tablet, rooms, objects, inventory):
    if not tablet.is_locked():
        clear_screen()
    print(" \n You pick up the tablet.\n")
    if tablet.is_locked():
        print(" You notice that the tablet is locked and is requesting a passcode.\n")
    while True:
        if tablet.is_locked():
            pin = input(" Please Enter Password or 'q' to cancel: ")
            if pin.lower() == 'q':
                break
            tablet.unlock(pin)
            if tablet.is_locked() is False:
                print(" UNLOCK SCREEN DETAILS")
                print(tablet.get_folder())
                rooms[1].set_visible()
                update_poster(tablet, objects)
                update_room_desc(rooms)
                break
        else:
            print(tablet.get_folder())
            break


def update_poster(item, objects):
    for obj in objects:
        if obj.get_name() == 'Poster':
            poster = obj

            if item.get_name() == "Tablet":
                description = poster.get_description() + "A new detail"
                poster.set_description(description)
                break


def update_room_desc(rooms):
    description = rooms[0].get_long_desc() + "\n\n Wait . . . something is different about the poster. And there " \
                                             "appears to be a new door. \n"
    rooms[0].set_long_desc(description)


def use_tv(tv):
    if not tv.is_on():
        tv.turn_on()
    else:
        tv.turn_off()


def use_commodore(pc, mainroom):
    clear_screen()
    print("Commodore 64")
    while True:
        user_input = input("Some Game that unlocks the door (type 0 to win): ")
        if user_input.lower() == 'q':
            return
        if user_input == pc.get_solution():
            mainroom.unlock_room()
            return


def use_remote(remote):
    print(" TODO: Implement Remote Functionality.")


def print_inventory(inventory):
    if not inventory:
        print(" You have nothing. Try to take something.")
    for item in inventory:
        print(item.get_name())


def approach_door(room):
    if room.is_locked():
        print(" You approach the door but as you turn the handle you realize it is locked.")
        return None

    else:
        clear_screen()
        print(" You approach the door turn the handle and step into the room.")
        time.sleep(3)
        return room


def print_help():
    print(" Implement Help Screen")
