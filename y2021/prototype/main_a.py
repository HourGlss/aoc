from enum import Enum

class InputHandler:
    elements: list


    def __init__(self, e):
        self.element = e


    def handle_raw_input(self, raw_input):
        ...


class OutputHandler:
    inputHandler: InputHandler
    output: int

    def __init__(self, i: InputHandler):
        self.inputHandler = i
        self.output = 0
        self.build_output()

    def build_output(self):
        ...

    def get_output(self):
        ...


if __name__ == "__main__":
    ...