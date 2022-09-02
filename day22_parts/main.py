from fighter import Fighter
from data import PRINT


def is_fight_done(fighters: tuple[Fighter, Fighter]) -> Fighter | None:
    for f in fighters:
        if f.health <= 0:
            return f
    return None


def print_fighters(fighters: tuple[Fighter, Fighter]) -> None:
    for fighter in fighters:
        print(fighter)


def fight(fighters: tuple[Fighter, Fighter]) -> bool:
    fighter1, fighter2 = fighters
    if PRINT:
        print("-- Player turn --")
        print_fighters(fighters)
    fighter1.health -= 1
    fighter1.next(fighter2)
    dead_fighter = is_fight_done(fighters)
    if dead_fighter is not None:
        if dead_fighter.name == "Me":
            return True
        else:
            return False
    for effect in fighter1.effects:
        effect.go()
    dead_fighter = is_fight_done(fighters)
    if dead_fighter is not None:
        if dead_fighter.name == "Me":
            return True
        else:
            return False
    if PRINT:
        print("-- Boss turn --")
        print_fighters(fighters)
    for effect in fighter1.effects:
        effect.go()
    dead_fighter = is_fight_done(fighters)
    if dead_fighter is not None:
        if dead_fighter.name == "Me":
            return True
        else:
            return False
    fighter2.hit(fighter1)

    dead_fighter = is_fight_done(fighters)
    if dead_fighter is not None:
        if dead_fighter.name == "Me":
            return True
        else:
            return False
    return fight((fighter1, fighter2))


def play_fair_round(_skill_list: list[tuple] = None, params_dict: dict = None):
    if params_dict is not None:
        _drain_health = params_dict['drain_health']
        _mana_recharge = params_dict['mana_recharge']
        _shield_health = params_dict['shield_health']
        _poison_boss_health = params_dict['poison_boss_health']
        me = Fighter("Me", health=50, mana=500,
                     drain_health=_drain_health,
                     mana_recharge=_mana_recharge,
                     shield_health=_shield_health,
                     poison_boss_health=_poison_boss_health)
    else:
        me = Fighter("Me", health=50, mana=500)
    boss = Fighter("Boss", health=55)
    boss.attack = 8
    if _skill_list is not None:
        me.skill_list = _skill_list
    lose = fight((me, boss))
    return lose, me.total_mana_cost, me, boss


def build_list(n: int) -> list[tuple]:
    import random
    skill_list_by_name = []
    last_cast = {
        "SHIELD": -1,
        "RECHARGE": 0,
        "POISON": -1
    }
    skill_list_by_name.append("RECHARGE")
    for _i in range(n):
        allowable = ["MAGICMISSILE", "DRAIN"]
        if last_cast['SHIELD'] == -1 or last_cast['SHIELD'] + 8 <= _i:
            allowable.append("SHIELD")
        if last_cast['POISON'] == -1 or last_cast['POISON'] + 8 <= _i:
            allowable.append("POISON")
        if last_cast['RECHARGE'] + 7 <= _i:
            allowable.append("RECHARGE")
        next_spell = random.choice(allowable)
        try:
            last_cast[next_spell] = _i
        except KeyError:
            pass
        skill_list_by_name.append(next_spell)
    skills = {
        "SHIELD": Fighter.shield,
        "RECHARGE": Fighter.recharge,
        "POISON": Fighter.poison,
        "MAGICMISSILE": Fighter.magic_missile,
        "DRAIN": Fighter.drain
    }
    _skill_list = []

    for _s in skill_list_by_name:
        _skill_list.append((skills[_s], _s))
    return _skill_list
#
#
#
# if __name__ == "__main__":
#     # cheapest = 5000
#     # # print(len(skill_list))
#     # while True:
#     #     # print(i)
#     #     _ = build_list(25)
#     #     lost, cost = play_fair_round(list(_))
#     #     if not lost:
#     #         print("WIN")
#     #         if cost < cheapest:
#     #             cheapest = cost
#     #             print(cost)
#     #     else:
#     #         pass
#     #         # print("LOSS")
#     cheapest = 4000
#     import time
#     start_time = time.time()
#     for a in range(0, 52):
#         for b in range(150, 700):
#             for c in range(0, 52):
#                 for d in range(0, 55):
#                     params = {
#                         "drain_health": a,
#                         "mana_recharge": b,
#                         "shield_health": c,
#                         "poison_boss_health": d
#                     }
#                     lost, cost,me,boss = play_fair_round(params_dict=params)
#
#                     if not lost:
#                         if cost < cheapest:
#                             cheapest = cost
#                             print(cost)
#                     else:
#                         # print(f"{me.health}/{me.mana} {boss.health}")
#                         pass
#                         # print("LOSS")
#     end_time = time.time()
#
#     print("Done, hope you found a solution that was lower than 1362")
#     print(f"took {end_time - start_time} seconds to run tests")
#
