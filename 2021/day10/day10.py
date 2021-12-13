def main():
    data = load_data()
    print("Part One:", part_one(data))
    print("Part Two:", part_two(data))

def load_data():
    with open('input') as data:
        return [line.strip() for line in data]

def part_one(data):
    pairs = {')':'(', ']':'[', '}':'{', '>':'<'}
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0
    for line in data:
        stack = []
        for c in line:
            if c in {'(', '[', '{', '<'}:
                stack.append(c)
            elif pairs[c] != stack.pop():
                score += points[c]
                break
    return score

def part_two(data):
    pairs = {')':'(', ']':'[', '}':'{', '>':'<'}
    points = {'(': 1, '[': 2, '{': 3, '<': 4}
    scores = []
    for line in data:
        stack = []
        for c in line:
            if c in {'(', '[', '{', '<'}:
                stack.append(c)
            elif pairs[c] != stack.pop():
                break
        else:
            score = 0
            for c in stack[::-1]:
                score = (score * 5) + points[c]
            scores.append(score)
    return sorted(scores)[(len(scores)-1)//2]

if __name__ == "__main__":
    main()
