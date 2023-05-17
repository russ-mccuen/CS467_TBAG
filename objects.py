import time


class GameObject:
    def __init__(self, name, short_desc, description, location,  is_movable,
                 is_visible):
        self.name = name
        self.short_desc = short_desc
        self.description = description
        self.location = location
        self.movable = is_movable
        self.visible = is_visible

    def __repr__(self):
        return f"This is the {self.name} room object"

    def set_description(self, description):
        self.description = description

    def get_short_desc(self):
        return self.short_desc

    def get_description(self):
        return self.description

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

    def is_visible(self):
        return self.visible


class TV(GameObject):
    def __init__(self, name, short_desc, description, location, is_movable,
                 is_visible):
        self.on = False
        self.channels = ["\n You see static with UHF-73 in green at the top right of the screen.\n",
                         "\n You see [TODO: Provide Description] the code UHF-74 at the top right of screen."]
        self.vcr = []
        self.current_channel = 0
        super(TV, self).__init__(name, short_desc, description, location,
                                 is_movable, is_visible)

    def __repr__(self):
        return " This is the TV object"

    def is_on(self):
        return self.on

    def turn_on(self):
        print(" \n You turn on the tv and hear a pop as the screen comes to life.")
        self.display_channel()
        self.on = True

    def turn_off(self):
        print(" \n You turn off the tv and almost see your reflection as the screen dims.\n")
        self.on = False

    def turn_channel(self, index):
        try:
            channel = self.channels[index]
            self.current_channel = index
            self.display_channel()
            return True
        except IndexError:
            print(f" \n Channel {index} is not available with your current subscription plan.\n")
            return False

    def display_channel(self):
        print(self.channels[self.current_channel])

    def add_channel(self, channel):
        self.channels.append(channel)


class Commodore(GameObject):
    def __init__(self, name, short_desc, description, location, is_movable,
                 is_visible):
        super().__init__(name, short_desc, description, location,
                         is_movable, is_visible)
        self.on = False
        self.solution = 'place bar'
        self.game_won = False
        self.total_won = 0

    def __repr__(self):
        return " This is the Commodore Object"

    def turn_on(self):
        self.on = True

    def get_solution(self):
        return self.solution

    def get_game_won(self):
        return self.game_won

    def set_game_won(self):
        self.game_won = True

    def set_total_won(self):
        self.total_won += 1

    def get_games_won(self):
        print(f" You won {self.total_won} times.")


# 8 Objects that the player can put in their inventory:
# Object 1
class Letter(GameObject):
    def __init__(self, name, short_desc, description, location, is_movable,
                 is_visible):
        super(Letter, self).__init__(name, short_desc, description,
                                     location, is_movable, is_visible)


class Blacklight(GameObject):
    def __init__(self, name, short_desc, description, location, is_movable,
                 is_visible):
        super(Blacklight, self).__init__(name, short_desc, description,
                                         location, is_movable, is_visible)


# Object 2
class Tablet(GameObject):
    def __init__(self, name, short_desc, description, location, is_movable,
                 is_visible):
        self.folder = ["Info 1: Look around the room. Something has changed."]
        self.passcode = 'UHF-73'
        self.locked = True
        super(Tablet, self).__init__(name, short_desc, description,
                                     location, is_movable, is_visible)

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
            time.sleep(1)

        else:
            print(f" Passcode: {pin} | Access Denied")

    def is_locked(self):
        return self.locked

    def add_to_folder(self, data):
        self.folder.append(data)


# Object 3
class Remote(GameObject):
    def __init__(self, name, short_desc, description, location, is_movable,
                 is_visible):
        super().__init__(name, short_desc, description, location,
                         is_movable, is_visible)

    def use_remote(self):
        pass


# Object 4
class VHS(GameObject):
    def __init__(self, name, short_desc, description, location, is_movable,
                 is_visible):
        super().__init__(name, short_desc, description, location,
                         is_movable, is_visible)

    def use_vhs(self):
        pass
