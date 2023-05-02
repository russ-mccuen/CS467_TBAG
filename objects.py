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


class TV(GameObject):
    def __init__(self, name, description, location, is_movable):
        self.on = False
        self.channels = ["\n You see static with UHF-73 in green at the top right of the screen.\n"]
        self.vcr = []
        self.current_channel = 0
        super(TV, self).__init__(name, description, location, is_movable)

    def __repr__(self):
        return "This is the TV object"

    def is_on(self):
        return self.on

    def turn_on(self):
        print(" \n You turn on the tv and hear a pop as the screen comes to life.")
        print(self.channels[self.current_channel])
        self.on = True

    def turn_off(self):
        print(" \n You turn off the tv and almost see your reflection as the screen dims.\n")
        self.on = False

    def turn_channel(self, index):
        try:
            self.current_channel = self.channels[index]
        except IndexError:
            print(" \n That channel is not available with your current subscription plan.\n")

    def add_channel(self, channel):
        self.channels.append(channel)


class Commodore(GameObject):
    def __init__(self, name, description, location, is_movable):
        super().__init__(name, description, location, is_movable)
        self.is_on = False

    def turn_pc_on(self):
        self.is_on = True


# 8 Objects that the player can put in their inventory:
# Object 1
class Letter(GameObject):
    def __init__(self, name, description, location, is_movable):
        super(Letter, self).__init__(name, description, location, is_movable)


# Object 2
class Tablet(GameObject):
    def __init__(self, name, description, location, is_movable):
        self.folder = {"Room One:", "Look around the room. Something has changed."}
        self.passcode = 'UHF-73'
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
            print(" Access Granted")

        else:
            print(f" Passcode: {pin} | Access Denied")

    def is_locked(self):
        return self.locked

    def drop_tablet(self):
        pass


# Object 3
class Remote(GameObject):
    def __init__(self, name, description, location, is_movable):
        super().__init__(name, description, location, is_movable)

    def use_remote(self):
        pass


# Object 4
class VHS(GameObject):
    def __init__(self, name, description, location, is_movable):
        super().__init__(name, description, location, is_movable)

    def use_vhs(self):
        pass
