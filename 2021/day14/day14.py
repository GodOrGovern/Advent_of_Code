from collections import defaultdict

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
    c_to_n = {c:n for n,c in enumerate(set(polymer))}
    chars = len(c_to_n)
    memoize = dict()
    def expand(polymer, step):
        if (polymer, step) in memoize:
            return memoize[(polymer, step)]
        count = [0] * chars
        for c in polymer:
            count[c_to_n[c]] += 1
        if step != end:
            for a,b in zip(polymer[:-1], polymer[1:]):
                new = rules[a+b]
                for n,x in enumerate(expand(a+new, step+1)):
                    count[n] += x
                for n,x in enumerate(expand(new+b, step+1)):
                    count[n] += x
                for c in (a, new, b):
                    count[c_to_n[c]] -= 1
        memoize[(polymer, step)] = tuple(count)
        return memoize[(polymer, step)]
    counts = expand(polymer, 0)
    return max(counts) - min(counts)

def part_one(polymer, rules):
    return get_count_diff(polymer, rules, 10)

def part_two(polymer, rules):
    return get_count_diff(polymer, rules, 40)

if __name__ == "__main__":
    main()
