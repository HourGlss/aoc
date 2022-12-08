from enum import Enum
from y2022.day5.data import test_input, real_input


class File:
    size:int
    name:str
    contents:list["File"]

    def __init__(self,name:str,file_size:int = 0):
        self.name = name
        self.size = file_size




class InputHandler:
    elements: list

    def __init__(self, e=None):
        if e is not None:
            self.element = e

    def handle_raw_input(self, input_to_use):
        input_to_use = input_to_use.split("\n")
        """
        - / (dir)
          - a (dir)
            - e (dir)
              - i (file, size=584)
            - f (file, size=29116)
            - g (file, size=2557)
            - h.lst (file, size=62596)
          - b.txt (file, size=14848514)
          - c.dat (file, size=8504156)
          - d (dir)
            - j (file, size=4060174)
            - d.log (file, size=8033020)
            - d.ext (file, size=5626152)
            - k (file, size=7214296)"""
        for line in input_to_use:
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
    i.handle_raw_input(real_input)
