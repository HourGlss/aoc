from effects.base import Effect
from effects.recharge import Recharge
from effects.shield import Shield
from effects.poison import Poison
from data import PRINT, SpellCost


class Fighter:
    health: int
    mana: int
    name: str
    defense: int
    attack: int
    total_mana_cost: int
    effects: list["Effect"]
    skill_list: list

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
        self.skill_list = []

    def hit(self, other: "Fighter"):
        damage = self.attack - other.defense
        if damage < 1:
            damage = 1
        display = ""
        if PRINT:
            display += "BEFORE\n"
            display += f"\tself {self.health}hp {self.attack}atk\n"
            display += f"\tother {other.health}hp {other.defense}def\n"
        other.health -= damage
        if PRINT:
            display += "AFTER\n"
            display += f"\tself {self.health}hp {self.attack}atk\n"
            display += f"\tother {other.health}hp {other.defense}def\n"
            print(display)

    def next(self, other: "Fighter"):
        if self.mana > SpellCost['MAGICMISSILE'] and other.health <= 4:
            self.magic_missile(other)
            return

        poison_active, shield_active, recharge_active = self.check_effects_active()
        if SpellCost['RECHARGE'] <= self.mana < self.mana_recharge:
            if not recharge_active:
                self.recharge(other)
                return
        if self.mana > SpellCost['DRAIN']:
            if self.health <= self.drain_health:
                self.drain(other)
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

    # def next(self, other: "Fighter"):
    #     current_spell, name_of_spell = self.skill_list.pop(0)
    #     if current_spell is not None:
    #         if self.mana >= SpellCost[name_of_spell]:
    #             current_spell(self, other)
    #             return
    #     self.health = 0
    #     # print(f"len {len(self.skill_list)} mana {self.mana} but need {SpellCost[name_of_spell]}")
    #     return

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
        for effect in self.effects:
            if effect.name == "Poison":
                return False
        self.track_and_remove_mana("POISON")
        self.effects.append(Poison(self, other))
        return True

    def shield(self, other: "Fighter"):

        for effect in self.effects:
            if effect.name == "Shield":
                return False
        self.track_and_remove_mana("SHIELD")
        self.effects.append(Shield(self, self))
        return True

    def recharge(self, other: "Fighter"):

        for effect in self.effects:
            if effect.name == "Recharge":
                return False
        self.track_and_remove_mana("RECHARGE")
        self.effects.append(Recharge(self, self))
        return True

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
