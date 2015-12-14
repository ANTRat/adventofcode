import re

data = open('day14.txt').read().split('\n')

points = {}
distances = {}

for second in range(2503):
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
            moving = []
            for a in range(dur):
                moving.append(True)
            for b in range(wait):
                moving.append(False)
            if moving[second % len(moving)]:
                distances[name] += speed
    for n in distances:
        if distances[n] == max(distances.values()):
            points[n] += 1

print('part1', max(distances.values()))
print('part2', max(points.values()))