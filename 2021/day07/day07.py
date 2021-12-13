def main():
    data = load_data()
    print("Part One:", part_one(data))
    print("Part Two:", part_two(data))

def load_data():
    with open('input') as data:
        return list(map(int, data.readline().strip().split(',')))

def part_one(data):
    def fuel_cost(pos):
        return sum(abs(x-pos) for x in data)
    return min(fuel_cost(n) for n in range(min(data), max(data)+1))

def part_two(data):
    def fuel_cost(pos):
        cost = 0
        for x in data:
            steps = abs(x-pos)
            cost += (steps*(steps+1))//2
        return cost
    return min(fuel_cost(n) for n in range(min(data), max(data)+1))

if __name__ == "__main__":
    main()
