''' https://adventofcode.com/2018/day/6 '''

import numpy as np

def main():
    ''' Driver function '''
    input_file = '/home/david/Documents/Programs/Advent_Code/day06/input'
    points = load(input_file)
    grid, safe = fill(points)
    size = check(grid, points)
    print(f'Part One: {size}')
    print(f'Part Two: {safe}')

def load(file_name):
    ''' Load points from 'file_name' into list and return as numpy array '''
    points = []
    with open(file_name) as data:
        for line in data:
            points.append([int(n) for n in line.split(', ')])
    return np.array(points)

def fill(points):
    ''' Fill the grid using 'points'. Return both 'grid' and the number of safe
    spots (spots less than a total of 10,000 units away from all coordinate
    points) '''
    x_max = max(points[:,0])
    x_min = min(points[:,0])
    y_max = max(points[:,1])
    y_min = min(points[:,1])
    x_range = x_max - x_min + 1
    y_range = y_max - y_min + 1
    grid = np.full((y_range, x_range), None)
    safe = 0
    for x in range(x_range):
        for y in range(y_range):
            dist = abs(x+x_min-points[:,0]) + abs(y+y_min-points[:,1])
            if sum(dist) < 10000:
                safe += 1
            mins = np.where(dist == dist.min())
            grid[y,x] = mins[0][0] if len(mins[0]) == 1 else -1
    return grid, safe

def check(grid, points):
    ''' Return the size of the largest non-infinite area in 'grid' '''
    border = set(np.concatenate((grid[0], grid[-1], grid[:,0], grid[:,-1])))
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y,x] in border:
                grid[y,x] = -1
    _, count = np.unique(grid, return_counts=True)
    return max(count[1:])

if __name__ == "__main__":
    main()