from re import match, findall

def main():
    ''' Memoizing can_hold() and bags_held() is unnecessary '''
    bags = dict()
    for line in open('input'):
        bag = match('\w+ \w+', line).group(0)
        bags[bag] = {b: int(n) for n, b in findall('(\d) (\w+ \w+)', line)}
    def can_hold(bag):
        ''' Return True if 'bag' can hold 'shinygold' else False '''
        return 'shiny gold' in bags[bag] or any(can_hold(b) for b in bags[bag])
    def bags_held(bag):
        ''' Returns the number of bags held by 'bag' '''
        return sum(bags[bag][b]*(bags_held(b)+1) for b in bags[bag])
    print(sum(map(can_hold, bags)), bags_held('shiny gold'))

if __name__ == "__main__":
    main()
