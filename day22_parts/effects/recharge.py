from day22_parts.effects.base import Effect
from day22_parts.data import PRINT




class Recharge(Effect):

    def __init__(self, caster, target):

        super().__init__("Recharge", 4, caster, target)

    def go(self):
        if not self.cast_this_round:
            if PRINT:
                print(f"{self.target.name}({self.target.mana})", end=" ")
            self.target.mana += 101
            if PRINT:
                print(f" recharge tick ({self.target.mana}) {self.rounds_left} rounds left")
            self.rounds_left -= 1
            self.caster.check_effects()

        else:
            self.cast_this_round = False
