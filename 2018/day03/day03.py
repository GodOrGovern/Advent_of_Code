''' https://adventofcode.com/2018/day/3 '''

import re
import numpy as np

def main():
    ''' Driver function '''
    input_file = '/home/david/Documents/Programs/Advent_Code/day03/input'
    vals = load(input_file)
    matrix = fill(vals)
    print(f'Part One: {len(matrix[matrix >= 2])}')
    print(f'Part Two: {intact(matrix, vals)}')

def load(file_name):
    ''' Load data from 'file_name' as a list of 5-tuples. The format is (ID, x,
    y, width, height) '''
    vals = []
    with open(file_name) as data:
        for line in data:
            vals.append(re.split(' @ |,|: |x', line.lstrip('#')))
    vals = [tuple(map(int, val)) for val in vals]
    return vals

def fill(vals):
    ''' Create a 2d matrix using largest possible width and height in vals as
    dimensions. Initialize each index to 0. For each tuple in 'vals', increment
    the corresponding indices by 1. Return 'matrix' '''
    width = max([val[1] + val[3] for val in vals])
    height = max([val[2] + val[4] for val in vals])
    matrix = np.array([[0 for x in range(width)] for y in range(height)])
    for val in vals:
        matrix[val[2]:(val[2] + val[4]), val[1]:(val[1] + val[3])] += 1
    return matrix

def intact(matrix, vals):
    ''' For each tuple in 'vals', check if any of the corresponding indices
    have been counted more than once. If not, return the ID of that tuple '''
    for val in vals:
        if np.all(matrix[val[2]:(val[2]+val[4]), val[1]:(val[1]+val[3])] == 1):
            return val[0]
    return None

if __name__ == '__main__':
    main()
