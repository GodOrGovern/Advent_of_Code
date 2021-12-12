def main():
    data = load_data()
    gamma, epsilon = get_gamma_epsilon(data)
    print("Part One:", gamma*epsilon)
    oxygen, co2 = get_oxygen_co2(data)
    print("Part Two:", oxygen*co2)

def load_data():
    ''' Return the binary numbers found in 'input' as a list of strings '''
    with open('input') as data:
        return list(map(str.strip, data))

def get_gamma_epsilon(data):
    ''' Find and return gamma and epsilon as described in part one of this
    problem: https://adventofcode.com/2021/day/3 '''
    # All numbers have the same length of 12
    bit_counts = [[0, 0] for _ in range(12)]
    for n in data:
        for i,bit in enumerate(n):
            bit_counts[i][int(bit)] += 1
    gamma, epsilon = 0, 0
    for zeroes,ones in bit_counts:
        most = 0 if zeroes > ones else 1
        least = int(not most)
        gamma = (gamma << 1) | most
        epsilon = (epsilon << 1) | least
    return gamma, epsilon

def get_oxygen_co2(data):
    ''' Find and return oxygen generator rating and CO2 scrubber rating as
    described in part two of this problem: https://adventofcode.com/2021/day/3 '''
    oxygen = set(data)
    index = 0
    while len(oxygen) > 1:
        bit_counts = [0, 0]
        for n in oxygen:
            bit_counts[int(n[index])] += 1
        most = '0' if bit_counts[0] > bit_counts[1] else '1'
        oxygen = {n for n in oxygen if n[index] == most}
        index += 1
    co2 = set(data)
    index = 0
    while len(co2) > 1:
        bit_counts = [0, 0]
        for n in co2:
            bit_counts[int(n[index])] += 1
        least = '0' if bit_counts[0] <= bit_counts[1] else '1'
        co2 = {n for n in co2 if n[index] == least}
        index += 1
    return int(oxygen.pop(), 2), int(co2.pop(), 2)

if __name__ == "__main__":
    main()
