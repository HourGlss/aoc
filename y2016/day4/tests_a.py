from y2016.day4.main_a import Room, InputHandler, OutputHandler
from y2016.day4.data import test_input


def test_build_room():
    data = "not-a-real-room-404[oarel]"
    r = Room(data)
    assert r.given_checksum == "oarel"
    assert r.get_built_checksum() == "oarel"
    assert r.is_real()

def test_input_handler():
    i = InputHandler()
    i.handle_raw_input(test_input)
    assert i.rooms[0].is_real()
    assert i.rooms[1].is_real()
    assert i.rooms[2].is_real()
    assert not i.rooms[3].is_real()

def test_sector_id():
    data = "not-a-real-room-404[oarel]"
    r = Room(data)
    assert r.get_sector_id() == 404

def test_output_handler():
    i = InputHandler()
    i.handle_raw_input(test_input)
    o = OutputHandler(i)
    assert o.get_output() == 1514


