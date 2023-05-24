import time

from terminal import newline, clear_screen
from room_setup import *
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
    "take": ["get", "grab", "pick-up"],
    "drop": ["put-down", "release"],
    "look": ["examine", "inspect"],
    "hit": ["attack", "strike", "punch"],
    "pull": ["drag", "tug"],
    "push": ["shove", "press"],
    "eat": ["consume", "devour"],
    "use": ["activate", "operate"],
    "talk": ["speak", "converse"],
    "dance": ["boogie", "get-down"]
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


def try_action(available_nav, rooms, room, action, item, objects, object_names, inventory):
    if action == "look":
        try_look(available_nav, rooms, room, item, objects, object_names, inventory)

    if action == "take":
        try_take(item, objects, object_names, inventory, room)

    if action == "use":
        try_use(item, objects, rooms, room)

    if action == "drop":
        try_drop(item, inventory, room)


def try_take(item, objects, object_names, inventory, room):
    if item not in object_names:
        print(f" You cannot take {item}")

    for obj in objects:
        if obj.get_location() == room.get_index():
            obj_in_room = obj.get_name().lower()
            movable = obj.is_movable()
            if item == obj_in_room and movable and obj not in inventory:
                inventory.append(obj)
                obj.set_object_location(-1)
                print(f" {item} is now in your inventory.")
                break

            if item == obj_in_room and not movable:
                print(f" You cannot move the {item}.")
                break


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
        available_nav, available_objs, object_names = room_setup_objs(room, objects)
        print_room_details(rooms, available_nav, available_objs, room)
        print_interactive_objs(objects, room.get_index())

    elif item == "desk":
        desk_items = []
        print(" \n On the desk you see: \n")
        for obj in objects:
            name = obj.get_name()
            if obj.get_location() == room.get_index() and name != "Poster" and name != "Desk":
                print(obj.get_short_desc())
                desk_items.append(obj.get_name())

        if desk_items:
            newline()
            print(" Interactive Desk Items: ")
            for item in desk_items:
                print(f" Option: {item}")

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


def try_use(item, objects, rooms, room):
    for obj in objects:
        if item == obj.get_name().lower() and (obj.get_location() == room.get_index() or obj.get_location() == -1):
            if item == "tablet":
                use_tablet(obj, rooms, objects)
                return

            elif item == "tv":
                use_tv(obj)
                return

            elif item == "commodore":
                use_commodore(obj, rooms[0])
                return

            elif item == "remote":
                use_remote(objects, room)
                return

            elif item == 'blacklight':
                use_blacklight()
                return

    print(f" Can't use {item}.")


def get_poster(objects):
    for obj in objects:
        if obj.get_name() == 'Poster':
            return obj


def use_tablet(tablet, rooms, objects):
    clear_screen()
    print(" \n You pick up the tablet.\n")
    if tablet.is_locked():
        print(" You notice that the tablet is locked and is requesting a passcode.\n")
    time.sleep(1)
    clear_screen()
    print(" \n USING TABLET \n")
    available_info = tablet.get_folder()
    poster = get_poster(objects)

    while True:
        if tablet.is_locked():
            pin = input(" Please Enter Password or 'q' to cancel: ")
            if pin.lower() == 'q':
                print(" \n  You put the tablet away.")
                time.sleep(1)
                break
            tablet.unlock(pin)
            if tablet.is_locked() is False:
                poster_detail = " A poster with a thin black frame."
                poster.set_description(poster_detail)

                clear_screen()
                print(" You hear something shift in the room. You unlocked the tablet. On it you "
                      "see information.")
                time.sleep(1)
                rooms[1].set_visible()
            else:
                continue

        clear_screen()
        print(" USING TABLET\n")
        print_tab_info(tablet)

        user_input = input(" \n Enter a new pin to access more or q to quit. ")
        if user_input == 'q':
            print("You put the tablet away.")
            time.sleep(1)
            break

        if user_input == "UHF-74":
            description = "Info 2: Room 2 unlocked"
            if description not in available_info:
                cur_desc = poster.get_description()
                poster_detail = cur_desc + " A shiny Delorean."
                poster.set_description(poster_detail)

                tablet.add_to_folder(description)
                rooms[2].set_visible()
                clear_screen()
                print(" \n You unlocked more information.")
                time.sleep(1)
                continue

        if user_input == "WKRP":
            description = "Info 3: Room 3 unlocked"
            if description not in available_info:
                cur_desc = poster.get_description()
                poster_detail = cur_desc + " A disco ball."
                poster.set_description(poster_detail)

                tablet.add_to_folder(description)
                rooms[3].set_visible()
                rooms[3].unlock_room()
                clear_screen()
                print(" \n You unlocked more information.")
                time.sleep(1)
                continue


