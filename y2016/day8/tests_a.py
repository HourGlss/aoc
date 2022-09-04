import pytest

from y2016.day8.main_a import LightGrid, InputHandler, BadGridSize, Instruction, OutputHandler
from y2016.day8.data import test_input, width, height


def test_create_lightgrid_and_check_sizes():
    l = LightGrid(width=width, height=height)
    l.create_grid()
    assert l.width == width
    assert l.height == height
    assert l.get_grid_dimensions() == (width, height)


def test_bad_sizes_for_lightgrid():
    with pytest.raises(BadGridSize):
        l = LightGrid(width=0, height=5)
    with pytest.raises(BadGridSize):
        l = LightGrid(width=-1, height=5)

    with pytest.raises(BadGridSize):
        l = LightGrid(width=5, height=0)
    with pytest.raises(BadGridSize):
        l = LightGrid(width=5, height=-1)


def test_handle_rect_valid_input():
    data = test_input.split('\n')
    data = data[0]
    i = InputHandler()
    # One line from input
    instruction = i.create_instruction(data)
    assert isinstance(instruction, Instruction)
    assert instruction.width == 3
    assert instruction.height == 2
    instruction = i.create_instruction("rect 50x6")
    instruction = i.create_instruction("rect 1x1")


def test_handle_rect_invalid_input():
    i = InputHandler()
    with pytest.raises(BadGridSize):
        instruction = i.create_instruction("rect 0x5")
    with pytest.raises(BadGridSize):
        instruction = i.create_instruction("rect -1x5")
    with pytest.raises(BadGridSize):
        instruction = i.create_instruction("rect 5x0")
    with pytest.raises(BadGridSize):
        instruction = i.create_instruction("rect 5x-1")
    with pytest.raises(BadGridSize):
        instruction = i.create_instruction("rect 51x5")
    with pytest.raises(BadGridSize):
        instruction = i.create_instruction("rect 5x7")


def test_use_rect_instruction():
    l = LightGrid(width=7, height=3)
    l.create_grid()
    data = test_input.split('\n')
    data = data[0]
    i = InputHandler()
    # One line from input
    instruction = i.create_instruction(data)
    l.use_instruction(instruction)
    # l.print_grid()


def test_build_all_instruction_types():
    data = test_input.split('\n')
    i = InputHandler()
    for _ in range(len(data)):
        d = data[_]
        instruction = i.create_instruction(d)


def test_use_all_instruction_types():
    data = test_input.split('\n')
    i = InputHandler()
    l = LightGrid(width=width, height=height)
    l.create_grid()
    for _ in range(len(data)):
        d = data[_]
        instruction = i.create_instruction(d)
        l.use_instruction(instruction)


def test_count_lit():
    i = InputHandler()
    i.handle_raw_input(test_input)
    l = LightGrid(width=7, height=3)
    o = OutputHandler(i, l)
    assert o.get_output() == 6

