from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


COMPASS_TURN = {
    Direction.NORTH: {
        "L": Direction.WEST,
        "R": Direction.EAST
    },
    Direction.EAST: {
        "L": Direction.NORTH,
        "R": Direction.SOUTH
    },
    Direction.SOUTH: {
        "L": Direction.EAST,
        "R": Direction.WEST
    },
    Direction.WEST: {
        "L": Direction.SOUTH,
        "R": Direction.NORTH
    },
}


class Sleigh:
    __heading: Direction
    __x: int
    __y: int
    __locations_visited: dict
    __done: int
    __answer: int

    def __init__(self):
        self.__heading = Direction.NORTH
        self.__x = 0
        self.__y = 0
        self.__locations_visited = dict()
        self.__visit_location()
        self.__done = False
        self.__answer = -1

    def set_heading(self, heading_to_set: Direction):
        self.__heading = heading_to_set

    def _turn(self, turn_direction: str) -> None:
        self.__heading = COMPASS_TURN[self.__heading][turn_direction]

    def get_heading(self) -> Direction:
        return self.__heading

    def _move(self, distance_to_move: int):
        if self.get_heading() == Direction.NORTH:
            self.__move_north(distance_to_move)
        if self.get_heading() == Direction.EAST:
            self.__move_east(distance_to_move)
        if self.get_heading() == Direction.SOUTH:
            self.__move_south(distance_to_move)
        if self.get_heading() == Direction.WEST:
            self.__move_west(distance_to_move)

    def __move_west(self, distance_to_move):
        for _ in range(distance_to_move):
            self.__x -= 1
            self.__visit_location()

    def __move_south(self, distance_to_move):
        for _ in range(distance_to_move):
            self.__y += 1
            self.__visit_location()

    def __move_east(self, distance_to_move):
        for _ in range(distance_to_move):
            self.__x += 1
            self.__visit_location()

    def __move_north(self, distance_to_move):
        for _ in range(distance_to_move):
            self.__y -= 1
            self.__visit_location()

    def get_location(self):
        return self.__x, self.__y

    def __visit_location(self):
        loc = self.__x, self.__y
        if loc not in self.__locations_visited.keys():
            self.__locations_visited[loc] = 0
        self.__locations_visited[loc] += 1
        self._check_if_done(loc)

    def _check_if_done(self, loc):
        if self.__locations_visited[loc] == 2:
            if not self.__done:
                self.__answer = self.get_move_distance_from_origin()
                self.__done = True

    def _move_and_turn(self, current_instruction: tuple[str, int]):
        _direction, _distance = current_instruction
        self._turn(_direction)
        self._move(_distance)

    def use_instructions(self, instructions_to_use: list[tuple[str, int]]):
        for instruction in instructions_to_use:
            if not self.__done:
                self._move_and_turn(instruction)

    def get_move_distance_from_origin(self) -> int:
        return abs(self.__x) + abs(self.__y)

    def _get_locations_visited(self) -> dict[tuple[int, int], int]:
        return self.__locations_visited

    def get_answer(self)->int:
        if self.__done:
            return self.__answer
        return -1


def generate_instructions(_input_str: str) -> list[tuple[str, int]]:
    _instructions = []
    for piece in [_.strip() for _ in _input_str.split(",")]:
        _direction = piece[0]
        _distance = int(piece[1:])
        _instructions.append((_direction, _distance))
    return _instructions
