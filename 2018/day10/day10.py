''' https://adventofcode.com/2018/day/10 '''

import re
import matplotlib.pyplot as plt

def main():
    ''' Driver function '''
    input_file = '/home/david/Documents/Programs/Advent_Code/day10/input'
    points = load_data(input_file)
    seconds = 10905 # answer to Part Two
    xs, ys = pos_after(points, seconds)
    plt.scatter(xs, ys)
    plt.show()

def load_data(file_name):
    ''' Load data from the file represented by 'file_name'. Returns a list of lists, where each sublist contains (in the following order): [x, y, x_vel, y_vel] where the first two are points and the second two are velocities '''
    points = []
    input_file = '/home/david/Documents/Programs/Advent_Code/day10/input'
    with open(input_file) as data:
        for line in data:
            point = re.findall(r'((?:-|\d)+)', line)
            points.append([int(p) for p in point])
    return points

def pos_after(points, time):
    ''' Change the position of each each point in 'points' to what it will be after 'time' seconds '''
    for p in points:
        p[0] += p[2] * time
        p[1] += p[3] * time
    return ([p[0] for p in points], [p[1] for p in points])

if __name__ == "__main__":
    main()