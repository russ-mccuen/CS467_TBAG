from verbs import VERBS


def main_room(homebase, rooms, objects, inventory):
    print(homebase.get_desc())
    describe_walls(rooms)
    describe_features(objects)

    while True:
        user_input = input("What would you like to do? ").lower().strip().split()
        if user_input[0] == 'q':
            break
        parse_input(user_input)


def describe_walls(rooms):
    visible_rooms = 0
    print("When you look at the walls around you, you see: ")
    for index, room in enumerate(rooms):
        if room.is_visible():
            visible_rooms += 1
            print(f"{index} : Room: {room.get_name()}  direction location: {room.get_direction()}")
    if not visible_rooms:
        print("Nothing ... on the walls")


def describe_features(objects):
    print("When you look around the room you see: ")
    for index, feature in enumerate(objects):
        if feature.get_location() == 0:
            print(f" {index} Feature: {feature.get_name()}")


def parse_input(user_input):
    length = len(user_input)

    if length != 2:
        print("Only two word commands are accepted.")
        return

    else:
        if user_input[0] == "go" or user_input[0] in VERBS["go"]:
            print("Navigating")



