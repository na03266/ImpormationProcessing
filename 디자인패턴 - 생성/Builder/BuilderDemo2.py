class Computer:
    def __init__(self, hdd, ram, is_graphics_card_enabled=False, is_bluetooth_enabled=False):
        self.hdd = hdd
        self.ram = ram
        self.is_graphics_card_enabled = is_graphics_card_enabled
        self.is_bluetooth_enabled = is_bluetooth_enabled

    def get_hdd(self):
        return self.hdd

    def get_ram(self):
        return self.ram

    def is_graphics_card_enabled(self):
        return self.is_graphics_card_enabled

    def is_bluetooth_enabled(self):
        return self.is_bluetooth_enabled

    class ComputerBuilder:
        def __init__(self, hdd, ram):
            self.hdd = hdd
            self.ram = ram
            self.is_graphics_card_enabled = False
            self.is_bluetooth_enabled = False

        def set_graphics_card_enabled(self, is_graphics_card_enabled):
            self.is_graphics_card_enabled = is_graphics_card_enabled
            return self

        def set_bluetooth_enabled(self, is_bluetooth_enabled):
            self.is_bluetooth_enabled = is_bluetooth_enabled
            return self

        def build(self):
            return Computer(self.hdd, self.ram, self.is_graphics_card_enabled, self.is_bluetooth_enabled)

if __name__ == "__main__":
    comp = Computer.ComputerBuilder("500 GB", "2 GB") \
        .set_bluetooth_enabled(True) \
        .set_graphics_card_enabled(True) \
        .build()