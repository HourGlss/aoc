from y2016.day6.main_a import PasswordBuilder
from y2016.day6.data import test_input

# def test_extract_character():
#     data = ['e', 'd', 'e', 'r', 'a', 't', 's', 'r', 'n', 'n', 's', 't', 'v', 'v', 'd', 'e']
#     p = PasswordBuilder(" ")
#     assert p.get_highest_occurance_char_in_list(data) == 'e'


def test_password_builder():
    p = PasswordBuilder(test_input)
    assert p.password == "easter"




