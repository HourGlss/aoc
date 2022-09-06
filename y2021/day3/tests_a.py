import pytest

from y2021.day3.main_a import InputHandler, OutputHandler, PowerConsumption
from y2021.day3.data import test_input


def test_gamma_and_epsilon():
    p = PowerConsumption()
    i = InputHandler()
    i.handle_raw_input(test_input)
    o = OutputHandler(i, p)
    assert p.gamma == 22
    assert p.epsilon == 9
    assert o.get_output() == 198
