''' https://adventofcode.com/2019/day/2 '''

from operator import mul, add

def main():
    ''' Driver function '''
    file_name = '/home/david/Documents/Programs/Advent_Code/2019/day02/input'
    codes = load_data(file_name)
    orig_codes = codes[:]
    run_program(codes)
    print(f'Part One: {codes[0]}')
    noun, verb = find_pair(orig_codes)
    print(f'Part Two: {100*noun + verb}')

def load_data(file_name):
    ''' Return list of numbers from file represented by 'file_name' '''
    with open(file_name) as data:
        nums = [int(n) for n in data.readline().split(',')]
    return nums

def run_program(codes):
    ''' Simulate running the program represented by 'codes' '''
    pos = 0
    while codes[pos] != 99:
        op = add if codes[pos] == 1 else mul
        codes[codes[pos+3]] = op(codes[codes[pos+1]], codes[codes[pos+2]])
        pos += 4
    return codes

def find_pair(codes):
    ''' Find the noun and verb that cause 'codes[0]' to be 19690720 '''
    for p1 in range(100):
        codes[1] = p1
        for p2 in range(100):
            codes[2] = p2
            if run_program(codes[:])[0] == 19690720:
                return p1, p2
    return None, None

if __name__ == "__main__":
    main()