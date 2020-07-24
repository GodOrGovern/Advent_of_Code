''' https://adventofcode.com/2018/day/2 '''

def main():
    ''' Driver function '''
    input_file = '/home/david/Documents/Programs/Advent_Code/day02/input'
    print(f'Part One: {checksum(input_file)}')
    print(f'Part Two: {similar(input_file)}')

def checksum(file_name):
    ''' Implements checksum on data in file represented by 'file_name' where the
    number of words containing two of the same letter is multiplied by the
    number of words containing three of the same letter. The same word can be
    counted as both '''
    two, three = 0, 0
    with open(file_name) as data:
        for line in data:
            result = set()
            for letter in set(line):
                result.add(sum(letter == char for char in line))
            if 2 in result:
                two += 1
            if 3 in result:
                three += 1
    return two * three

def similar(file_name):
    ''' Finds the IDs that differ by one character and return characters that
    they have in common '''
    with open(file_name) as data:
        lines = [line.rstrip() for line in data]
    for i, x in enumerate(lines):
        for y in range(1, len(lines[i::])):
            if one_diff(x, lines[i+y]):
                return rem_diff(x, lines[i+y])
    return None

def one_diff(str_one, str_two):
    ''' Returns True if 'str_one' and 'str_two' differ by only one character.
    Otherwise it returns False '''
    diff = 0
    for i, c in enumerate(str_one):
        if c != str_two[i]:
            diff += 1
        if diff > 1:
            return False
    return True

def rem_diff(str_one, str_two):
    ''' Returns an ordered string of characters that 'str_one' and 'str_two'
    have in common '''
    common = ''
    for i, c in enumerate(str_one):
        if c == str_two[i]:
            common += c
    return common

if __name__ == '__main__':
    main()