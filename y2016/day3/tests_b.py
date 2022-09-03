from y2016.day3.main_b import Triangle, InputHandler,OutputHandler
from y2016.day3.data import test_input

def test_input_handler():
    i = InputHandler()
    i.handle_raw_input(test_input)
    o = OutputHandler(i)
    o.build_output()
    assert o.get_output() == 2


