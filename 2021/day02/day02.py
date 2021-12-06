def main():
    data = load_data()
    x1, y1 = get_position(data)
    print("Part one:", x1*y1)
    x2, y2 = get_position_revised(data)
    print("Part two:", x2*y2)

def load_data():
    ''' Return the movement instructions in the file 'input' as a list of
    tuples containing (direction, size of change) '''
    moves = []
    with open('input') as data:
        for move in data:
            direction, size = move.split()
            moves.append((direction, int(size)))
    return moves

def get_position(data):
    ''' Return a tuple containing the horizontal and vertical positions after
    following the movements in 'data'. Both positions start at 0. ('forward',
    n) increases horizontal by n, ('up', n) decreases vertical by n, ('down',
    n) increases vertical by n '''
    x, y = 0, 0
    for direction, n in data:
        if direction == 'forward':
            x += n
        elif direction == 'up':
            y -= n
        elif direction == 'down':
            y += n
    return (x, y)

def get_position_revised(data):
    ''' Return a tuple containing the horizontal and vertical positions after
    following the movements in 'data'. Both positions and aim start at 0.
    ('forward', n) increases horizontal by n and vertical by aim*n. ('up', n)
    decreases aim by n, ('down', n) increases aim by n. '''
    aim = 0
    x, y = 0, 0
    for direction, n in data:
        if direction == 'forward':
            x += n
            y += aim*n
        elif direction == 'up':
            aim -= n
        elif direction == 'down':
            aim += n
    return (x, y)

if __name__ == "__main__":
    main()
