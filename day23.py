input = open('day23.txt').read().strip().split('\n')


def run(asm, day2=False):
    reg = dict(a=0, b=0)
    if day2:
        reg['a'] = 1
    n = 0
    while True:
        i, d = asm[n].split(' ', 1)
        if i == 'inc':
            reg[d] += 1
            n += 1
        elif i == 'hlf':
            reg[d] = int(reg[d] / 2)
            n += 1
        elif i == 'tpl':
            reg[d] *= 3
            n += 1
        elif i == 'jmp':
            n += int(d)
        elif i == 'jio':
            cr, j = d.split(', ')
            if reg[cr] == 1:
                n += int(j)
            else:
                n += 1
        elif i == 'jie':
            cr, j = d.split(', ')
            if reg[cr] % 2 == 0:
                n += int(j)
            else:
                n += 1
        else:
            print('bad instr: ' + i)
            break
        if n >= len(asm):
            break
    return reg


print('part1', run(input)['b'])
print('part2', run(input, True)['b'])
