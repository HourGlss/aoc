import pytest

from y2021.day3.main_a import InputHandler, OutputHandler, PowerConsumption
from y2021.day3.data import test_input


def test_gamma_and_epsilon():
    i = InputHandler()
    i.handle_raw_input(test_input)
    p = PowerConsumption(i.elements)
    assert p.get_gamma() == 22
    assert p.get_epsilon() == 9
    assert p.get_power_consumption() == 198

