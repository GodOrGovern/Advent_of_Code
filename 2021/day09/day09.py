def main():
    data = load_data()
    print("Part One:", part_one(data))
    print("Part Two:", part_two(data))

def load_data():
    with open('input') as data:
        points = []
        for line in data:
            row = [int(n) for n in line.strip()]
            points.append(row)
        return points

def get_adjacent(x, y, xmax, ymax):
    adj = []
    if x != 0:
        adj.append((x-1, y))
    if x != xmax-1:
        adj.append((x+1, y))
    if y != 0:
        adj.append((x, y-1))
    if y != ymax-1:
        adj.append((x, y+1))
    return adj

def get_low_points(points, xmax, ymax):
    low_points = []
    for y,row in enumerate(points):
        for x,p in enumerate(row):
            if all(p < points[ay][ax] for ax,ay in get_adjacent(x, y, xmax, ymax)):
                low_points.append((x, y))
    return low_points

def part_one(points):
    xmax, ymax = len(points[0]), len(points)
    return sum(points[y][x]+1 for x,y in get_low_points(points, xmax, ymax))

def part_two(points):
    xmax, ymax = len(points[0]), len(points)
    def basin_size(x, y):
        found = {(x, y)}
        def helper(x, y):
            total = 0
            for ax,ay in get_adjacent(x, y, xmax, ymax):
                if points[y][x] < points[ay][ax] < 9 and (ax, ay) not in found:
                    found.add((ax, ay))
                    total += 1+helper(ax, ay)
            return total
        return 1+helper(x, y)
    sizes = [basin_size(x, y) for x,y in get_low_points(points, xmax, ymax)]
    total = 1
    for s in sorted(sizes)[-3:]:
        total *= s
    return total

if __name__ == "__main__":
    main()
