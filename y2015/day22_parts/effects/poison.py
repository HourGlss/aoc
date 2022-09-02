from day22_parts.effects.base import Effect
from day22_parts.data import PRINT



class Poison(Effect):

    def __init__(self, caster, target):
        super().__init__("Poison", 5, caster, target)

    def go(self):
        if not self.cast_this_round:
            if PRINT:
                print(f"{self.target.name}({self.target.health})", end=" ")
            self.target.health -= 3
            if PRINT:
                print(f" psn tick ({self.target.health}) {self.rounds_left} left")
            self.rounds_left -= 1
            self.caster.check_effects()
        else:
            self.cast_this_round = False
