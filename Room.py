# Room Base Class
class Room:
    def __init__(self, index, name, doorDesc, intro, short_desc, long_desc, is_locked, is_visible, direction):
        self.index = index
        self.name = name
        self.intro = intro
        self.doorDesc = doorDesc
        self.shortDesc = short_desc
        self.longDesc = long_desc
        self.objects = []
        self.features = []
        self.locked = is_locked
        self.visible = is_visible
        self.direction = direction
        self.visited = False

    def __str__(self):
        return f"This is the {self.name} room object"

    def __repr__(self):
        return f"This is the {self.name} room object"

    def get_name(self):
        return self.name

    def get_long_desc(self):
        return self.longDesc

    def get_desc(self):
        if self.visited:
            return self.shortDesc
        else:
            print(self.intro)
            return self.longDesc

    def get_room_objects(self):
        return self.objects

    def is_locked(self):
        return self.locked

    def set_visible(self):
        self.visible = True

    def is_visible(self):
        return self.visible

    def set_intro(self, intro):
        self.intro = intro

    def set_short_desc(self, description):
        self.shortDesc = description

    def set_long_desc(self, description):
        self.longDesc = description

    def set_object(self, room_object):
        self.objects.append(room_object)

    def remove_room_object(self, room_object):
        self.objects.remove(room_object)

    def lock_room(self):
        self.locked = True

    def unlock_room(self):
        self.locked = False

    def get_direction(self):
        return self.direction

    def get_index(self):
        return self.index

    def already_visited(self):
        return self.visited

    def set_visited_true(self):
        self.visited = True

    def get_door_desc(self):
        return self.doorDesc
