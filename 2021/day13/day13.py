def main():
    dots,lines = load_data()
    print("Part One:", part_one(dots, lines))
    print("Part Two:")
    for row in part_two(dots, lines):
        print(row)

def load_data():
    with open('input') as data:
        dots = set()
        for line in data:
            if line.isspace():
                break
            dots.add(tuple(map(int, line.strip().split(','))))
        lines = []
        for line in data:
            axis,val = line.strip().split()[2].split('=')
            lines.append((axis, int(val)))
        return dots,lines

def fold(dots, line):
    new_dots = set()
    axis, val = line
    for x,y in dots:
        if axis == 'x':
            new_dots.add((2*val-x, y) if x > val else (x, y))
        else:
            new_dots.add((x, 2*val-y) if y > val else (x, y))
    return new_dots

def part_one(dots, lines):
    return len(fold(dots, lines[0]))

def part_two(dots, lines):
    for line in lines:
        dots = fold(dots, line)
    xmax, ymax = 0, 0
    for x,y in dots:
        xmax, ymax = max(x, xmax), max(y, ymax)
    return [''.join('#' if (x, y) in dots else ' ' for x in range(xmax+1)) for y in range(ymax+1)]

if __name__ == "__main__":
    main()
