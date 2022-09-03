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
    keypad: list[list[str | None]]
    __height: int
    __width: int
    current_x: int
    current_y: int

    def __init__(self):
        self.__height = 5
        self.__width = 5
        self.keypad = [
            [None, None, "1", None, None],
            [None, "2", "3", "4", None],
            ["5", "6", "7", "8", "9"],
            [None, "A", "B", "C", None],
            [None, None, "D", None, None],
        ]
        self.current_x = 0
        self.current_y = 2

    def print_keypad(self):
        largest = len(str(self.keypad[2][2]))
        for y in range(self.__height):
            row = []
            for x in range(self.__width):
                if self.keypad[y][x] is not None:
                    row.append(f"{self.keypad[y][x]:>{largest}}")
                else:
                    row.append(f" ")
            print(" ".join(row))

    def get_key_at_location(self, loc: tuple[int, int] = None) -> str | None:
        if loc is not None:
            x, y = loc
        else:
            x, y = self.current_x, self.current_y

        return self.keypad[y][x]

    def move_up(self):
        x = self.current_x
        y = self.current_y - 1
        if y < 0 or y == self.__height:
            raise OffKeypad
        if self.get_key_at_location((x, y)) is not None:
            self.current_y -= 1
        else:
            raise OffKeypad

    def move_down(self):
        x = self.current_x
        y = self.current_y + 1
        if y < 0 or y == self.__height:
            raise OffKeypad
        if self.get_key_at_location((x, y)) is not None:
            self.current_y += 1
        else:
            raise OffKeypad

    def move_left(self):
        x = self.current_x - 1
        y = self.current_y
        if x < 0 or x == self.__width:
            raise OffKeypad
        if self.get_key_at_location((x, y)) is not None:
            self.current_x -= 1
        else:
            raise OffKeypad

    def move_right(self):
        x = self.current_x + 1
        y = self.current_y
        if x < 0 or x == self.__width:
            raise OffKeypad
        if self.get_key_at_location((x, y)) is not None:
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

    def use_directions_and_get_key(self, directions) -> str:
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
    output: str

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


if __name__ == "__main__":
    k = Keypad()
    k.print_keypad()
