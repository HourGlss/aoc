import pytest

from y2022.day7.main_a import InputHandler,OutputHandler,Commands
from y2022.day7.data import test_input


def test_pwd_change_up_one_layer():
    pwd = "/home/azbai/run/"
    c = Commands()
    pwd = c.change_directory(pwd,"..")
    assert pwd == '/home/azbai/'

