from enum import Enum


class MoveDirection(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class OffKeypad(Exception):
    ...


class InvalidDirection(Exception):
    ...


class Keypad:
    keypad: list[list[int]]
    __height: int
    __width: int
    current_x: int
    current_y: int

    def __init__(self,
                 height=3,
                 width=3):
        self.__height = height
        self.__width = width
        self.keypad = []
        counter = 1
        for y in range(height):
            row = []
            for x in range(width):
                row.append(counter)
                counter += 1
            self.keypad.append(row)
        self.current_x = int(width / 2)
        self.current_y = int(height / 2)

    def print_keypad(self):
        largest = len(str(self.keypad[self.__height - 1][self.__width - 1]))
        for y in range(self.__height):
            row = []
            for x in range(self.__width):
                row.append(f"{self.keypad[y][x]:>{largest}}")
            print(" ".join(row))

    def get_key_at_location(self):
        return self.keypad[self.current_y][self.current_x]

    def move_up(self):
        if self.current_y - 1 >= 0:
            self.current_y -= 1
        else:
            raise OffKeypad

    def move_down(self):
        if self.current_y + 1 <= self.__height - 1:
            self.current_y += 1
        else:
            raise OffKeypad

    def move_left(self):
        if self.current_x - 1 >= 0:
            self.current_x -= 1
        else:
            raise OffKeypad

    def move_right(self):
        if self.current_x + 1 <= self.__width - 1:
            self.current_x += 1
        else:
            raise OffKeypad

    def move(self, direction: MoveDirection):
        if direction == MoveDirection.RIGHT:
            try:
                self.move_right()
            except OffKeypad:
                pass
        elif direction == MoveDirection.LEFT:
            try:
                self.move_left()
            except OffKeypad:
                pass
        elif direction == MoveDirection.UP:
            try:
                self.move_up()
            except OffKeypad:
                pass
        elif direction == MoveDirection.DOWN:
            try:
                self.move_down()
            except OffKeypad:
                pass
        else:
            raise ValueError("Cannot move that way")

    def use_directions_and_get_key(self, directions) -> int:
        for direction in directions:
            self.move(direction)
        return self.get_key_at_location()


class InputHandler:
    instructions: list[list[MoveDirection]]

    def __init__(self):
        self.instructions = []

    @staticmethod
    def get_direction(direction: str):
        if direction == "L":
            return MoveDirection.LEFT
        if direction == "R":
            return MoveDirection.RIGHT
        if direction == "U":
            return MoveDirection.UP
        if direction == "D":
            return MoveDirection.DOWN
        raise InvalidDirection(f"Not a valid direction {direction}")

    @staticmethod
    def get_directions_from_line(line: str) -> list[MoveDirection] | None:
        directions = []
        for c in line:
            try:
                directions.append(InputHandler.get_direction(c))
            except InvalidDirection:
                return
        return directions

    def handle_raw_input(self, raw_input):
        lines = raw_input.split("\n")
        for line in lines:
            _ = InputHandler.get_directions_from_line(line)
            if _ is not None:
                self.instructions.append(_)
            else:
                raise ValueError(f"Bad input {raw_input}")


class OutputHandler:
    keypad: Keypad
    inputHandler: InputHandler
    output:str

    def __init__(self, k: Keypad, i: InputHandler):
        self.keypad = k
        self.inputHandler = i
        self.output = ""

    def build_output(self):
        for list_instructions in self.inputHandler.instructions:
            for instruction in list_instructions:
                self.keypad.move(instruction)
            self.output += str(self.keypad.get_key_at_location())

    def get_output(self):
        return self.output

