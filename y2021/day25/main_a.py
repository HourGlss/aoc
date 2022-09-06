from enum import Enum


class FloorSpot(Enum):
    SOUTH = 0
    EAST = 1
    EMPTY = 2


class SeaFloor:
    width: int
    height: int
    floor: list[list[FloorSpot]]

    def __init__(self):
        ...

    def set_size_of_floor(self, width: int = -1, height: int = -1) -> None:
        self.width = width
        self.height = height

    def print_floor(self) -> None:
        print("=" * self.width)
        for y in range(self.height):
            disp = ""
            for x in range(self.width):
                _ = self.floor[y][x]
                if _ == FloorSpot.SOUTH:
                    disp += "v"
                elif _ == FloorSpot.EAST:
                    disp += ">"
                elif _ == FloorSpot.EMPTY:
                    disp += "."
            print(disp)

    def tick(self) -> bool:
        count = 0
        count += self.tag_and_move_eastern_cucumbers()
        count += self.tag_and_move_southern_cucumbers()
        if count == 0:
            return True
        return False

    def tag_and_move_eastern_cucumbers(self) -> int:
        how_many_move = 0
        for y in range(self.height):
            tagged: list[int] = []
            how_many_move = self.tag_eastern(how_many_move, tagged, y)
            self.move_eastern(tagged, y)
        return how_many_move

    def tag_and_move_southern_cucumbers(self) -> int:
        how_many_move = 0
        for x in range(self.width):
            tagged: list[int] = []
            how_many_move = self.tag_southern(how_many_move, tagged, x)
            self.move_southern(tagged, x)
        return how_many_move

    def move_eastern(self, tagged: list[int], y: int) -> None:
        for x in range(self.width - 1, -1, -1):
            for _ in tagged:
                if x == _:
                    self.floor[y][x] = FloorSpot.EAST
                    if _ != 0:
                        self.floor[y][x - 1] = FloorSpot.EMPTY
                    else:
                        self.floor[y][self.width - 1] = FloorSpot.EMPTY

    def move_southern(self, tagged: list[int], x: int) -> None:
        for y in range(self.height - 1, -2, -1):
            for _ in tagged:
                if y == _:
                    if y == -1:
                        self.floor[self.height - 1][x] = FloorSpot.EMPTY
                        self.floor[0][x] = FloorSpot.SOUTH
                    else:
                        self.floor[y - 1][x] = FloorSpot.EMPTY
                        self.floor[y][x] = FloorSpot.SOUTH

    def tag_southern(self, how_many_move: int, tagged: list[int], x: int) -> int:
        for y in range(self.height - 1, -1, -1):
            if self.floor[y][x] == FloorSpot.SOUTH:
                if y + 1 < self.height:
                    if self.floor[y + 1][x] == FloorSpot.EMPTY:
                        tagged.append(y + 1)
                        how_many_move += 1
                else:
                    if self.floor[0][x] == FloorSpot.EMPTY:
                        tagged.append(-1)
                        how_many_move += 1
        return how_many_move

    def tag_eastern(self, how_many_move: int, tagged: list[int], y: int) -> int:
        for x in range(self.width - 1, -1, -1):
            if self.floor[y][x] == FloorSpot.EAST:
                if x + 1 < self.width:
                    if self.floor[y][x + 1] == FloorSpot.EMPTY:
                        tagged.append(x + 1)
                        how_many_move += 1
                else:
                    if self.floor[y][0] == FloorSpot.EMPTY:
                        tagged.append(0)
                        how_many_move += 1
        return how_many_move

    def run(self) -> int:
        steps = 0
        while True:
            steps += 1
            check = self.tick()
            if check:
                break
        return steps


class InputHandler:
    seafloor: SeaFloor

    def __init__(self, s):
        self.seafloor = s

    def set_size_of_seafloor(self, raw_input):
        data = raw_input.split('\n')
        width = len(data[0])
        height = len(data)
        self.seafloor.set_size_of_floor(width=width, height=height)

    def handle_raw_input(self, raw_input: str):
        self.set_size_of_seafloor(raw_input)
        data = raw_input.split('\n')
        floor = []
        for line in data:
            row = []
            for c in line.strip():
                if c == "v":
                    row.append(FloorSpot.SOUTH)
                elif c == ">":
                    row.append(FloorSpot.EAST)
                elif c == ".":
                    row.append(FloorSpot.EMPTY)
                else:
                    raise NotImplemented
            floor.append(row)
        self.seafloor.floor = floor


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
