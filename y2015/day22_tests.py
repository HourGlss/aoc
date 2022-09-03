from day22_parts.day22 import *


def test_creation():
    me = Fighter("Me", health=50, mana=500)
    boss = Fighter("Boss", health=55)
    assert me.health == 50
    assert me.mana == 500
    assert boss.health == 55


def test_boss_attack():
    me = Fighter("Me", health=50, mana=500)
    boss = Fighter("Boss", health=55)
    boss.attack = 8
    boss.hit(me)
    assert me.health == 50 - 8


def test_magic_missile():
    me = Fighter("Me", health=50, mana=500)
    boss = Fighter("Boss", health=55)
    me.magic_missile(boss)
    assert me.mana == 500 - SpellCost['MAGICMISSILE']
    assert boss.health == (55 - 4)


def test_drain():
    me = Fighter("Me", health=50, mana=500)
    boss = Fighter("Boss", health=55)
    me.drain(boss)
    assert me.mana == (500 - SpellCost['DRAIN'])
    assert boss.health == (55 - 2)
    assert me.health == 50 + 2


def test_shield():
    me = Fighter("Me", health=50, mana=500)
    boss = Fighter("Boss", health=55)
    boss.attack = 8
    me.shield(boss)  # shield does not "work on cast"
    assert me.mana == 500 - SpellCost['SHIELD']
    me.effects[0].build_output()  # shield will be active now
    boss.hit(me)
    assert me.health == (50 - boss.attack + me.defense)
    me.effects[0].build_output()
    me.check_effects()
    me.effects[0].build_output()
    me.check_effects()
    me.effects[0].build_output()
    me.check_effects()
    me.effects[0].build_output()
    me.check_effects()
    me.effects[0].build_output()
    me.check_effects()
    me.effects[0].build_output()
    me.check_effects()
    assert me.defense == 0


def test_poison():
    me = Fighter("Me", health=50, mana=500)
    boss = Fighter("Boss", health=55)
    me.poison(boss)
    assert me.mana == 500 - SpellCost['POISON']
    assert boss.health == 55
    me.effects[0].build_output()  # poison doesnt tick on first
    me.check_effects()
    me.effects[0].build_output()  # first tick of damage
    me.check_effects()
    assert boss.health == 52
    me.effects[0].build_output()  # second tick
    me.check_effects()
    me.effects[0].build_output()  # third tick
    me.check_effects()
    me.effects[0].build_output()  # fourth
    me.check_effects()
    me.effects[0].build_output()  # fifth
    me.check_effects()
    me.effects[0].build_output()  # sixth
    me.check_effects()
    assert boss.health == 55 - (3 * 6)
    assert len(me.effects) == 0


def test_recharge():
    me = Fighter("Me", health=50, mana=500)
    boss = Fighter("Boss", health=55)
    me.recharge(boss)
    assert me.mana == (500 - int(SpellCost['RECHARGE']))
    me.effects[0].build_output()  # first
    me.check_effects()
    ticks = 0
    assert me.mana == (500 - int(SpellCost['RECHARGE']))
    me.effects[0].build_output()  # second turn, first tick
    me.check_effects()
    ticks += 1
    assert me.mana == (500 - SpellCost['RECHARGE'] + (101 * ticks))
    me.effects[0].build_output()  # third turn, second tick
    me.check_effects()
    ticks += 1
    assert me.mana == (500 - SpellCost['RECHARGE'] + (101 * ticks))
    me.effects[0].build_output()  # 4 , 3
    me.check_effects()
    ticks += 1
    assert me.mana == (500 - SpellCost['RECHARGE'] + (101 * ticks))
    me.effects[0].build_output()  # 5 , 4
    me.check_effects()
    ticks += 1
    assert me.mana == (500 - SpellCost['RECHARGE'] + (101 * ticks))
    assert me.recharge(boss) == False
    me.effects[0].build_output()  # 6, 5
    me.check_effects()
    ticks += 1
    assert me.mana == (500 - SpellCost['RECHARGE'] + (101 * ticks))
    assert len(me.effects) == 0
    assert me.recharge(boss) == True




