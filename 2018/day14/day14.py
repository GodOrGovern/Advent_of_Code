''' https://adventofcode.com/2018/day/14 '''

def main():
    ''' Driver function '''
    end = 513401
    a, b = 0, 1
    scores = [3, 7]
    while len(scores) < end+10:
        a, b = add_scores(a, b, scores)
    print("Part One:", ''.join([str(n) for n in scores[end:end+10]]))
    index = find_instance(a, b, scores)
    print("Part Two:", len(scores) - index)

def add_scores(a, b, scores):
    ''' The values of 'scores[a]' and 'scores[b]' are added. Each digit of the
    result is appended to 'scores'. After all new values are added to 'scores',
    both indexes are updated by moving to the index located at '(1 +
    scores[index] + index) % len(scores)'. The updated indexes are returned '''
    scores.extend([int(n) for n in str(scores[a]+scores[b])])
    length = len(scores)
    return (1+a+scores[a]) % length, (1+b+scores[b]) % length

def find_instance(a, b, scores):
    ''' Find the first instance of 513401 in 'scores'  '''
    index = 0
    end = [5, 1, 3, 4, 0, 1]
    while index < 6:
        value = scores[a] + scores[b]
        if index == 0 and value % 10 == 5:
            index += 1
        elif index == 1 and value == 13:
            index += 2
        elif index == 5 and value // 10 == 1:
            index += 2
        elif value == end[index]:
            index += 1
        else:
            index = 0
        a, b = add_scores(a, b, scores)
    return index

if __name__ == "__main__":
    main()