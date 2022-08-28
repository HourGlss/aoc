from enum import Enum
from itertools import combinations


class ItemSlot(Enum):
    WEAPON = 0
    ARMOR = 1
    RING = 2


class Item:
    attack: int
    armor: int
    cost: int
    name: str
    slot: ItemSlot

    def __init__(self, name: str, cost: int, attack: int, armor: int, slot: ItemSlot):
        self.name = name
        self.slot = slot
        self.attack = attack
        self.armor = armor
        self.cost = cost

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self.name:<10}\t{self.cost:>3}\t{self.attack:>2}\t{self.armor:>2}"


class Fighter:
    defense: int
    attack: int
    health: int


    armor: Item | None
    weapon: Item | None
    rings: list[Item | None]
    name: str

    def __init__(self, name):
        self.name = name
        self.rings = [None, None]
        self.armor = None
        self.weapon = None
        self.health = 100
        self.attack = 0
        self.defense = 0

    def hit(self, other: "Fighter"):
        damage = self.attack - other.defense
        if damage < 1:
            damage = 1
        other.health -= damage
        # print(f"{self.name}({self.health}) deals {self.attack}-{other.defense} = {damage} damage. ({other.health})")

    def add_stats_from_item(self, item: Item):
        self.attack += item.attack
        self.defense += item.armor
        # print(f"a{self.attack} d{self.defense}")

    def remove_stats_from_item(self, item: Item):
        self.attack -= item.attack
        self.defense -= item.armor

    def can_equip_ring_without_removing(self):
        for _ in self.rings:
            if _ is None:
                return True
        return False

    def equip(self, item: Item, slot: int = -1):
        # print(f"Equipping {item}")
        if item is None:
            return
        if item.slot == ItemSlot.WEAPON:
            if self.weapon is not None:
                self.remove_stats_from_item(self.weapon)
            self.weapon = item
        if item.slot == ItemSlot.ARMOR:
            if self.armor is not None:
                self.remove_stats_from_item(self.armor)
            self.armor = item
        if item.slot == ItemSlot.RING:
            if self.can_equip_ring_without_removing():
                for i, r in enumerate(self.rings):
                    if r is None:
                        self.rings[i] = item
                        break
            else:
                if 0 <= slot <= 1:
                    if self.rings[slot] is not None:
                        self.remove_stats_from_item(self.rings[slot])
                        self.rings[slot] = item
                else:
                    raise RuntimeError("Tried to equip a ring when two rings are already equipped, but no slot given")
        self.add_stats_from_item(item)


def build_items():
    weapons = [
        # Weapons:    Cost  Damage  Armor
        Item("Dagger", 8, 4, 0, ItemSlot.WEAPON),
        # Dagger        8     4       0
        Item("Shortsword", 10, 5, 0, ItemSlot.WEAPON),
        # Shortsword   10     5       0
        Item("Warhammer", 25, 6, 0, ItemSlot.WEAPON),
        # Warhammer    25     6       0
        Item("Longsword", 40, 7, 0, ItemSlot.WEAPON),
        # Longsword    40     7       0
        Item("Greataxe", 74, 8, 0, ItemSlot.WEAPON),
        # Greataxe     74     8       0
    ]
    armors = [
        # Armor:      Cost  Damage  Armor
        Item("Leather", 13, 0, 1, ItemSlot.ARMOR),
        # Leather      13     0       1
        Item("Chainmail", 31, 0, 2, ItemSlot.ARMOR),
        # Chainmail    31     0       2
        Item("Splintmail", 53, 0, 3, ItemSlot.ARMOR),
        # Splintmail   53     0       3
        Item("Bandedmail", 75, 0, 4, ItemSlot.ARMOR),
        # Bandedmail   75     0       4
        Item("Platemail", 102, 0, 5, ItemSlot.ARMOR),
        # Platemail   102     0       5
        None,
    ]
    rings = [
        # Rings:      Cost  Damage  Armor
        Item("Damage +1", 25, 1, 0, ItemSlot.RING),
        # Damage +1    25     1       0
        Item("Damage +2", 50, 2, 0, ItemSlot.RING),
        # Damage +2    50     2       0
        Item("Damage +3", 100, 3, 0, ItemSlot.RING),
        # Damage +3   100     3       0
        Item("Defense +1", 20, 0, 1, ItemSlot.RING),
        # Defense +1   20     0       1
        Item("Defense +2", 40, 0, 2, ItemSlot.RING),
        # Defense +2   40     0       2
        Item("Defense +3", 80, 0, 3, ItemSlot.RING),
        # Defense +3   80     0       3
        None,
        None
    ]
    return weapons, armors, rings


def is_fight_done(fighters):
    for f in fighters:
        if f.health <= 0:
            return f
    return None


def fight(fighter1: Fighter, fighter2: Fighter):
    fighter1.hit(fighter2)
    dead_fighter = is_fight_done([fighter1, fighter2])
    if dead_fighter is not None:
        # print(dead_fighter.name)
        if dead_fighter.name != "Me":
            return True
        else:
            return False
    fighter2.hit(fighter1)
    dead_fighter = is_fight_done([fighter1, fighter2])
    if dead_fighter is not None:
        if dead_fighter.name != "Me":
            # print(dead_fighter.name)

            return True
        else:
            return False
    return fight(fighter2, fighter1)


def get_cost_of_gear(gear_list: list[Item]) -> int:
    total = 0
    for g in gear_list:
        if g is not None:
            total += g.cost
    return total


def play_fair_round(gear):
    me = Fighter("Me")
    for g in gear:
        me.equip(g)
    cost = get_cost_of_gear(gear)
    me.health = 100
    boss = Fighter("Boss")
    boss.health = 103
    boss.attack = 9
    boss.defense = 2
    _win = fight(me, boss)
    return _win, cost


def part1():
    weps, arms, rins = build_items()
    ring_combos = list(combinations(rins, 2))
    cheapest = 1000
    for ring_combo in ring_combos:
        for iw, w in enumerate(weps):
            for ia, a in enumerate(arms):
                gear = []
                gear += ring_combo
                gear.append(w)
                gear.append(a)
                win, cost = play_fair_round(gear)
                if win:
                    if cost < cheapest:
                        cheapest = cost
    return cheapest

def part2():
    weps, arms, rins = build_items()
    ring_combos = list(combinations(rins, 2))
    most_expensive = 0
    for ring_combo in ring_combos:
        for iw, w in enumerate(weps):
            for ia, a in enumerate(arms):
                gear = []
                gear += ring_combo
                gear.append(w)
                gear.append(a)
                win, cost = play_fair_round(gear)
                if not win:
                    if cost > most_expensive:
                        most_expensive = cost
    return most_expensive


if __name__ == "__main__":
    print(part2())

