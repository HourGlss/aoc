class PowerConsumption:
    power_field: list[list[int]]

    oxygen_generator_rating: int
    co2_scrubbing_rating: int

    def __init__(self, power_field: list[list[int]]):
        self.power_field = power_field
        self.width = len(self.power_field[0])
        self.height = len(self.power_field)

    def rating_per_index(self, _index, current_rating):
        ones = 0
        zeroes = 0
        for y in range(len(self.power_field)):
            if self.power_field[y][_index] == 1:
                ones += 1
            else:
                zeroes += 1
        if current_rating == "co2":
            if zeroes <= ones:
                return 0
            else:
                return 1
        elif current_rating == "oxy":
            if ones >= zeroes:
                return 1
            else:
                return 0

    def build_rating(self, current_rating):
        original = self.build_copy()
        self.minimize_power_field(current_rating)
        if current_rating == "co2":
            self.co2_scrubbing_rating = int("".join([str(e) for e in self.power_field[0]]), 2)
        elif current_rating == "oxy":
            self.oxygen_generator_rating = int("".join([str(e) for e in self.power_field[0]]), 2)
        self.power_field = original

    def minimize_power_field(self, current_rating):
        current_index = 0
        while len(self.power_field) > 1:
            find_value = self.rating_per_index(current_index, current_rating)
            allowed = []
            for value in self.power_field:
                if value[current_index] == find_value:
                    allowed.append(value)
            self.power_field = allowed
            current_index += 1

    def build_copy(self):
        original = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(self.power_field[y][x])
            original.append(row)
        return original

    def get_oxygen_generator_rating(self):
        self.build_rating("oxy")
        return self.oxygen_generator_rating

    def get_co2_scrubber_rating(self):
        self.build_rating("co2")
        return self.co2_scrubbing_rating

    def get_life_support_rating(self):
        return self.get_co2_scrubber_rating() * self.get_oxygen_generator_rating()


class InputHandler:
    elements: list[list[int]]

    def __init__(self):
        self.elements = []

    def handle_raw_input(self, raw_input):
        for line in raw_input.split('\n'):
            row = []
            for c in line.strip():
                row.append(int(c))
            self.elements.append(row)


class OutputHandler:
    inputHandler: InputHandler
    output: int

    def __init__(self, inp: InputHandler):
        self.inputHandler = inp
        self.output = 0
        self.build_output()

    def build_output(self):
        ...

    def get_output(self):
        ...
