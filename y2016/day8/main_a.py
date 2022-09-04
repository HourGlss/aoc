from enum import Enum

from y2016.day8.data import width as WIDTH, height as HEIGHT


class IncompleteData(Exception):
    ...


class TooManySpecificInputs(Exception):
    ...


class BadGridSize(Exception):
    ...


class TypeInstruction(Enum):
    RECT = 0
    ROTATE_ROW = 1
    ROTATE_COL = 2


class Instruction:
    type_of_instruction: TypeInstruction
    width: int | None
    height: int | None
    y_index: int | None
    x_index: int | None
    rotation_amount: int | None

    def __init__(self, type_of_instruction: TypeInstruction, width: int = None, height: int = None,
                 x_index: int = None, y_index: int = None, rotation_amount: int = None):
        self.type_of_instruction = type_of_instruction

        # PERFORM ERROR CHECKING
        if type_of_instruction == TypeInstruction.ROTATE_COL or type_of_instruction == TypeInstruction.ROTATE_ROW:
            if rotation_amount is None:
                raise IncompleteData
            if x_index is not None:
                if y_index is not None:
                    raise TooManySpecificInputs
            if y_index is not None:
                if x_index is not None:
                    raise TooManySpecificInputs
            if width is not None or height is not None:
                raise TooManySpecificInputs
        if type_of_instruction == TypeInstruction.RECT:
            if width is None or height is None:
                raise IncompleteData
            if width <= 0:
                raise BadGridSize
            if height <= 0:
                raise BadGridSize
            if width > WIDTH:
                raise BadGridSize
            if height > HEIGHT:
                raise BadGridSize

        # HANDLE ACTUAL CREATION
        if type_of_instruction == TypeInstruction.RECT:
            self.width = width
            self.height = height

        if type_of_instruction == type_of_instruction.ROTATE_COL:
            self.x_index = x_index
            self.rotation_amount = rotation_amount

        if type_of_instruction == type_of_instruction.ROTATE_ROW:
            self.y_index = y_index
            self.rotation_amount = rotation_amount


class LightGrid:
    width: int
    height: int
    grid: list[list[int]]

    def __init__(self, width=-1, height=-1):
        self.grid = []
        self.width = width
        self.height = height
        if width <= 0:
            raise BadGridSize
        if height <= 0:
            raise BadGridSize
        self.create_grid()

    def create_grid(self) -> None:
        grid = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(0)
            grid.append(row)
        self.grid = grid

    def get_grid_dimensions(self):
        return len(self.grid[0]), len(self.grid)

    def use_instruction(self, instruction: Instruction):
        if instruction.type_of_instruction == TypeInstruction.RECT:
            self.create_light_box(instruction)
        if instruction.type_of_instruction == TypeInstruction.ROTATE_COL:
            self.rotate_column(instruction)
        if instruction.type_of_instruction == TypeInstruction.ROTATE_ROW:
            self.rotate_row(instruction)

    def rotate_row(self, instruction: Instruction):
        for _ in range(instruction.rotation_amount):
            data = self.grid[instruction.y_index].pop(self.width - 1)
            self.grid[instruction.y_index].insert(0, data)

    def rotate_column(self, instruction: Instruction):
        for _ in range(instruction.rotation_amount):
            useful_data = None
            for i in range(self.height - 1, -1, -1):
                if i == self.height - 1:
                    useful_data = self.grid[i][instruction.x_index]
                    continue
                data = self.grid[i][instruction.x_index]

                self.grid[i + 1][instruction.x_index] = data
            self.grid[0][instruction.x_index] = useful_data

    def create_light_box(self, instruction: Instruction):
        for y in range(instruction.height):
            for x in range(instruction.width):
                self.grid[y][x] = 1

    def print_grid(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 1:
                    disp = "#"
                else:
                    disp = "."
                print(disp, end='')
            print()

    def count_lit(self) -> int:
        total_lit = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 1:
                    total_lit += 1
        return total_lit


class InputHandler:
    instructions: list[Instruction]

    def __init__(self):
        self.instructions = []

    def handle_raw_input(self, raw_input):
        data = raw_input.split('\n')
        for line in data:
            self.instructions.append(self.create_instruction(line))

    @staticmethod
    def create_instruction(line: str) -> Instruction:
        if line.startswith("rect"):
            pieces = line.split(" ")
            subpieces = pieces[1].split("x")
            subpieces = [int(_) for _ in subpieces]
            width, height = subpieces[0], subpieces[1]
            return Instruction(TypeInstruction.RECT, width=width, height=height)
        if line.startswith("rotate"):
            if "x=" in line:
                # rotate column x=1 by 1
                pieces = line.split(" ")
                subpieces = pieces[2].split("=")
                x_index = int(subpieces[1])
                rotation_amount = int(pieces[4])
                return Instruction(TypeInstruction.ROTATE_COL, rotation_amount=rotation_amount, x_index=x_index)
            else:
                # rotate row y=0 by 4
                pieces = line.split(" ")
                subpieces = pieces[2].split("=")
                y_index = int(subpieces[1])
                rotation_amount = int(pieces[4])
                return Instruction(TypeInstruction.ROTATE_ROW, rotation_amount=rotation_amount, y_index=y_index)


class OutputHandler:
    inputHandler: InputHandler
    output: int
    lightgrid: LightGrid

    def __init__(self, i: InputHandler, lightgrid: LightGrid):
        self.inputHandler = i
        self.lightgrid = lightgrid
        self.output = 0
        self.build_output()

    def build_output(self):
        for instruction in self.inputHandler.instructions:
            self.lightgrid.use_instruction(instruction)

    def get_output(self):
        return self.lightgrid.count_lit()


if __name__ == "__main__":
    from y2016.day8.data import test_input

    i = InputHandler()
    i.handle_raw_input(test_input)
    l = LightGrid(width=7, height=3)
    o = OutputHandler(i, l)
    assert o.get_output() == 6
