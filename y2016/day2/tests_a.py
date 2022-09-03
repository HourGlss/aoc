import pytest

from y2016.day2.main_a import OutputHandler, Keypad, OffKeypad, MoveDirection, InputHandler, InvalidDirection
from y2016.day2.data import test_input


def test_build_keypad():
    k = Keypad(height=3, width=3)


def test_get_current_key_at_location():
    k = Keypad()
    assert k.get_key_at_location() == 5


def test_movement_and_get_valid_current_key_at_location():
    k = Keypad()
    k.move_up()
    assert k.get_key_at_location() == 2
    k = Keypad()
    k.move_down()
    assert k.get_key_at_location() == 8
    k = Keypad()
    k.move_left()
    assert k.get_key_at_location() == 4
    k = Keypad()
    k.move_right()
    assert k.get_key_at_location() == 6


def test_invalid_movement():
    k = Keypad()
    k.current_y = 0
    k.current_x = 0
    with pytest.raises(OffKeypad):
        k.move_up()
    with pytest.raises(OffKeypad):
        k.move_left()
    k.current_y = 0
    k.current_x = 1
    with pytest.raises(OffKeypad):
        k.move_up()
    k.current_y = 0
    k.current_x = 2
    with pytest.raises(OffKeypad):
        k.move_up()
    with pytest.raises(OffKeypad):
        k.move_right()
    k.current_y = 2
    k.current_x = 2
    with pytest.raises(OffKeypad):
        k.move_right()
    with pytest.raises(OffKeypad):
        k.move_down()


def test_move_with_MoveDirection_valid_and_invalid():
    k = Keypad()
    k.move(MoveDirection.UP)
    assert k.get_key_at_location() == 2
    k.move(MoveDirection.UP)
    assert k.get_key_at_location() == 2


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
    assert k.use_directions_and_get_key(out) == 1


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
    o = OutputHandler(k,i)

def test_run_full_test():
    k = Keypad()
    i = InputHandler()
    i.handle_raw_input(test_input)
    o = OutputHandler(k,i)
    o.build_output()
    assert o.get_output() == "1985"
