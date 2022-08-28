from enum import Enum

SpellCost = {
    "MAGICMISSILE": 53,
    "DRAIN": 73,
    "SHIELD": 113,
    "POISON": 173,
    "RECHARGE": 229
}


class Fighter:
    health: int
    mana: int
    name: str
    defense: int
    attack: int
    total_mana_cost: int
    effects: list["Effect"]

    def __init__(self,
                 name,
                 health: int = 100,
                 mana: int = 0,
                 drain_health: int = 14,
                 mana_recharge: int = 400,
                 shield_health: int = 20,
                 poison_boss_health: int = 8
                 ):
        self.name = name
        self.health = health
        self.mana = mana
        self.defense = 0
        self.attack = 0
        self.effects = []
        self.total_mana_cost = 0
        self.drain_health = drain_health
        self.mana_recharge = mana_recharge
        self.shield_health = shield_health
        self.poison_boss_health = poison_boss_health

    def hit(self, other: "Fighter"):
        damage = self.attack - other.defense
        if damage < 1:
            damage = 1
        other.health -= damage
        if PRINT:
            print(f"{self.name}({self.health}) hits for {self.attack}-{other.defense} = {damage} damage. ({other.health})")

    def next(self, other: "Fighter"):
        poison_active, shield_active, recharge_active = self.check_effects_active()
        if self.mana > SpellCost['MAGICMISSILE'] and other.health <= 4:
            self.magic_missile(other)
            return
        if self.mana > SpellCost['DRAIN']:
            if self.health <= self.drain_health:
                self.drain(other)
                return
        if SpellCost['RECHARGE'] <= self.mana < self.mana_recharge:
            if not recharge_active:
                self.recharge(other)
                return
        if self.mana > SpellCost['SHIELD'] and self.health < self.shield_health:
            if not shield_active:
                self.shield(other)
                return
        if other.health >= self.poison_boss_health:
            if self.mana > SpellCost['POISON']:
                if not poison_active:
                    self.poison(other)
                    return

        if self.mana > SpellCost['MAGICMISSILE']:
            self.magic_missile(other)
            return
        if PRINT:
            print("Player has no mana")
        self.health = 0
        return

    def check_effects_active(self):
        poison_active = False
        shield_active = False
        recharge_active = False
        for e in self.effects:
            if e.name == "Poison":
                poison_active = True
            if e.name == "Shield":
                shield_active = True
            if e.name == "Recharge":
                recharge_active = True
        return poison_active, shield_active, recharge_active

    def track_and_remove_mana(self, name_of_spell: str):
        cost = SpellCost[name_of_spell]
        self.mana -= cost
        self.total_mana_cost += cost

    def magic_missile(self, other: "Fighter"):
        self.track_and_remove_mana("MAGICMISSILE")
        damage = 4
        other.health -= damage
        if PRINT:
            print(f"{self.name}({self.health}) casts MM {damage} damage. ({other.health})")

    def drain(self, other: "Fighter"):
        self.track_and_remove_mana("DRAIN")
        damage = 2
        heal = 2
        other.health -= damage
        self.health += heal
        if PRINT:
            print(f"{self.name}({self.health}) casts drain {damage} damage. ({other.health})")

    def poison(self, other: "Fighter"):
        self.track_and_remove_mana("POISON")
        for effect in self.effects:
            if effect.name == "Poison":
                return
        self.effects.append(Poison(self,other))

    def shield(self, other: "Fighter"):
        self.track_and_remove_mana("SHIELD")

        for effect in self.effects:
            if effect.name == "Shield":
                return
        self.effects.append(Shield(self,self))

    def recharge(self, other: "Fighter"):

        self.track_and_remove_mana("RECHARGE")

        for effect in self.effects:
            if effect.name == "Recharge":
                return
        self.effects.append(Recharge(self,self))

    def __repr__(self):
        return str(self)

    def __str__(self):
        ret_string = f"{self.name} ({self.health}/{self.mana})"
        poison_active, shield_active, recharge_active = self.check_effects_active()
        if poison_active:
            ret_string += " P"
        if shield_active:
            ret_string += " S"
        if recharge_active:
            ret_string += " R"
        return ret_string

    def check_effects(self):
        to_remove = []
        for effect in self.effects:
            if effect.rounds_left == -1:
                to_remove.append(effect)
        for effect in to_remove:
            if PRINT:
                print(f"REMOVING {effect.name}")
            self.effects.remove(effect)


class Effect:
    rounds_left: int
    name: str
    target: Fighter
    cast_this_round: bool
    caster : Fighter

    def __init__(self, name: str, rounds: int, caster: Fighter, target: Fighter):
        self.name = name
        self.rounds_left = rounds
        self.caster = caster
        self.target = target
        self.cast_this_round = True
        if PRINT:
            print(f"CAST {self.name}")

    def go(self):
        ...


class Shield(Effect):

    def __init__(self, caster: Fighter, target: Fighter):

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


class Poison(Effect):

    def __init__(self, caster: Fighter, target: Fighter):
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


class Recharge(Effect):

    def __init__(self, caster: Fighter, target: Fighter):

        super().__init__("Recharge", 5, caster, target)

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


def is_fight_done(fighters):
    for f in fighters:
        if f.health <= 0:
            return f
    return None


def print_fighters(fighters):
    for fighter in fighters:
        print(fighter)


def fight(fighters: tuple):
    fighter1, fighter2 = fighters
    if PRINT:
        print("-- Player turn --")
        print_fighters(fighters)
    fighter1.next(fighter2)
    dead_fighter = is_fight_done(fighters)
    if dead_fighter is not None:
        if dead_fighter.name != "Me":
            return False
        else:
            return True
    for effect in fighter1.effects:
        effect.go()
    dead_fighter = is_fight_done(fighters)
    if dead_fighter is not None:
        if dead_fighter.name != "Me":
            return False
        else:
            return True
    if PRINT:
        print("-- Boss turn --")
        print_fighters(fighters)
    for effect in fighter1.effects:
        effect.go()
    dead_fighter = is_fight_done(fighters)
    if dead_fighter is not None:
        if dead_fighter.name != "Me":
            return False
        else:
            return True
    fighter2.hit(fighter1)

    dead_fighter = is_fight_done(fighters)
    if dead_fighter is not None:
        if dead_fighter.name != "Me":
            return False
        else:
            return True
    return fight((fighter1, fighter2))


def play_fair_round(a, b, c, d):
    me = Fighter("Me", health=50, mana=500,
                 drain_health=a,
                 mana_recharge=b,
                 shield_health=c,
                 poison_boss_health=d)
    boss = Fighter("Boss", health=55)
    boss.attack = 8
    lose = fight((me, boss))
    return lose, me.total_mana_cost

PRINT = False
if __name__ == "__main__":
    #
    # drain_health: int = 14,
    # mana_recharge: int = 400,
    # shield_health: int = 20,
    # poison_boss_health: int = 8
    # print(play_fair_round(1, 275, 3, 0))
    cheapest = 4000
    for a in range(0,30):
        for b in range(SpellCost['RECHARGE'],500):
            for c in range(0,50):
                for d in range(0,50):

                    lost, cost = play_fair_round(a, b, c, d)
                    if not lost:
                        if cost < cheapest:
                            cheapest = cost
                            print(cost,a,b,c,d)
