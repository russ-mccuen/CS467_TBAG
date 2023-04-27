class GameObject:
    def __init__(self, description, location, unlocks_room):
        self.description = description
        self.location = location
        self.unlocks_room = unlocks_room

    def get_object_description(self):
        return self.description

    def get_object_location(self):
        return self.location

    def set_object_location(self, location):
        self.location = location

