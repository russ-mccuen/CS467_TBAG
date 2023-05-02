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
        if user_input[0] == 'help':
            print_help()
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

            return None


def parse_direction(user_direction):
    for direction, aliases in DIRECTIONS.items():
        if user_direction in aliases:
            return direction
    return None


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
        print(" ... no exits and no doors ... you seem to be trapped.")


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
        try_use(item, objects, object_names, inventory, rooms)


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


def try_look(available_nav, rooms, room, item, objects, object_names, inventory):
    if item == "room":
        print(room.get_long_desc())
        describe_walls(rooms, available_nav)
        describe_features(objects, room.get_index())

    elif item == "desk":
        for obj in objects:
            if obj.get_location() == room.get_index():
                print(obj.get_obj_description())

    elif item == "inventory":
        print_inventory(inventory)

    elif item not in object_names and item not in inventory:
        print(" That object is not in this room or your inventory")

    else:
        for obj in objects:
            if item == obj.get_name().lower():
                print(obj.get_obj_description())


def try_use(item, objects, object_names, inventory, rooms):
    for obj in objects:
        if item == obj.get_name().lower():
            if item == "tablet":
                use_tablet(obj, rooms)
                break

            if item == "tv":
                use_tv(obj)
                break

            print(f"Can't use {item}")


def use_tablet(tablet, rooms):
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
                break
        else:
            print(tablet.get_folder())
            break


def use_tv(tv):
    if not tv.is_on():
        tv.turn_on()
    else:
        tv.turn_off()


def print_inventory(inventory):
    if not inventory:
        print(" You have nothing. Try to take something.")
    for item in inventory:
        print(item.get_name())


def print_help():
    print(" Implement Help Screen")
