input_data = open('day16.txt').read()

wanted = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


def solve(part2=False):
    for l in input_data.split('\n'):
        a = l.split(': ', 1)
        sue = a[0]
        count = 0
        traits = a[1].split(', ')
        for b in traits:
            trait, num = b.split(': ')
            num = int(num)
            if part2:
                if trait in ['cats', 'trees'] and wanted[trait] < num:
                    count += 1
                elif trait in ['pomeranians', 'goldfish'] and wanted[trait] > num:
                    count += 1
                elif trait not in ['pomeranians', 'goldfish', 'cats', 'trees'] and wanted[trait] == num:
                    count += 1
            else:
                if wanted[trait] == num:
                    count += 1
        if count == 3:
            return sue


print('part1', solve())
print('part2', solve(True))
