from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    FORWARD = 2


class Instruction:
    type_of_instruction: Direction
    amount: int

    def __init__(self, amount: int = -1, type_of_instruction: Direction = None):
        self.amount = amount
        self.type_of_instruction = type_of_instruction


class Submarine:
    horizontal_position: int
    depth: int
    aim:int
    def __init__(self):
        self.horizontal_position = 0
        self.depth = 0
        self.aim = 0

    def use_instruction(self, instruction: Instruction):
        if instruction.type_of_instruction == Direction.UP:
            self.move_up(instruction)
        if instruction.type_of_instruction == Direction.DOWN:
            self.move_down(instruction)
        if instruction.type_of_instruction == Direction.FORWARD:
            self.move_forward(instruction)

    def move_up(self, instruction):
        self.aim -= instruction.amount

    def move_down(self, instruction):
        self.aim += instruction.amount

    def move_forward(self, instruction):
        # print(f"Adding {instruction.amount} to horizontal")
        # print(f"\twas {self.horizontal_position}")
        self.horizontal_position += instruction.amount
        # print(f"\tis {self.horizontal_position}")
        depth_delta = (self.aim * instruction.amount)
        # print(f"Adding {depth_delta} to depth")
        # print(f"\twas {self.depth}")
        self.depth += depth_delta
        # print(f"\tis {self.depth}")

    def get_result_of_planned_course(self):
        return self.depth * self.horizontal_position


class InvalidSubDirection(Exception):
    ...


class InputHandler:
    elements: list[Instruction]

    def __init__(self):
        self.elements = []

    def handle_raw_input(self, raw_input: str):
        for line in raw_input.split('\n'):
            self.elements.append(InputHandler.create_instruction(line.strip()))

    @staticmethod
    def create_instruction(line: str) -> Instruction:
        pieces = line.split(" ")
        toi = None
        if line.startswith("forward"):
            toi = Direction.FORWARD
        if line.startswith("up"):
            toi = Direction.UP
        if line.startswith("down"):
            toi = Direction.DOWN
        amount = int(pieces[1])
        if toi is not None:
            return Instruction(amount=amount, type_of_instruction=toi)
        else:
            raise InvalidSubDirection(f"{pieces[0]} seems to be invalid")


class OutputHandler:
    inputHandler: InputHandler
    output: int
    submarine: Submarine

    def __init__(self, i: InputHandler, s: Submarine):
        self.inputHandler = i
        self.output = 0
        self.submarine = s
        self.build_output()

    def build_output(self):
        for instruction in self.inputHandler.elements:
            self.submarine.use_instruction(instruction)

    def get_output(self):
        return self.submarine.get_result_of_planned_course()


if __name__ == "__main__":
    from y2021.day2.data import test_input
    i = InputHandler()
    i.handle_raw_input(raw_input=test_input)
    s = Submarine()
    o = OutputHandler(i, s)
    assert s.depth == 60
    assert s.horizontal_position == 15

