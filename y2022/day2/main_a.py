from enum import Enum
from y2022.day3.data import test_input, real_input


def score(blah):
    total = 0
    for e in blah:

        if ord(e) > 96:
            this = ord(e) - 96
        else:
            this = ord(e) - 64 + 26
        print(e,this)
        total += this
    return total


class InputHandler:
    elements: list

    def __init__(self, e=None):
        if e is not None:
            self.element = e

    def handle_raw_input(self, input_to_use):
        input_to_use = input_to_use.split("\n")
        save = []
        for line in input_to_use:
            length = int(len(line) / 2)
            a = line[:length]
            b = line[length:]
            # print(a)
            # print(b)
            a = set([e for e in a])
            b = set([e for e in b])
            c = list(a.intersection(b))
            # print(c)
            save.append(c[0])
        print(score(save))


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
