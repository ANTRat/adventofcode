input_data = open('day18.txt').read()
grid = {}
initial = 0
for x, line in enumerate(input_data.split('\n')):
    grid[x] = {}
    for y, data in enumerate(line):
        if data == '#':
            initial += 1
            state = True
        else:
            state = False
        grid[x][y] = state
ogrid = grid


def count(countgrid):
    c = 0
    for x in countgrid:
        for y in countgrid[x]:
            if countgrid[x][y] == True:
                c += 1
    return c


def neigh(g, x, y):
    on = 0
    for nx in [x - 1, x, x + 1]:
        for ny in [y - 1, y, y + 1]:
            try:
                if grid[nx][ny]:
                    if (x, y) != (nx, ny):
                        on += 1
            except KeyError:
                pass
    # print(x,y,on)
    return on


def animate(part2=False):
    global grid
    oldgrid = grid
    if part2:
        oldgrid[0][0] = True
        oldgrid[max(grid.keys())][max(grid.keys())] = True
        oldgrid[0][max(grid.keys())] = True
        oldgrid[max(grid.keys())][0] = True
    ng = {}
    for x in oldgrid:
        ng[x] = {}
        for y in oldgrid[x]:
            if oldgrid[x][y]:
                if neigh(oldgrid, x, y) in [2, 3]:
                    ng[x][y] = True
                else:
                    ng[x][y] = False
            else:
                if neigh(oldgrid, x, y) == 3:
                    ng[x][y] = True
                else:
                    ng[x][y] = False
    if part2:
        ng[0][0] = True
        ng[max(ng.keys())][max(ng.keys())] = True
        ng[0][max(ng.keys())] = True
        ng[max(ng.keys())][0] = True
    grid = ng


def printgrid(g):
    s = ''
    for x in g:
        xs = ''
        for y in g[x]:
            if g[x][y] == True:
                xs = xs + '#'
            else:
                xs = xs + '.'
        s += xs + "\n"
    return s


for a in range(100):
    animate()
print('part1', count(grid))

grid = ogrid
for b in range(100):
    animate(True)
print('part2', count(grid))
