# Room Base Class
class Room:
    def __init__(self, name, short_desc, long_desc, is_locked):
        self.name = name
        self.shortDesc = short_desc
        self.longDesc = long_desc
        self.objects = []
        self.is_locked = is_locked

    def __str__(self):
        return f"This is the {self.name} room object"

    def get_name(self):
        return self.name

    def get_short_desc(self):
        return self.shortDesc

    def get_long_desc(self):
        return self.longDesc

    def get_room_objects(self):
        return self.objects

    def get_is_locked(self):
        return self.is_locked

    def set_short_desc(self, description):
        self.shortDesc = description

    def set_long_desc(self, description):
        self.longDesc = description

    def set_object(self, room_object):
        self.objects.append(room_object)

    def remove_room_object(self, room_object):
        self.objects.remove(room_object)

    def unlock_room(self):
        self.is_locked = False
