from y2016.day1.main_a import *


def test_turn():
    s = Sleigh()
    s.set_heading(Direction.NORTH)
    s.turn("L")
    direction = s.get_heading()
    assert direction == Direction.WEST
    s.set_heading(Direction.EAST)
    s.turn("R")
    direction = s.get_heading()
    assert direction == Direction.SOUTH
    s.turn("R")
    direction = s.get_heading()
    assert direction == Direction.WEST


def test_move():
    s = Sleigh()
    s.move(5)
    assert s.get_location() == (0, -5)
    s = Sleigh()
    s.set_heading(Direction.EAST)
    s.move(5)
    assert s.get_location() == (5, 0)
    s = Sleigh()
    s.set_heading(Direction.SOUTH)
    s.move(5)
    assert s.get_location() == (0, 5)
    s = Sleigh()
    s.set_heading(Direction.WEST)
    s.move(5)
    assert s.get_location() == (-5, 0)


def test_raw_input():
    input1 = "R2, L3"
    output1 = generate_instructions(input1)
    assert output1 == [("R", 2), ("L", 3)]
    input2 = "R2, R2, R2"
    output2 = generate_instructions(input2)
    assert output2 == [("R", 2), ("R", 2), ("R", 2)]
    input3 = "R5, L5, R5, R3"
    output3 = generate_instructions(input3)
    assert output3 == [("R", 5), ("L", 5), ("R", 5), ("R", 3)]


def test_move_and_turn():
    input1 = "R2, L3"
    output1 = generate_instructions(input1)
    s = Sleigh()
    s.use_instructions(output1)
    current_x, current_y = s.get_location()
    assert current_x == 2
    assert current_y == -3


def test_answer_puzzle():
    input1 = "R2, L3"
    output1 = generate_instructions(input1)
    s = Sleigh()
    s.use_instructions(output1)
    blocks_away = s.get_answer()
    assert blocks_away == 5
    input2 = "R2, R2, R2"
    output2 = generate_instructions(input2)
    s = Sleigh()
    s.use_instructions(output2)
    blocks_away = s.get_answer()
    assert blocks_away == 2
    input3 = "R5, L5, R5, R3"
    output3 = generate_instructions(input3)
    s = Sleigh()
    s.use_instructions(output3)
    blocks_away = s.get_answer()
    assert blocks_away == 12


