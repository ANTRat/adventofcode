import re

data = open('day14.txt').read().split('\n')

reindeer = {}
points = {}
distances = {}

for line in data:
    r = re.search('(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds', line)
    if r:
        rg = r.groups()
        name = rg[0]
        if name not in points:
            points[name] = 0
        if name not in distances:
            distances[name] = 0
        speed = int(rg[1])
        dur = int(rg[2])
        wait = int(rg[3])
        reindeer[name] = [speed]*dur + [0]*wait

for second in range(2503):
    for name, rd in reindeer.items():
        distances[name] += rd[second % len(rd)]
    for n in distances:
        if distances[n] == max(distances.values()):
            points[n] += 1

print('part1', max(distances.values()))
print('part2', max(points.values()))
