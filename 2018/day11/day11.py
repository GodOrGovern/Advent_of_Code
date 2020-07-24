''' https://adventofcode.com/2018/day/11 '''

import numpy as np

def main():
    ''' Driver function '''
    grid = init_grid(300, 5535)
    cord, _ = cell_power(grid, 3)
    print(f'Part One: {cord}')
    cord = any_size_power(grid)
    print(f'Part Two: {cord}')

def init_grid(grid_size, serial):
    ''' Create square grid of size 'grid_size' and fill according to rules '''
    grid = np.zeros((grid_size, grid_size), dtype=int)
    for x in range(1, grid_size+1):
        rack_ID = x + 10
        for y in range(1, grid_size+1):
            grid[x-1][y-1] = rack_ID*(rack_ID*y + serial) // 100 % 10 - 5
    return grid

def cell_power(grid, sq_size):
    ''' Find the square of size 'sq_size' with the largest total power '''
    max_power = 0
    cord = (None, None)
    for x in range(0, grid.shape[1] - sq_size + 1):
        for y in range(0, grid.shape[0] - sq_size + 1):
            cur_power = grid[x:x+sq_size, y:y+sq_size].sum()
            if cur_power > max_power:
                max_power = cur_power
                cord = (x+1, y+1)
    return cord, max_power

def any_size_power(grid):
    ''' Find the square of any size with the largest total power '''
    max_power = 0
    for x in range(1, grid.shape[0] + 1):
        cur_cord, cur_power = cell_power(grid, x)
        if cur_power > max_power:
            max_power = cur_power
            max_cord = cur_cord + (x,)
    return max_cord

if __name__ == "__main__":
    main()
