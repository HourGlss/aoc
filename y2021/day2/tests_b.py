import pytest

from y2021.day2.main_b import InputHandler,OutputHandler,Submarine
from y2021.day2.data import test_input

def test_submarine_move_with_aim():
    i = InputHandler()
    i.handle_raw_input(raw_input=test_input)
    s = Submarine()
    o = OutputHandler(i, s)
    assert s.depth == 60
    assert s.horizontal_position == 15


