from enum import Enum


class ReindeerState(Enum):
    RESTING = 0
    MOVING = 1


class Reindeer:
    speed: int
    movement_period: int
    rest_period: int
    current_second: int
    total_distance_traveled: int
    current_state: ReindeerState
    next_state_starts_at: int
    points: int

    def __init__(self, name, speed, movement_period, rest_period):
        self.name = name
        self.speed = speed
        self.movement_period = movement_period
        self.rest_period = rest_period
        self.total_distance_traveled = 0
        self.current_state = ReindeerState.MOVING
        self.current_second = 0
        self.next_state_starts_at = movement_period
        self.points = 0

    def tick_second(self):
        self.determine_state()
        if self.current_state == ReindeerState.MOVING:
            self.total_distance_traveled += self.speed
        self.current_second += 1

    def determine_state(self):
        if self.current_second == self.next_state_starts_at:
            if self.current_state == ReindeerState.MOVING:
                self.current_state = ReindeerState.RESTING
                self.next_state_starts_at += self.rest_period
            else:
                self.current_state = ReindeerState.MOVING
                self.next_state_starts_at += self.movement_period

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.name} {self.total_distance_traveled} {self.points}"


def award_leaders(list_of_reindeer):
    furthest = -1
    for current_reindeer in list_of_reindeer:
        if furthest == -1:
            furthest = current_reindeer.total_distance_traveled
        else:
            if current_reindeer.total_distance_traveled > furthest:
                furthest = current_reindeer.total_distance_traveled
    for current_reindeer in list_of_reindeer:
        if current_reindeer.total_distance_traveled == furthest:
            current_reindeer.points += 1


if __name__ == "__main__":
    reindeers = [
        Reindeer("dancer", 27, 5, 132),
        Reindeer("cupid", 22, 2, 41),
        Reindeer("rudolph", 11, 5, 48),
        Reindeer("donner", 28, 5, 134),
        Reindeer("dasher", 4, 16, 55),
        Reindeer("blitzen", 14, 3, 38),
        Reindeer("prancer", 3, 21, 40),
        Reindeer("comet", 18, 6, 103),
        Reindeer("vixen", 18, 5, 84),

    ]
    for i in range(2503):
        for reindeer in reindeers:
            reindeer.tick_second()
        award_leaders(reindeers)
    for reindeer in reindeers:
        print(reindeer)
