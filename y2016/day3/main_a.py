class Triangle:
    sides: list[int]

    def __init__(self, raw_input:str):
        raw_input = raw_input.strip()
        raw_input = raw_input.replace("   ", " ")
        raw_input = raw_input.replace("  ", " ")
        sides = [int(e) for e in raw_input.split(" ")]
        sides.sort()
        self.sides = sides

    def is_possible(self):
        return self.sides[0] + self.sides[1] > self.sides[2]


class InputHandler:
    triangles: list[Triangle]

    def __init__(self):
        self.triangles = []

    def handle_raw_input(self, raw_input):
        lines = raw_input.split("\n")
        for line in lines:
            self.triangles.append(Triangle(line))


class OutputHandler:
    inputHandler: InputHandler
    output: int

    def __init__(self, i):
        self.inputHandler = i
        self.output = 0

    def build_output(self):
        for triangle in self.inputHandler.triangles:
            if triangle.is_possible():
                self.output += 1

    def get_output(self):
        return self.output
