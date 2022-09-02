from day14 import *


def test_reindeer_creation():
    r = Reindeer("",0, 0, 0)
    assert isinstance(r, Reindeer)

def test_movement():
    comet = Reindeer("comet",14, 10, 127)
    comet.tick_second()
    assert comet.total_distance_traveled == 14

    for i in range(9):
        comet.tick_second()
    assert comet.total_distance_traveled == 140
    comet.tick_second()
    comet.tick_second()
    assert comet.current_state == ReindeerState.RESTING

    while comet.current_second < 1000:
        comet.tick_second()
    assert comet.total_distance_traveled == 1120
