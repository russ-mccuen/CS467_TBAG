class GameObject:
    def __init__(self, name, description, location,  is_movable):
        self.name = name
        self.description = description
        self.location = location
        self.movable = is_movable

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
        return self.movable


class Tablet(GameObject):
    def __init__(self, name, description, location, is_movable):
        self.folder = {"Room One:", "Look around the room. Something has changed."}
        self.passcode = '0'
        self.locked = True
        super(Tablet, self).__init__(name, description, location, is_movable)

    def get_folder(self):
        return self.folder

    def get_passcode(self):
        return self.passcode

    def set_passcode(self, passcode):
        self.passcode = passcode

    def unlock(self, pin):
        if pin == self.passcode:
            self.locked = False
            print("Access Granted")

        else:
            print(f"Passcode: {pin} | Access Denied")

    def is_locked(self):
        return self.locked


class TV(GameObject):
    def __init__(self, name, description, location, is_movable):
        self.is_on = False
        self.channels = ["UHF-73"]
        self.vcr = []
        self.current_channel = self.channels[0]
        super(TV, self).__init__(name, description, location, is_movable)

    def __repr__(self):
        return "This is the TV object"

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def turn_channel(self, index):
        try:
            self.current_channel = self.channels[index]
        except IndexError:
            print("That channel is not available with your current subscription plan.")

    def add_channel(self, channel):
        self.channels.append(channel)
