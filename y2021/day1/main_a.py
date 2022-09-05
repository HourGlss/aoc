from enum import Enum


class IncreasingTester:

    def __init__(self, elements: list[int]):
        self.elements = elements

    def is_next_index_larger(self, x, y) -> bool | None:
        if x < len(self.elements):
            if y < len(self.elements):
                return self.elements[y] > self.elements[x]
        return None

    def iterate_through_list_and_count(self) -> int:
        count = 0
        for i in range(0, len(self.elements)-1):
            if self.is_next_index_larger(i, i + 1):
                count += 1
        return count


class InputHandler:
    elements: list

    def __init__(self, e=None):
        if e is not None:
            self.element = e

    def handle_raw_input(self, raw_input):
        self.elements = []
        for line in raw_input.split('\n'):
            self.elements.append(int(line.strip()))


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
    data = """3
            2
            3
            1
            4"""
    i = InputHandler()
    i.handle_raw_input(data)
    it = IncreasingTester(i.elements)
    print(it.iterate_through_list_and_count())
