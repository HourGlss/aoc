from item import Item
from itemslot import ItemSlot


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
