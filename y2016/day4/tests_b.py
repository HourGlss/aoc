from y2016.day4.main_b import Room, InputHandler, OutputHandler
from y2016.day4.data import test_input

def test_decrypt_room_name():
    data = "qzmt-zixmtkozy-ivhz-343[zimth]"
    r = Room(data)
    r.decrypt_name()
    assert r.decrypted_name == "very encrypted name"

