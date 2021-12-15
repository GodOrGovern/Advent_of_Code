from collections import Counter

def main():
    polymer,rules = load_data()
    print("Part One:", part_one(polymer, rules))
    print("Part Two:", part_two(polymer, rules))

def load_data():
    with open('input') as data:
        polymer = data.readline().strip()
        data.readline()
        rules = dict()
        for line in data:
            adj,insert = line.strip().split(' -> ')
            rules[adj] = insert
        return polymer,rules

def get_count_diff(polymer, rules, end):
    memoize = dict()
    def get_count(a, b, step):
        if step == end:
            return Counter('')
        if (a, b, step) not in memoize:
            new = rules[a+b]
            memoize[(a,b,step)] = Counter(new) + get_count(a,new,step+1) + get_count(new,b,step+1)
        return memoize[(a, b, step)]
    counts = Counter(polymer)
    for a,b in zip(polymer[:-1], polymer[1:]):
        counts += get_count(a, b, 0)
    return max(counts.values()) - min(counts.values())

def part_one(polymer, rules):
    return get_count_diff(polymer, rules, 10)

def part_two(polymer, rules):
    return get_count_diff(polymer, rules, 40)

if __name__ == "__main__":
    main()