def use_blacklight():
    print(" You turn the blacklight on and shine it around the room. "
          "Different \n things suddenly appear on the walls. You see a "
          "peace\n sign, a few names written with hearts between them, "
          "but what\n catches your eye is a drawing of a television with the "
          "letters\n WKRP written underneath it. For some reason you think "
          "you\n should remember this.\n")
    return


def print_tab_info(tablet):
    for info in tablet.get_folder():
        print("", info)


def update_room_desc(rooms):
    description = rooms[0].get_long_desc() + "\n\n Wait . . . something is different about the " \
                                             "poster. And there appears to be a new door. \n"
    rooms[0].set_long_desc(description)


def use_tv(tv):
    if not tv.is_on():
        tv.turn_on()

    else:
        tv.turn_off()


def use_commodore(pc, mainroom):
    clear_screen()
    print(" As you power on this magnificent machine, your eyes are greeted "
          "by a \n stunning 8-bit display, capable of producing vivid colors "
          "and sharp graphics. Its resolution, while modest by today's "
          "\n standards, is a sight to behold in its time. You notice\n"
          " your favorite game, Zork, on the screen! You are at the end "
          "\n of the game! You never managed to beat it. This is what you"
          "\n see on the screen:\n\n")
    while True:
        user_input = input("\n Living room. Your collection of treasures "
                           "consists of:"
                           "\n  A crystal skull"
                           "\n  A sapphire-encrusted bracelt"
                           "\n  A jewel-encrusted egg"
                           "\n  A golden clockwork canary"
                           "\n  A chalice"
                           "\n  A beautiful brass bauble"
                           "\n  A leather bag of coins"
                           "\n  A trunk of jewels"
                           "\n  A crystal trident"
                           "\n  A beautiful jeweled scarab"
                           "\n  A large emerald"
                           "\n  A huge diamond"
                           "\n  A jade figurine"
                           "\n  A sceptre"
                           "\n  A pot of gold"
                           "\n  A gold coffin"
                           "\n  A painting"
                           "\n\n > ")
        if user_input.lower() == 'q':
            return
        if user_input == pc.get_solution():
            mainroom.unlock_room()
            if not pc.get_game_won():
                print(" \n You place the bar in the case, head to the "
                      "mailbox, then head southwest to the barrow and . . "
                      ". \n\n You won! After all these years!!!")
                print(" \n You hear a loud click behind you.\n")
                pc.set_game_won()
                pc.set_total_won()
                return
            else:
                print(" You already beat this game.")
                pc.set_total_won()
                pc.get_games_won()
        else:
            print("\n That wasn't the right command. Maybe you should try "
                  "again.\n")


def use_remote(objects, room):
    room_index = room.get_index()
    if room_index != 0:
        print(" You mash the buttons on the remote but it does not seem to do anything.")
        return
    channel = 0
    for tv in objects:
        if tv.get_name().lower() == "tv":
            if not tv.is_on():
                print(" You notice the tv is off. You press the power button on the remote.")
                tv.turn_on()
            else:
                print(" You notice the tv is already on.")
                tv.display_channel()

            while True:
                user_channel = input(" \n USING REMOTE: Type + or - to change channel or q to quit: ").lower()
                if user_channel == "q":
                    break

                if user_channel == "+":
                    channel += 1
                    change_channel(channel, tv)

                if user_channel == "-":
                    channel -= 1
                    change_channel(channel, tv)


def change_channel(channel, tv):
    print(" You hear a click as you change the channel.", channel)
    tv.turn_channel(channel)


def print_inventory(inventory):
    if not inventory:
        print(" You have nothing. Try to take something.")
    for item in inventory:
        print(item.get_name())


def print_help():
    print(" Implement Help Screen")
