class GameObject:
    def __init__(self, name, description, location,  is_movable):
        self.name = name
        self.description = description
        self.location = location
        self.is_movable = is_movable
        self.items = []

    def __repr__(self):
        return f"This is the {self.name} room object"

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def get_obj_description(self):
        return self.description

    def get_object_location(self):
        return self.location

    def set_object_location(self, location):
        self.location = location

    def is_movable(self):
        return self.is_movable()

    def set_item(self, item):
        self.items.append(item)

    def get_items(self):
        return self.items

