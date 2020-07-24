''' https://adventofcode.com/2019/day/1 '''

def main():
    ''' Driver function '''
    file_name = '/home/david/Documents/Programs/Advent_Code/2019/day01/input'
    masses = load_data(file_name)
    print(f'Part One: {calc_fuel_naive(masses)}')
    print(f'Part Two: {calc_fuel(masses)}')

def load_data(file_name):
    ''' Return list of numbers from file represented by 'file_name' '''
    with open(file_name) as data:
        nums = [int(line) for line in data]
    return nums

def calc_fuel_naive(masses):
    ''' Given a list of masses, find the required amount of fuel. Does not
    take mass of fuel into account '''
    total = 0
    for n in masses:
        total += n // 3 - 2
    return total

def calc_fuel(masses):
    ''' Given a list of masses, find the required amount of fuel. Takes mass
    of fuel into account '''
    total = 0
    for n in masses:
        new_fuel = n // 3 - 2
        while new_fuel > 0:
            total += new_fuel
            new_fuel = new_fuel // 3 - 2
    return total

if __name__ == "__main__":
    main()