def main():
    data = load_data()
    print("Part one:", part_one(data))
    print("Part two:", part_two(data))

def load_data():
    with open('input') as data:
        points = []
        for line in data:
            start, end = line.strip().split(' -> ')
            (x1, y1), (x2, y2) = start.split(','), end.split(',')
            points.append(((int(x1), int(y1)), (int(x2), int(y2))))
        return points

def overlap(grid):
    count = 0
    for row in grid:
        for point in row:
            if point > 1:
                count += 1
    return count

def part_one(points):
    max_x, max_y = 0, 0
    for (x1, y1), (x2, y2) in points:
        max_x = max(x1, x2, max_x)
        max_y = max(y1, y2, max_y)
    grid = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]
    for (x1, y1), (x2, y2) in points:
        if x1 != x2 and y1 != y2:
            continue
        else:
            x1, x2 = sorted((x1, x2))
            y1, y2 = sorted((y1, y2))
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    grid[y][x] += 1
    return overlap(grid)

def part_two(points):
    max_x, max_y = 0, 0
    for (x1, y1), (x2, y2) in points:
        max_x = max(x1, x2, max_x)
        max_y = max(y1, y2, max_y)
    grid = [[0 for _ in range(max_x+1)] for _ in range(max_y+1)]
    for (x1, y1), (x2, y2) in points:
        dx = 0 if x1 == x2 else (1 if x1 <= x2 else -1)
        dy = 0 if y1 == y2 else (1 if y1 <= y2 else -1)
        for i in range(max(abs(y1-y2), abs(x1-x2))+1):
            grid[y1+i*dy][x1+i*dx] += 1
    return overlap(grid)

if __name__ == "__main__":
    main()
