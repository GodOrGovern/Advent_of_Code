''' https://adventofcode.com/2018/day/1 '''

def main():
    ''' Driver function '''
    nums = load('/home/david/Documents/Programs/Advent_Code/2018/day01/input')
    repeat = find_repeat(nums)
    print(f'Part One: {sum(nums)}')
    print(f'Part Two: {repeat}')

def load(file_name):
    ''' Load the numbers from the file represented by 'file_name' into a list.
    Return that list '''
    with open(file_name) as data:
        nums = [int(n) for n in data]
    return nums

def find_repeat(nums):
    ''' Apply values in 'nums' until a number appears twice. Return repeated
    number '''
    index, total = 0, 0
    freqs = set()
    length = len(nums)
    while total not in freqs:
        freqs.add(total)
        total += nums[index % length]
        index += 1
    return total

if __name__ == '__main__':
    main()
