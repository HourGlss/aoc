class Triangle:
    sides: list[int]

    def __init__(self, list_of_sides:list[int]):
        self.sides = list_of_sides

    def is_possible(self):
        return self.sides[0] + self.sides[1] > self.sides[2]





class InputHandler:
    triangles: list[Triangle]

    def __init__(self):
        self.triangles = []

    @staticmethod
    def __reorganize_data(data):
        temp = []
        for y in range(3):
            current = []
            for x in range(3):
                current.append(data[x][y])
            temp.append(current)
        return temp

    def handle_raw_input(self, raw_input):
        lines = raw_input.split("\n")
        data = []
        for i in range(0,len(lines),3):
            current_chunk = []
            for _ in range(3):
                raw_input = lines[i+_].strip()
                raw_input = raw_input.replace("   ", " ")
                raw_input = raw_input.replace("  ", " ")
                sides = [int(e) for e in raw_input.split(" ")]
                current_chunk.append(sides)
            actual = self.__reorganize_data(current_chunk)
            for triangle_sides in actual:
                triangle_sides.sort()
                data.append(Triangle(triangle_sides))

        self.triangles = data



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

if __name__ == "__main__":
    i = InputHandler()
    from y2016.day3.data import test_input
    i.handle_raw_input(test_input)
