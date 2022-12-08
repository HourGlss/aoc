from enum import Enum
from y2022.day4.data import test_input, real_input




class InputHandler:
    elements: list

    def __init__(self, e=None):
        if e is not None:
            self.element = e

    def handle_raw_input(self, input_to_use):
        input_to_use = input_to_use.split("\n")
        count = 0
        for line in input_to_use:
            data = line.strip('\n').split(",")
            first = data[0]
            second = data[1]
            fdata = first.split("-")
            sdata = second.split("-")
            fdata = [int(e) for e in fdata]
            sdata = [int(e) for e in sdata]
            frange = [e for e in range(fdata[0], fdata[1]+1)]
            srange = [e for e in range(sdata[0],sdata[1]+1)]
            lf = len(frange)
            ls = len(srange)
            if lf > ls:
                longer = frange
                shorter = srange
            else:
                longer = srange
                shorter = frange
            if shorter[0] in longer and shorter[-1] in longer:
                count += 1
        print(count)




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
