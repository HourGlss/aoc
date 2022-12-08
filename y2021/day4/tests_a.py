import pytest

from y2021.day4.main_a import InputHandler, OutputHandler
from y2021.day4.data import test_draws, test_boards


def test_build_draws():
    i = InputHandler()
    i.handle_draws(test_draws)
    assert i.draws == [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]

def test_build_boards():
    i = InputHandler()
    i.handle_boards(test_boards)
    i.handle_draws(test_draws)
    o = OutputHandler(i)
    assert o.get_output() == 4512

