from d==effects.base import Effect

from day22_parts.data import PRINT


class Shield(Effect):

    def __init__(self, caster, target):

        super().__init__("Shield", 6, caster, target)

    def go(self):

        if self.rounds_left == 0:
            if PRINT:
                print("Shield fades")
            self.target.defense -= 7
            self.rounds_left -= 1
            self.caster.check_effects()
        elif self.rounds_left == 6:
            if PRINT:
                print("Shield is active")
            self.target.defense += 7
        else:
            pass
            if PRINT:
                print(f"Shield is active {self.rounds_left} left")
        self.rounds_left -= 1
