from itemslot import ItemSlot


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
