from terminal import *


def describe_exit():
    """
    General description of leaving the room to navigate back towards the main room.
    :return:
    """
    newline()
    print(" You are also aware of the door that will lead you back to the "
          "main room: ")
    print(f" Navigation Option (1) :  The door heading back to the main room "
          "that is located in the center.")
    newline()


def room_setup_objs(room, objects):
    """
    Initializes available navigation options, available objects based on room index and an array of those object names.
    :param room: Index number of current room.
    :param objects: An array of game objects.
    :return: a list of available navigation, a list of available objects, a list of object names.
    """
    room_index = room.get_index()
    available_nav = []
    available_objs = [item for item in objects if item.get_location() == room_index]
    object_names = [item.get_name().lower() for item in available_objs]
    return available_nav, available_objs, object_names


def print_room_details(rooms, available_nav, available_objs, room):
    """
    Prints the room details based on the current room index.
    :param rooms: An array of room objects.
    :param available_nav: An array of rooms that are available to navigate to.
    :param available_objs: An array of objects with an index position that matches the room index.
    :param room: The current room's index.
    :return: None
    """
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
              "exiting the room. There are not even any windows. You know "
              "you have a window in your room.\n\n "
              " At least you think you do.\n\n")


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

    if room_index == 3:
        print(" As you leave Woodstock, a part of you remains forever changed."
              "The memories of the music, the people, and the indomitable "
              "spirit of that magical weekend will forever be etched in your "
              "heart. Woodstock will forever stand as a symbol of hope, "
              "a testament to the power of music and the unyielding pursuit "
              "of a better world.")

    if room_index == 4:
        print(" As you stroll through the bustling food court of the 1990s, "
              "the nostalgic aromas of greasy burgers, fresh popcorn, "
              "and sugary treats fill the air. The vibrant neon lights and "
              "vibrant decor transport you back to an era of vibrant colors "
              "and retro charm. Laughter and chatter resonate from the "
              "crowded tables as people enjoy their meals and share stories. "
              "You take a moment to soak in the atmosphere, appreciating the "
              "simplicity and innocence of this bygone time. Before you leave "
              "you can't help but feel a twinge of bittersweet nostalgia. "
              "You carry the memories of this vibrant food court, frozen in "
              "time, as you prepare to journey back to the present, eager to "
              "rejoin the world of modern marvels and future possibilities.")

    if room_index == 5:
        print(" As you stand on the threshold of the living room, your gaze "
              "lingers on the familiar surroundings, filled with memories of "
              "the 2000s. The soft glow of the table lamps casts a warm "
              "ambiance, illuminating the space where laughter and "
              "conversations once flowed freely. You take one last glance at "
              "the entertainment unit, its sleek lines housing the beloved "
              "gaming consoles and that prized flat-screen television. The "
              "familiar hum of the ceiling fan above stirs the air gently, "
              "as if bidding you farewell. The bookshelf stands proud, "
              "displaying the cherished collection of books, CDs, and DVDs, "
              "a testament to a time when physical media reigned supreme. "
              "With a mix of nostalgia and anticipation, you reluctantly "
              "turn away, leaving the room behind, the remnants of the 2000s "
              "clinging to your thoughts as you prepare to reemerge into the "
              "present")

    if room_index == 6:
        print(" As you stand on the edge of Washington, D.C. in the "
              "remarkable year of 2076, a surge of anticipation tingles "
              "through your veins. The air crackles with an electric energy "
              "as you prepare to bid farewell to this extraordinary future. "
              "With one last look at the awe-inspiring cityscape, adorned "
              "with futuristic architecture and bustling with advanced "
              "technologies, you take a deep breath, savoring the moment. "
              "The sun casts a warm glow over the horizon, illuminating the "
              "sleek buildings and reflecting off the surfaces of "
              "self-driving vehicles gliding by. You pause, absorbing the "
              "vibrant atmosphere and the palpable sense of progress. The "
              "future has unfolded before your eyes, leaving an indelible "
              "mark on your memories. With gratitude and excitement, "
              "you embrace the unknown, ready to carry the lessons and "
              "inspiration of Washington, D.C. in 2076 back to the present.")

    if room_index == 7:
        print(" As you rise from the booth, a sense of bittersweet nostalgia "
              "fills your heart, for you know that your time in this "
              "enchanting 1950s diner is coming to an end; you take a final "
              "glance around, savoring the vibrant colors, the retro "
              "ambiance, and the lively conversations that surround you, "
              "committing every detail to memory, realizing that soon you "
              "will return to the present, bidding farewell to the jukebox "
              "melodies, the aroma of freshly brewed coffee, and the warmth "
              "of a bygone era, cherishing this unique experience as you "
              "step towards the door, the bell above jingling one last time, "
              "and with a mixture of gratitude and longing, you take one "
              "final breath of the past before venturing back into the "
              "unknown future.")

    if room_index == 8:
        print("As you prepare to leave the base on Mars, a sense of "
              "bittersweet nostalgia washes over you. The familiar hum of "
              "machinery and the bustling activity of scientists and "
              "engineers surround you, creating a symphony of human "
              "endeavor. You steal a final glance at the awe-inspiring "
              "Martian landscape, its rugged beauty etched in your memory. "
              "The reddish hues of the dunes, the towering mountains, "
              "and the ethereal sky overhead evoke a profound appreciation "
              "for the indomitable spirit of exploration. With a mixture of "
              "excitement and reluctance, you take a deep breath, knowing "
              "that the time has come to bid farewell to this extraordinary "
              "world and return to your own time, carrying with you the "
              "untold stories and infinite possibilities of Mars.\n\n")

    time.sleep(1)


