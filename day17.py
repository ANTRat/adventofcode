import itertools

containers = list(map(int, open('day17.txt').read().split('\n')))

counts = {}
for r in range(len(containers)):
    for a in itertools.combinations(containers, r):
        if sum(a) == 150:
            if r not in counts:
                counts[r] = 0
            counts[r] += 1

print('part1', sum(counts.values()))
print('part2', counts[min(counts)])
