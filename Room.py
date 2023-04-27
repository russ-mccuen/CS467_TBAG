# Room Base Class
class Room:
    def __init__(self, index, name, short_desc, long_desc, is_locked, feature_1, feature_2, is_visible, direction):
        self.index = index
        self.name = name
        self.shortDesc = short_desc
        self.longDesc = long_desc
        self.objects = []
        self.features = []
        self.locked = is_locked
        self.feature_1 = feature_1
        self.feature_2 = feature_2
        self.visible = is_visible
        self.direction = direction
        self.visited = False

    def __str__(self):
        return f"This is the {self.name} room object"

    def __repr__(self):
        return f"This is the {self.name} room object"

    def get_name(self):
        return self.name

    def get_short_desc(self):
        return self.shortDesc

    def get_long_desc(self):
        return self.longDesc

    def get_room_objects(self):
        return self.objects

    def get_feature_one(self):
        return self.feature_1

    def get_feature_two(self):
        return self.feature_2

    def is_locked(self):
        return self.locked

    def set_visible(self):
        self.visible = True

    def is_visible(self):
        return self.visible

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
