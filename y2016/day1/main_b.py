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
    heading: Direction
    x: int
    y: int
    locations_visited: dict

    def __init__(self):
        self.heading = Direction.NORTH
        self.x = 0
        self.y = 0
        self.locations_visited = dict()
        self.visit_location()

    def set_heading(self, heading_to_set):
        self.heading = heading_to_set

    def turn(self, turn_direction):
        self.heading = COMPASS_TURN[self.heading][turn_direction]

    def get_heading(self):
        return self.heading

    def move(self, distance_to_move: int) -> bool:
        if self.get_heading() == Direction.NORTH:
            for _ in range(distance_to_move):
                self.y -= 1
                if self.visit_location():
                    return True
        if self.get_heading() == Direction.EAST:
            for _ in range(distance_to_move):
                self.x += 1
                if self.visit_location():
                    return True
        if self.get_heading() == Direction.SOUTH:
            for _ in range(distance_to_move):
                self.y += 1
                if self.visit_location():
                    return True
        if self.get_heading() == Direction.WEST:
            for _ in range(distance_to_move):
                self.x -= 1
                if self.visit_location():
                    return True
        return False

    def get_location(self):
        return self.x, self.y

    def visit_location(self) -> bool:
        loc = self.x, self.y
        if loc not in self.locations_visited.keys():
            self.locations_visited[loc] = 0
        self.locations_visited[loc] += 1
        if self.locations_visited[loc] == 2:
            return True
        return False

    def move_and_turn(self, current_instruction: tuple[str, int]) -> bool:
        _direction, _distance = current_instruction
        self.turn(_direction)
        if self.move(_distance):
            return True
        return False

    def use_instructions(self, instructions_to_use: list[tuple[str, int]])->bool:
        for instruction in instructions_to_use:
            if self.move_and_turn(instruction):
                break
        else:
            return False
        return True

    def get_move_distance_from_origin(self):
        return abs(self.x) + abs(self.y)

    def get_locations_visited(self):
        return self.locations_visited


def generate_instructions(_input_str: str) -> list[tuple[str, int]]:
    _instructions = []
    for piece in [_.strip() for _ in _input_str.split(",")]:
        _direction = piece[0]
        _distance = int(piece[1:])
        _instructions.append((_direction, _distance))
    return _instructions


if __name__ == "__main__":
    from data import raw_input

    s = Sleigh()
    instructions = generate_instructions(raw_input)
    if s.use_instructions(instructions):
        print(s.get_move_distance_from_origin())
