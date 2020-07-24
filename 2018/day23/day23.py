''' https://adventofcode.com/2018/day/23 '''

import re

def main():
    ''' Driver function '''
    coordinates = load('/home/david/Documents/Programs/Advent_Code/2018/day23/input')
    print(f'Part One: {nanobots(coordinates)}')

def load(file_name):
    ''' Loads coordinates from 'file_name' into array. The format is a list
    of lists where each sublist contains (in the following order): [x, y, z,
    r] where the first three are coordinate points corresponding to
    their listed names and 'r' is a radius. It can be thought of as the center
    of a circle with radius 'r' '''
    coordinates = []
    with open(file_name) as data:
        for line in data:
            line = re.sub(r'pos|<|>|=| r|\n', '', line)
            coordinates.append([int(cord) for cord in line.split(',')])
    return coordinates

def nanobots(coordinates):
    ''' Determines how many nanobots are in range of the nanobot with the
    largest signal radius '''
    strong = max(coordinates, key=lambda cord: cord[3])
    count = 0
    for cord in coordinates:
        distance = sum(abs(strong[x] - cord[x]) for x in range(3))
        if distance <= strong[3]:
            count += 1
    return count

if __name__ == "__main__":
    main()
