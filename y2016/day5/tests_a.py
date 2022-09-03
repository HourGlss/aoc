from y2016.day5.main_a import PasswordBuilder
from y2016.day5.data import test_input


def test_password_builder():
    data = test_input
    p = PasswordBuilder(data)
    assert p.password == "18f47a30"




