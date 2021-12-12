def main():
    data = load_data()
    print("Part One:", part_one(data))
    print("Part Two:", part_two(data))

def load_data():
    with open('input') as data:
        return list(map(int, data.readline().strip().split(',')))

def part_one(data):
    def f(timer, days):
        if days == 0:
            return 1
        elif timer == 0:
            return f(6, days-1) + f(8, days-1)
        else:
            return f(timer-1, days-1)
    return sum(f(fish, 80) for fish in data)

def part_two(data):
    memoize = [[0 for _ in range(257)] for _ in range(9)]
    def f(timer, days):
        if memoize[timer][days] != 0:
            return memoize[timer][days]
        elif days == 0:
            memoize[timer][days] = 1
        elif timer == 0:
            memoize[timer][days] = f(6, days-1) + f(8, days-1)
        else:
            memoize[timer][days] = f(timer-1, days-1)
        return memoize[timer][days]
    return sum(f(fish, 256) for fish in data)

if __name__ == "__main__":
    main()
