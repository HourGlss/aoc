import pytest

from y2021.day25.main_a import InputHandler,OutputHandler,SeaFloor
from y2021.day25.data import test_input


def test_create_seafloor():
    s = SeaFloor()
    i = InputHandler(s)
    i.handle_raw_input(test_input)

def test_move_one_row_of_cucumbers():
    s = SeaFloor()
    i = InputHandler(s)
    i.handle_raw_input("...>>>>>..v")
    s.tag_and_move_eastern_cucumbers()
    # s.print_floor()
    s.tag_and_move_eastern_cucumbers()
    # s.print_floor()

def test_move_column_of_cucumbers():
    s = SeaFloor()
    i = InputHandler(s)
    i.handle_raw_input("""v
    .
    .
    .
    .""")
    s.tag_and_move_southern_cucumbers()
    # s.print_floor()
    s.tag_and_move_southern_cucumbers()
    # s.print_floor()

def test_count_stop_movement():
    s = SeaFloor()
    i = InputHandler(s)
    i.handle_raw_input(test_input)
    assert s.run() == 58



