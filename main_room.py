
def main_room(homebase, rooms):
    description = homebase.get_desc()
    print(description)
    print(f"Feature One: {homebase.get_feature_one()}")
    print(f"Feature Two: {homebase.get_feature_two()}")
    print("When you look at the walls around you, you see: ")
    for index, room in enumerate(rooms):
        if room.is_visible():
            print(f"{index} : Room: {room.get_name()}  direction location: {room.get_direction()}")

