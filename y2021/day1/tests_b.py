import pytest

from y2021.day1.main_b import InputHandler,OutputHandler,IncreasingTester
from y2021.day1.data import test_input


def test_break_input_list_into_sliding_windows():
    i = InputHandler()
    i.handle_raw_input(test_input)
    assert i.elements == [607, 618, 618, 617, 647, 716, 769, 792]

def test_ensure_test_input_is_correct():
    i = InputHandler()
    i.handle_raw_input(test_input)
    ita = IncreasingTester(i.elements)
    assert ita.iterate_through_list_and_count() == 5






