def main():
    data = load_data()
    print("Part One:", part_one(data))
    print("Part Two:", part_two(data))

def load_data():
    with open('input') as data:
        entries = []
        for line in data:
            signal, output = line.strip().split(' | ')
            entries.append([signal.split(), output.split()])
        return entries

def part_one(data):
    count = 0
    for _,output in data:
        count += sum(len(val) in {2, 3, 4, 7} for val in output)
    return count

def part_two(data):
    count = 0
    segs_to_digit = {'abcefg': '0', 'cf': '1', 'acdeg': '2', 'acdfg': '3', 'bcdf': '4',
                     'abdfg': '5', 'abdefg': '6', 'acf': '7', 'abcdefg': '8', 'abcdfg': '9'}
    for signals,output in data:
        mapping = {c:set() for c in 'abcdefg'}
        segs_by_len = {2:[], 3:[], 4:[], 5:[], 6:[], 7:[]}
        for s in signals:
            segs_by_len[len(s)].append(s)
        a = mapping['a'] = set(segs_by_len[3][0]) - set(segs_by_len[2][0])
        cf = set(segs_by_len[2][0])
        bd = set(segs_by_len[4][0]) - cf
        eg = set(segs_by_len[7][0]) - cf - bd - a
        for s in segs_by_len[6]:
            blank = (a | cf | bd | eg) - set(s)
            if cf.intersection(blank):
                mapping['c'] = blank
                mapping['f'] = cf - blank
            elif bd.intersection(blank):
                mapping['b'] = bd - blank
                mapping['d'] = blank
            else:
                mapping['e'] = blank
                mapping['g'] = eg - blank
        mapping = {v.pop():k for k,v in mapping.items()}
        num = ''
        for n in output:
            digit = ''.join(sorted(mapping[c] for c in n))
            num += segs_to_digit[digit]
        count += int(num)
    return count

if __name__ == "__main__":
    main()
