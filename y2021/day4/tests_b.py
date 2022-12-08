import pytest

from y2021.day4.main_b import InputHandler, OutputHandler
from y2021.day4.data import test_draws, test_boards

def test_build_boards():
    i = InputHandler()
    i.handle_boards(test_boards)
    i.handle_draws(test_draws)
    o = OutputHandler(i)
    assert o.get_output() == 1924

