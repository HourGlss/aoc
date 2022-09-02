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


    def __init__(self):
        self.heading = Direction.NORTH
        self.x = 0
        self.y = 0


    def set_heading(self, heading_to_set):
        self.heading = heading_to_set

    def turn(self, turn_direction):
        self.heading = COMPASS_TURN[self.heading][turn_direction]

    def get_heading(self):
        return self.heading



    def move(self, distance_to_move: int):
        if self.get_heading() == Direction.NORTH:
            self.y -= distance_to_move
        if self.get_heading() == Direction.EAST:
            self.x += distance_to_move
        if self.get_heading() == Direction.SOUTH:
            self.y += distance_to_move
        if self.get_heading() == Direction.WEST:
            self.x -= distance_to_move

    def get_location(self):
        return self.x, self.y

    def move_and_turn(self, current_instruction: tuple[str, int]):
        _direction, _distance = current_instruction
        self.turn(_direction)
        self.move(_distance)

    def use_instructions(self, instructions_to_use: list[tuple[str, int]]):
        for instruction in instructions_to_use:
            self.move_and_turn(instruction)

    def get_move_distance_from_origin(self):
        return abs(self.x) + abs(self.y)




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
    s.use_instructions(instructions)
    print(s.get_move_distance_from_origin())