''' https://adventofcode.com/2018/day/4 '''

import re

class Guard:
    ''' A simple data structure to keep track of each guard '''
    def __init__(self, id_num):
        self.id_num = id_num
        self.sleep = 0
        self.time = [0 for x in range(60)]
    def __repr__(self):
        return str(self.id_num)

def main():
    ''' Driver function '''
    input_file = '/home/david/Documents/Programs/Advent_Code/2018/day04/input'
    records = organize(input_file)
    guards = load_guards(records)
    max_guard = max(guards, key=lambda x: x.sleep)
    max_min = max_guard.time.index(max(max_guard.time))
    print(f'Part One: {max_guard.id_num * max_min}')
    print(f'Part Two: {freq_min(guards)}')

def organize(file_name):
    ''' Load the guard records from 'file_name' and return in a sorted list '''
    records = []
    with open(file_name) as data:
        for line in data:
            line = re.sub(r'\[|\]|[A-z#]', '', line)
            line = re.sub(r'\-|:', ' ', line)
            records.append(line.rstrip())
    records.sort()
    return records

def load_guards(records):
    ''' Load the guards into a list and use 'load_time()' to load sleep and
    wake times for each shift. Return the list of guards '''
    guards = []
    shift = []
    for entry in records:
        entry = entry.split()
        if len(entry) == 6:
            id_num = int(entry[-1])
            if find_guard(guards, id_num) == None:
                guards.append(Guard(id_num))
        else:
            shift.append(entry)
        if len(shift) == 2:
            load_time(guards, id_num, shift)
            shift = []
    return guards

def load_time(guards, id_num, shift):
    ''' Load sleep and wake times for the guard with 'id_num' given the info
    provided in 'shift' '''
    sleep = int(shift[0][4])
    wake = int(shift[1][4])
    index = find_guard(guards, id_num)
    guards[index].sleep += wake - sleep
    for t in range(sleep, wake):
        guards[index].time[t] += 1

def freq_min(guards):
    ''' Find the guard who is most frequently asleep on the same minute. Return
    the guard's 'id_num' multiplied by the minute he was most often asleep '''
    cur_max = [0, 0]
    id_num = 0
    for guard in guards:
        temp_max = max(guard.time)
        if temp_max > cur_max[0]:
            cur_max[0] = temp_max
            cur_max[1] = guard.time.index(temp_max)
            id_num = guard.id_num
    return cur_max[1] * id_num

def find_guard(guards, id_num):
    ''' Try to find the guard with 'id_num'. If one is found, return its index.
    Otherwise return None '''
    for index, guard in enumerate(guards):
        if guard.id_num == id_num:
            return index
    return None

if __name__ == "__main__":
    main()
