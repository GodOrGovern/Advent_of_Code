''' https://adventofcode.com/2018/day/5 '''

import re

def main():
    ''' Driver function '''
    data = open('/home/david/Documents/Programs/Advent_Code/2018/day05/input')
    polymer = data.readline().rstrip()
    print(f'Part One: {check(polymer)}')
    print(f'Part Two: {remove(polymer)}')

def check(polymer):
    ''' Return the size of the polymer after all reactions have occurred '''
    new_poly, old_poly = '', polymer
    while len(new_poly) != len(polymer):
        polymer = old_poly
        new_poly = ''
        new_poly = re.sub(r'([a-zA-z])(?!\1)(?i:\1)', '', polymer)
        old_poly = new_poly
    return len(polymer)

def remove(polymer):
    ''' Return the length of the shortest polymer that results from removing
    all of any one letter '''
    lengths = []
    for x in range(65, 91):
        modified = polymer.replace(chr(x), '')
        modified = modified.replace(chr(x+32), '')
        lengths.append(check(modified))
    return min(lengths)

if __name__ == "__main__":
    main()
