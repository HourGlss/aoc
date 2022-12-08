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

    def run(self) -> int:
        steps = 0
        while True:
            steps += 1
            check = self.tick()
            if check:
                break
        return steps

    def tick(self) -> bool:
        count = 0
        count += self.move_eastern_cucumbers()
        count += self.move_southern_cucumbers()
        if count == 0:
            return True
        return False

    def move_eastern_cucumbers(self) -> int:
        return SeaFloor.tag_and_move_cucumbers(self.height, self.tag_eastern, self.move_eastern)

    def move_southern_cucumbers(self) -> int:
        return SeaFloor.tag_and_move_cucumbers(self.width, self.tag_southern, self.move_southern)

    @staticmethod
    def tag_and_move_cucumbers(dimension, tag_fn, move_fn) -> int:
        how_many_move = 0
        for i in range(dimension):
            tagged: list[int] = []
            how_many_move = tag_fn(how_many_move, tagged, i)
            move_fn(tagged, i)
        return how_many_move

    def tag_eastern(self, how_many_move: int, tagged: list[int], y: int) -> int:
        for x, y in self.east_facing_tiles_in_row(y):
            next_x = self.next_tile_east(x)
            if self.is_empty(next_x, y):
                tagged.append(next_x)
                how_many_move += 1
        return how_many_move

    def east_facing_tiles_in_row(self, y: int) -> list[tuple[int, int]]:
        for x in range(self.width):
            if self.floor[y][x] == FloorSpot.EAST:
                yield x, y

    def next_tile_east(self, x: int) -> int:
        next_x = (x + 1) % self.width
        return next_x

    def tag_southern(self, how_many_move: int, tagged: list[int], x: int) -> int:
        for x, y in self.south_facing_tiles_in_column(x):
            next_y = self.next_tile_south(y)
            if self.is_empty(x, next_y):
                tagged.append(next_y)
                how_many_move += 1
        return how_many_move

    def south_facing_tiles_in_column(self, x: int) -> list[tuple[int, int]]:
        for y in range(self.height):
            if self.floor[y][x] == FloorSpot.SOUTH:
                yield x, y

    def next_tile_south(self, y: int) -> int:
        next_y = (y + 1) % self.height
        return next_y

    def is_empty(self, x, y) -> bool:
        return self.floor[y][x] == FloorSpot.EMPTY

    def move_eastern(self, tagged: list[int], y: int) -> None:
        for x in tagged:
            self.floor[y][x] = FloorSpot.EAST
            self.floor[y][x - 1] = FloorSpot.EMPTY

    def move_southern(self, tagged: list[int], x: int) -> None:
        for y in tagged:
            self.floor[y][x] = FloorSpot.SOUTH
            self.floor[y - 1][x] = FloorSpot.EMPTY

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
