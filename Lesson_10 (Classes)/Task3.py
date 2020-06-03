# TV controller

Channels = ["Discovery", "A1", "EuroSport", "MTV"]


class TVController:

    def __init__(self, channels):
        self.channels = channels
        self.num_of_channel = 1

    def first_channel(self):
        print(self.channels[0])

    def last_channel(self):
        print(self.channels[-1])

    def turn_channel(self, num_of_channel):
        self.num_of_channel = num_of_channel
        return self.show_channel()

    def next_channel(self):
        self.num_of_channel += 1
        if self.num_of_channel > len(self.channels):
            self.num_of_channel = 1
        return self.show_channel()

    def previous_channel(self):
        self.num_of_channel -= 1
        if self.num_of_channel == 1:
            self.num_of_channel = len(self.channels) - 1
        return self.show_channel()

    def current_channel(self):
        return self.show_channel()

    def is_exist(self, name_of_channel):
        if name_of_channel not in self.channels:
            return "No"
        else:
            return "Yes"

    def show_channel(self):
        return print(self.channels[self.num_of_channel - 1])

    def __repr__(self):
        return self.show_channel()


tv_controller = TVController(Channels)
tv_controller.first_channel()
tv_controller.last_channel()
tv_controller.turn_channel(4)
tv_controller.next_channel()
tv_controller.previous_channel()
tv_controller.current_channel()
print(tv_controller.is_exist("A1"))
print(tv_controller.is_exist("UT-2"))
