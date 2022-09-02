from day22_parts.data import PRINT


class Effect:
    rounds_left: int
    name: str
    cast_this_round: bool

    def __init__(self, name: str, rounds: int, caster, target):
        self.name = name
        self.rounds_left = rounds
        self.caster = caster
        self.target = target
        self.cast_this_round = True
        if PRINT:
            print(f"CAST {self.name}")

    def go(self):
        ...
