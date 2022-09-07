import pytest

from y2021.day3.main_b import InputHandler, OutputHandler, PowerConsumption
from y2021.day3.data import test_input


def test_generate_oxy_ratings():
    i = InputHandler()
    i.handle_raw_input(test_input)
    p = PowerConsumption(i.elements)
    assert p.get_oxygen_generator_rating() == 23

def test_generate_co2_ratings():
    i = InputHandler()
    i.handle_raw_input(test_input)
    p = PowerConsumption(i.elements)
    assert p.get_co2_scrubber_rating() == 10

def test_get_both_ratings():
    i = InputHandler()
    i.handle_raw_input(test_input)
    p = PowerConsumption(i.elements)
    assert p.get_oxygen_generator_rating() == 23
    assert p.get_co2_scrubber_rating() == 10

def test_get_both_ratings_again():
    i = InputHandler()
    i.handle_raw_input(test_input)
    p = PowerConsumption(i.elements)
    assert p.get_co2_scrubber_rating() == 10
    assert p.get_oxygen_generator_rating() == 23

def test_get_life_support_rating():
    i = InputHandler()
    i.handle_raw_input(test_input)
    p = PowerConsumption(i.elements)
    assert p.get_life_support_rating() == 230

