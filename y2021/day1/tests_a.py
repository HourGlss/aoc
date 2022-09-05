import pytest

from y2021.day1.main_a import InputHandler,OutputHandler,IncreasingTester
from y2021.day1.data import test_input


def test_break_into_list_of_ints():
    data = """1
    2
    3"""

    i = InputHandler()
    i.handle_raw_input(data)
    assert i.elements == [1,2,3]

def test_if_checking_indexes_works():
    data = """3
        2
        3"""

    i = InputHandler()
    i.handle_raw_input(data)
    it = IncreasingTester(i.elements)
    assert it.is_next_index_larger(0,1) == False
    assert it.is_next_index_larger(1,2) == True

def test_get_two_indexes_at_a_time():
    data = """3
            2
            3
            1
            4"""
    i = InputHandler()
    i.handle_raw_input(data)
    ita = IncreasingTester(i.elements)
    assert ita.iterate_through_list_and_count() == 2


