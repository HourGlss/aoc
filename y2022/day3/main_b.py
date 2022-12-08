from enum import Enum
from y2022.day3.data import test_input, real_input


def score(blah):
    total = 0
    for e in blah:

        if ord(e) > 96:
            this = ord(e) - 96
        else:
            this = ord(e) - 64 + 26
        total += this
    return total


class InputHandler:
    elements: list

    def __init__(self, e=None):
        if e is not None:
            self.element = e

    def handle_raw_input(self, input_to_use):
        input_to_use = input_to_use.split("\n")
        first = []
        second = []
        i = 0
        total = 0
        for line in input_to_use:

            if i < 3:
                first.append(set(line))
            else:
                second.append(set(line))
            i += 1
            if i % 6 == 0:
                i = 0
                a = first[0]
                for x in range(1,3):
                    a = a.intersection(first[x])
                b = second[0]
                for x in range(1,3):
                    b = b.intersection(second[x])
                save = [list(a)[0],list(b)[0]]
                total += score(save)
                first = []
                second = []
        print(total)



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
