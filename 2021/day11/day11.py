def main():
    data = load_data()
    print("Part One:", part_one(data))
    print("Part Two:", part_two(data))

def load_data():
    with open('input') as data:
        return [list(map(int, line.strip())) for line in data]

def one_step(data, xmax, ymax):
    def gen_adjacent(x, y):
        for ax in (x-1, x, x+1):
            if 0 <= ax < xmax:
                for ay in (y-1, y, y+1):
                    if (0 <= ay < ymax) and not (ax==x and ay==y):
                        yield ax,ay
    def check_flash(x, y):
        if data[y][x] > 9 and (x, y) not in flashed:
            flashed.add((x, y))
            for ax,ay in gen_adjacent(x, y):
                data[ay][ax] += 1
                check_flash(ax, ay)
    flashed = set()
    for x in range(xmax):
        for y in range(ymax):
            data[y][x] += 1
    for x in range(xmax):
        for y in range(ymax):
            check_flash(x, y)
    for x,y in flashed:
        data[y][x] = 0
    return len(flashed)

def part_one(data):
    data = [[x for x in row] for row in data]
    xmax, ymax = len(data[0]), len(data)
    return sum(one_step(data, xmax, ymax) for _ in range(100))

def part_two(data):
    xmax, ymax = len(data[0]), len(data)
    steps = 1
    while one_step(data, xmax, ymax) != xmax*ymax:
        steps += 1
    return steps

if __name__ == "__main__":
    main()
