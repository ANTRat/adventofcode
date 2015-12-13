import itertools
import re


def solve(part2=False):
    people = {}
    for line in open('day13.txt'):
        reg = re.search('(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+).', line)
        if reg:
            groups = reg.groups()
            if groups[0] not in people:
                people[groups[0]] = {}
            if groups[1] == 'gain':
                mul = 1
            else:
                mul = -1
            people[groups[0]][groups[3]] = int(groups[2]) * mul

    if part2:
        people['me'] = {}
        for name in people.keys():
            people[name]['me'] = 0
            people['me'][name] = 0

    max_change = 0
    for seats in itertools.permutations(people.keys(), len(people.keys())):
        change = 0
        for i in range(len(people.keys())):
            left = seats[(i - 1) % len(people.keys())]
            person = seats[i]
            right = seats[(i + 1) % len(people.keys())]
            change += people[person][left]
            change += people[person][right]
        max_change = max(change, max_change)
    return max_change


print('part1', solve())
print('part2', solve(True))
