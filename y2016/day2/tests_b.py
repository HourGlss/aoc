import pytest

from y2016.day2.main_b import OutputHandler, Keypad, OffKeypad, MoveDirection, InputHandler, InvalidDirection
from y2016.day2.data import test_input


def test_build_keypad():
    k = Keypad()


def test_get_current_key_at_location():
    k = Keypad()
    k.current_y = 2
    k.current_x = 2
    assert k.get_key_at_location() == "7"


def test_movement_and_get_valid_current_key_at_location():
    k = Keypad()
    k.current_y = 2
    k.current_x = 2
    assert k.get_key_at_location() == "7"
    k.move_down()
    assert k.get_key_at_location() == "B"


def test_a():
    k = Keypad()
    k.move_right()
    assert k.get_key_at_location() == "6"


def test_move_with_MoveDirection_valid_and_invalid():
    k = Keypad()
    k.current_y = 2
    k.current_x = 2
    k.move(MoveDirection.UP)
    assert k.get_key_at_location() == "3"
    k.move(MoveDirection.UP)
    assert k.get_key_at_location() == "1"
    k.move(MoveDirection.UP)
    assert k.get_key_at_location() == "1"


def test_create_input_handler():
    i = InputHandler()


def test_create_direction_from_input_character_valid_and_nonvalid():
    i = InputHandler()
    out = i.get_direction("L")
    assert out == MoveDirection.LEFT
    out = i.get_direction("R")
    assert out == MoveDirection.RIGHT
    out = i.get_direction("U")
    assert out == MoveDirection.UP
    out = i.get_direction("D")
    assert out == MoveDirection.DOWN
    with pytest.raises(InvalidDirection):
        out = i.get_direction("X")


def test_create_directions_from_input_line():
    i = InputHandler()
    testlines = test_input.split('\n')
    line = testlines[0]
    out = i.get_directions_from_line(line)
    assert out == [MoveDirection.UP, MoveDirection.LEFT, MoveDirection.LEFT]


def test_keypad_uses_multiple_directions():
    k = Keypad()
    i = InputHandler()
    testlines = test_input.split('\n')
    line = testlines[0]
    out = i.get_directions_from_line(line)
    assert k.use_directions_and_get_key(out) == "5"


def test_keypad_uses_multiple_lines():
    i = InputHandler()
    i.handle_raw_input(test_input)
    assert i.instructions == [
        [MoveDirection.UP, MoveDirection.LEFT, MoveDirection.LEFT],
        [MoveDirection.RIGHT, MoveDirection.RIGHT, MoveDirection.DOWN, MoveDirection.DOWN, MoveDirection.DOWN],
        [MoveDirection.LEFT, MoveDirection.UP, MoveDirection.RIGHT, MoveDirection.DOWN, MoveDirection.LEFT],
        [MoveDirection.UP, MoveDirection.UP, MoveDirection.UP, MoveDirection.UP, MoveDirection.DOWN]
    ]


def test_build_output():
    k = Keypad()
    i = InputHandler()
    i.handle_raw_input(test_input)
    o = OutputHandler(k, i)


def test_run_full_test():
    k = Keypad()
    i = InputHandler()
    i.handle_raw_input(test_input)
    o = OutputHandler(k, i)
    o.build_output()
    assert o.get_output() == "5DB3"
