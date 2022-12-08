from enum import Enum
from y2022.day1.data import test_input, real_input


class Elf:
    calories: list
    i = 0

    def __init__(self, calories: list):
        self.calories = [int(e) for e in calories]
        Elf.i += 1

    def total_calories(self):
        return sum(self.calories)


class InputHandler:
    elements: list
    elves: list[Elf]

    def __init__(self, e=None):
        if e is not None:
            self.element = e

    def handle_raw_input(self, input_to_use):
        data = []
        self.elves = []
        input_to_use = input_to_use.split("\n")
        for line in input_to_use:

            if line != "":
                data.append(line)
            else:
                self.elves.append(Elf(data))
                data = []


class OutputHandler:
    inputHandler: InputHandler

    def __init__(self, i: InputHandler):
        self.inputHandler = i
        self.output = 0
        self.build_output()

    def build_output(self):
        ...

    def get_output(self):
        ...


if __name__ == "__main__":
    i = InputHandler()
    i.handle_raw_input(real_input)
    all = [e.total_calories() for e in i.elves]
    ids = [e.i for e in i.elves]
    max_cals = []
    best_elves = []
    totals = []
    for i in range(3):
        best = max(all)
        to_pop = all.index(best)
        all.pop(to_pop)
        totals.append(best)
    print(sum(totals))
