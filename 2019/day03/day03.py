''' https://adventofcode.com/2019/day/3 '''

from collections import defaultdict

def main():
    ''' Driver function '''
    file_name = "/home/david/Documents/Programs/Advent_Code/2019/day03/input"
    wire_path = defaultdict(int)
    path1, path2 = load_data(file_name)
    wire1 = get_wire_path(path1, wire_path)
    wire2 = get_wire_path(path2, wire_path)
    wire_cross = wire1.intersection(wire2) - {(0, 0)}
    print(f'Part One: {find_close_cross(wire_cross)}')

def load_data(file_name):
    ''' Load data from file represented by 'file_name'. Returns a tuple
    containing two lists of tuples of the form (direction, length) '''
    vals = ([], [])
    with open(file_name) as data:
        for lst in range(2):
            for val in data.readline().split(','):
                vals[lst].append((val[0], int(val[1:])))
    return vals

def get_wire_path(vals, wires):
    ''' Trace the wire path as indicated by 'vals'. For each position that
    the wire crosses, increment the corresponding entry in 'wires' by 1 '''
    wires = set()
    x, y = 0, 0
    for dir, length in vals:
        step = 1 if dir in {'R', 'U'} else -1
        if dir in {'L', 'R'}:
            x_prev = x
            x += length * step
            for x_cur in range(x_prev, x, step):
                wires.add((x_cur, y))
        elif dir in {'D', 'U'}:
            y_prev = y
            y += length * step
            for y_cur in range(y_prev, y, step):
                wires.add((x, y_cur))
    return wires

def find_close_cross(wire_cross):
    ''' Find the point closest to (0, 0) where the wires cross '''
    min_dist = float("inf")
    for x, y in wire_cross:
        min_dist = min(min_dist, manhattan_distance((x, y), (0, 0)))
    return min_dist

def manhattan_distance(start, end):
    ''' Manhattan distance from 'start' to 'end' '''
    return sum(abs(n-end[i]) for i, n in enumerate(start))

if __name__ == "__main__":
    main()