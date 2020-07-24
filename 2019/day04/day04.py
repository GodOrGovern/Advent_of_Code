''' adventofcode.com/2019/day/4 '''

from collections import Counter

def main():
    ''' Driver function '''
    total1 = 0
    total2 = 0
    for n in range(245182, 790573):
        str_n = str(n)
        if in_order(str_n):
            total1 += two_adjacent(str_n)
            total2 += two_adjacent_alone(str_n)
    print(f'Part One: {total1}')
    print(f'Part Two: {total2}')

def in_order(str_n):
    ''' Determine if the digits of 'str_n' are in increasing order '''
    for i, d in enumerate(str_n[:-1]):
        if d > str_n[i+1]:
            return False
    return True

def two_adjacent(str_n):
    ''' Determine if the number represented by 'str_n' has two adjacent
    digits that are the same '''
    for n in Counter(str_n).values():
        if n >= 2:
            return True
    return False

def two_adjacent_alone(str_n):
    ''' Determine if the number represented by 'str_n' has two adjacent
    digits that are the same and are not part of a larger group of matching
    digits '''
    for n in Counter(str_n).values():
        if n == 2:
            return True
    return False

if __name__ == "__main__":
    main()