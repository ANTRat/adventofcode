import re

d = open('day15.txt').read()
s = '(\w+): capacity ([\d\-]+), durability ([\d\-]+), flavor ([\d\-]+), texture ([\d\-]+), calories ([\d\-]+)'
ingredients = {}
for l in d.split('\n'):
    reg = re.search(s, l)
    if reg:
        g = reg.groups()
        ingredients[g[0]] = {
            'capacity': int(g[1]),
            'durability': int(g[2]),
            'flavor': int(g[3]),
            'texture': int(g[4]),
            'calories': int(g[5])
        }


def score(nums, part2=False):
    caps = []
    durs = []
    flas = []
    texs = []
    cals = []
    for name in nums:
        caps.append(ingredients[name]['capacity'] * nums[name])
        durs.append(ingredients[name]['durability'] * nums[name])
        flas.append(ingredients[name]['flavor'] * nums[name])
        texs.append(ingredients[name]['texture'] * nums[name])
        cals.append(ingredients[name]['calories'] * nums[name])
    caps = max(0, sum(caps))
    durs = max(0, sum(durs))
    flas = max(0, sum(flas))
    texs = max(0, sum(texs))
    if part2:
        if sum(cals) != 500:
            return 0
    return caps * durs * flas * texs


max1 = 0
max2 = 0
for a in range(101):
    for b in range(101):
        for c in range(101):
            for d in range(101):
                if a + b + c + d == 100:
                    t = {'Frosting': a, 'Candy': b, 'Butterscotch': c, 'Sugar': d}
                    max1 = max(max1, score(t))
                    max2 = max(max2, score(t, part2=True))
print('part1', max1)
print('part2', max2)
