from y2016.day3.main_a import Triangle, InputHandler,OutputHandler
from y2016.day3.data import test_input
def test_create_triangle():
    t = Triangle("3 4 5")
    assert t.sides == [3,4,5]

def test_real_triangle():
    t = Triangle("3 4 5")
    assert t.is_possible() == True

def test_fake_triangle():
    t = Triangle("5 10 25")
    assert t.is_possible() == False

def test_input_handler():
    i = InputHandler()
    i.handle_raw_input(test_input)
    o = OutputHandler(i)
    o.build_output()
    assert o.get_output() == 1