def navigate_from_main(desired_location, rooms, from_room):
    if desired_location == 'center' and from_room != 0:
        room = rooms[0]
        return approach_door(room, from_room)
    available_rooms = [room.get_index() for room in rooms if room.is_visible()]
    room_dir = [room.get_direction() for room in rooms if room.is_visible()]
    if desired_location.isnumeric():
        door_index = int(desired_location)
        if door_index in available_rooms:
            room = rooms[door_index]
            return approach_door(room, from_room)
    else:
        if desired_location in room_dir:
            room_dir_index = room_dir.index(desired_location)
            room_index = available_rooms[room_dir_index]
            room = rooms[room_index]
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
    if room.is_locked() and from_room != 3 and from_room != 5:

        print("\n You approach the door but as you turn the handle you "
              "realize it is locked.\n\n")
        if from_room == 2:
            dance = False
            while not dance:
                dance2 = input("\n You feel like before you leave the 1970s "
                               "you really should do a disco dance! How "
                               "about it? Will you dance? ")
                if dance2 == 'dance':
                    do_dance(room)
                    dance = True
                else:
                    print("\n You really should dance.\n\n")

        if from_room == 4:
            eat = False
            while not eat:
                eat2 = input("\n You feel like before you leave the 1990s you "
                             "really should get a slice of pizza. What do "
                             "you want to do? ")
                if eat2 == 'eat pizza':
                    eat_pizza(room)
                    eat = True
                else:
                    print("\n You really should eat a slice of pizza.\n\n")

        if from_room == 6:
            swim = False
            while not swim:
                swim2 = input("\n You remember how hot it is in July. You "
                              "wish there was someway to cool off before you "
                              "left. You'd bet that the reflecting pool is "
                              "refreshing! But surely you can't swim in the "
                              "reflecting pool . . . can you? What do you "
                              "want to do? ")
                if swim2 == 'swim' or swim2 == 'swim in reflecting pool':
                    go_swim(room)
                    swim = True
                else:
                    print("\n You really should go for a swim. I'll bet "
                          "if you type 'swim' or 'swim in reflecting pool' "
                          "then you could probably swim!\n\n")

        if from_room == 7:
            booth = False
            while not booth:
                booth2 = input("\n The smell of the food stops you from "
                               "leaving. It smells so good and you realize "
                               "you are so hungry that you have to try "
                               "something.\n\n Maybe you should sit in a "
                               "booth.\n\n What do you want to do? ")
                if booth2 == 'sit in booth' or booth2 == 'sit booth':
                    sit_booth(room)
                    booth = True
                else:
                    print("\n You really should try a burger. Maybe you "
                          "should 'sit in booth' or perhaps 'sit booth'.")

        if from_room == 8:
            print("\n It's a good thing because you remember that "
                  "gravity on Mars in only 38% that of Earth! (You really "
                  "paid attention in school so you remember stuff like "
                  "this.) Conveniently there is a spacesuit nearby.\n\n")
            suit = False
            while not suit:
                suit2 = input("What do you want to do? ")
                if suit2 == 'wear spacesuit':
                    put_on_spacesuit(room)
                    suit = True
                else:
                    print("\n You really should jump on Mars. Maybe you "
                          "should 'wear spacesuit'. Just a thought.\n\n")

        return None

    else:
        clear_screen()
        print(" You approach the door, turn the handle, and step into the "
              "room.")
        time.sleep(1)
        return room


