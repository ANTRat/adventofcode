import re

boss = {'hp': 103, 'd': 9, 'a': 2}

weapons_text = """
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0
"""
armor_text = """
Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
"""
rings_text = """
Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""


def fight(my_stats, boss_stats, dump=False):
    turns = 0
    while my_stats['hp'] > 0 and boss_stats['hp'] > 0:
        turns += 1
        if turns % 2 == 1:
            if dump:
                print('my turn')
            boss_stats['hp'] -= my_stats['d'] - boss_stats['a']
        else:
            if dump:
                print('boss turn')
            my_stats['hp'] -= boss_stats['d'] - my_stats['a']
    if dump:
        print(my_stats, boss_stats)
    if my_stats['hp'] > 0:
        return True
    else:
        return False


reg = '^(\w+|\w+ \+\d)\s+(\d+)\s+(\d+)\s+(\d+)'
weapons = {}
for a in re.findall(reg, weapons_text, re.MULTILINE):
    weapons[a[0]] = {'c': int(a[1]), 'd': int(a[2]), 'a': int(a[3])}
armors = {'None': {'c': 0, 'd': 0, 'a': 0}}
for a in re.findall(reg, armor_text, re.MULTILINE):
    armors[a[0]] = {'c': int(a[1]), 'd': int(a[2]), 'a': int(a[3])}
rings = {'None': {'c': 0, 'd': 0, 'a': 0}}
for a in re.findall(reg, rings_text, re.MULTILINE):
    rings[a[0]] = {'c': int(a[1]), 'd': int(a[2]), 'a': int(a[3])}

wins = []
losses = []
for r1 in rings:
    for r2 in rings:
        if r2 != 'None' and r1 != r2:
            for w in weapons:
                for a in armors:
                    tc = weapons[w]['c'] + armors[a]['c'] + rings[r1]['c'] + rings[r2]['c']
                    td = weapons[w]['d'] + armors[a]['d'] + rings[r1]['d'] + rings[r2]['d']
                    ta = weapons[w]['a'] + armors[a]['a'] + rings[r1]['a'] + rings[r2]['a']
                    me = {'hp': 100, 'd': td, 'a': ta}
                    if fight(dict(me), dict(boss)):
                        wins.append(tc)
                    else:
                        losses.append(tc)

print('part1', min(wins))
print('part2', max(losses))
