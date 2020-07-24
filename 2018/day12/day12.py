''' https://adventofcode.com/2018/day/12 '''

def main():
    ''' Driver function '''
    input_file = '/home/david/Documents/Programs/Advent_Code/2018/day12/input'
    rule, current = load_data(input_file)
    print(f'Part One: {plant_sum(20, rule, current)}')
    gens = 5*10**10
    print(f'Part Two: {52*gens + 919}')

def load_data(file_name):
    ''' Load initial state and rules from file referred to by 'file_name'. Rules are represented as a dict where keys are states and values are what they become '''
    rule = dict()
    with open(file_name, 'r') as data:
        initial = data.readline().strip().split(': ')[1]
        data.readline()
        for line in data:
            rule[line[:5]] = line[9]
    return rule, initial

def plant_sum(gens, rule, current):
    ''' Find sum of cells that are turned on after gens iterations '''
    for _ in range(gens):
        current = find_next_gen(rule, '..'+current+'..')
    total = 0
    for index, state in enumerate(current):
        if state == '#':
            total += index - gens
    return total

def find_next_gen(rule, current):
    ''' Return next generation '''
    length = len(current)
    next_gen = ''
    for x in range(1, length-1):
        if x == 1:
            nhood = '.' + current[:x+3]
        elif x == length - 2:
            nhood = current[x-2:] + '.'
        else:
            nhood = current[x-2:x+3]
        next_gen += rule[nhood]
    return next_gen

if __name__ == "__main__":
    main()
