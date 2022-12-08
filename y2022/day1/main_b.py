from enum import Enum
from y2022.day1.data import test_input,real_input


class InputHandler:
    elements: list

    def __init__(self,e=None):
        if e is not None:
            self.element = e

    def handle_raw_input(self, raw_input):
        ...


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
    i.handle_raw_input()
    it = IncreasingTester(i.elements)
    print(it.iterate_through_list_and_count())
