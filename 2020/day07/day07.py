def main():
    ''' Memoizing can_hold() and bags_held() is unnecessary '''
    bags = dict()
    with open('input') as data:
        for line in data:
            line = line.strip().split()
            bag = line[0] + line[1]
            bags[bag] = dict()
            if line[4] == 'no':
                continue
            for num, adj, color in zip(line[4::4], line[5::4], line[6::4]):
                bags[bag][adj+color] = int(num)
    def can_hold(bag):
        ''' Return True if 'bag' can hold 'shinygold' else False '''
        return 'shinygold' in bags[bag] or any(can_hold(b) for b in bags[bag])
    def bags_held(bag):
        ''' Returns the number of bags held by 'bag' '''
        return sum(bags[bag][b]*(bags_held(b)+1) for b in bags[bag])
    print(sum(map(can_hold, bags)), bags_held('shinygold'))

if __name__ == "__main__":
    main()