def do_dance(room):
    print("\n Great choice! You can do the dance you watched before! Try "
          "it!\n\n"
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
            print("\n Please enter one number at a time.\n\n")
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


def eat_pizza(room):
    print("\n Great choice! As you approach the pizza place your mouth "
          "starts to water. After waiting in line for a minute, you finally "
          "get to order a slice. You reach for your wallet and realize you "
          "don't have it!\n\n The person working the register says, 'If you "
          "know the map location of our store on the mall directory you can "
          "have a free slice! What is the location?'\n\n")
    code = 'FC-15'
    correct_code = False
    while not correct_code:
        free_slice = input(" What is the code? ")
        if free_slice == code:
            print("\n The person working behind the counter says, 'That's "
                  "it! Here's a slice of pizza on us. Enjoy!'\n\n"
                  "Yes, it is a slice of pizza. but somehow it just tastes "
                  "different. It is better. It may be the best slice of "
                  "pizza you've ever had! Or you could just be really "
                  "hungry. Regardless, it was quite a slice!\n\n"
                  " The door unlocks.\n\n")
            room.unlock_room()
            correct_code = True
            return
        else:
            print("\n That's not the right code. Have a look around. It has to"
                  " be here somewhere.\n\n")
            return


def sit_booth(room):
    print("\n You sit down in a booth, the waitress comes over and asks, "
          "'What'll you have, sugar?'\n\n You realize you forgot your "
          "wallet. Again. Although your money would be no good here. Sensing "
          "your hesitation, the waitress smiles and says, 'How about a burger?"
          " On me.\n\n The shocked look on your face tells her everything she "
          "needs to know.\n\n 'Be right back with that burger, hon.'\n\n A "
          "few minutes later the waitress arrives with a burger that looks "
          "amazing, and a soda for you to drink. You are about the thank her "
          "when she smiles, winks, and walks away.\n\n As you sit in the "
          "booth, you notice a small, weathered baseball card peeking out "
          "from beneath the edge of the seat cushion.\n\n")
    eat_burger(room)


def eat_burger(room):
    eaten = False
    while not eaten:
        num_nums = input("\n You start to drool as you are enveloped by the "
                         "aroma of the burger.\n\n What do you want to do? ")
        if num_nums == 'eat burger':
            print("\n This is the best burger you've ever had. And you are "
                  "not saying that just because you are hungry. The burger "
                  "tastes so fresh. It is like you've never eaten a burger "
                  "before you had this one.\n\n")
            room.unlock_room()
            eaten = True
            return
        else:
            print("\n Maybe you should, you know, eat the burger. Or, in game "
                  "talk, 'eat burger'.\n\n")


def go_swim(room):
    print("\n It is so hot you can't help but go for a swim, and the only "
          "place around to swim is the reflecting pool! You jump in quickly "
          "and then realize the pool is only 18 inches deep at the edges, "
          "30 inches deep in the middle. So you lie down to cool off.\n\n "
          " While lying in the pool you notice a coin. For some reason you "
          "think you should take it.\n\n")
    room.unlock_room()
    return


def put_on_spacesuit(room):
    print("\n Surprisingly enough, the spacesuit fits perfectly! It's just "
          "like in the movies!\n\n You go through the airlock and find "
          "yourself on the surface of Mars. On Earth you can't jump very "
          "high. Maybe a few feet if that. But on Mars you think you could "
          "probably jump high enough to dunk a basketball. Maybe.\n\n There "
          "is only one way to find out.\n\n")
    jump = False
    while not jump:
        jump2 = input(" What do you want to do? ")
        if jump2 == "jump":
            print("\n You crouch down, tense up, and explode off of the "
                  "surface of Mars! You have never jumped so high in your "
                  "life! You could dunk a basketball on Mars for sure!\n\n "
                  "For what seems like an eternity you slowly rise up, "
                  "then just as slowly come back down before landing gently "
                  "on the Martian surface.\n\n While airborne, "
                  "you happened to catch a glimpse of what appeared to be "
                  "one of NASA's rovers! What was it called?\n\n "
                  "Curiousity!\n\n For some reason you think this is "
                  "important.\n\n You head back "
                  "inside, and hang your borrowed spacesuit back up before "
                  "anyone notices it was gone.\n\n")
            room.unlock_room()
            return
        else:
            print("\n Might as well jump!\n\n")


def print_interactive_objs(objects, room_num):
    newline()
    print(" Interactive Objects:")
    for index, obj in enumerate(objects):
        if obj.get_location() == room_num and obj.is_visible():
            print(f" Option: {obj.get_name()}")
