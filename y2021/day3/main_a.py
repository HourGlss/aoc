from enum import Enum


class PowerConsumption:
    gamma: int
    epsilon: int
    powerfield: list[list[int]]

    life_support_rating:int
    oxygen_generator_rating:int
    co2_scrubbing_rating:int

    def __init__(self, powerfield: list[list[int]]):

        self.powerfield = powerfield
        self.width = len(self.powerfield[0])
        self.height = len(self.powerfield)
        self.build_gamma_and_epsilon()

    def get_gamma(self):
        return self.gamma

    def get_epsilon(self):
        return self.epsilon

    def build_gamma_and_epsilon(self):
        gamma_field = []

        epsilon_field = []
        for x in range(self.width):
            ones = 0
            zeroes = 0
            for y in range(self.height):
                if self.powerfield[y][x] == 1:
                    ones += 1
                else:
                    zeroes += 1
            if ones > zeroes:
                gamma_field.append(1)
                epsilon_field.append(0)
            else:
                gamma_field.append(0)
                epsilon_field.append(1)
        self.gamma = int("".join([str(e) for e in gamma_field]), 2)
        self.epsilon = int("".join([str(e) for e in epsilon_field]), 2)

    def get_power_consumption(self):
        return self.epsilon * self.gamma


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

    def __init__(self, i: InputHandler, powerconsumption):
        self.powerconsumption = powerconsumption
        self.inputHandler = i
        self.output = 0
        self.build_output()

    def build_output(self):
        ...

    def get_output(self):
        ...


if __name__ == "__main__":
    ...
