def main():
    nums, boards = load_data()
    n, board = find_first_winner(nums, boards)
    print("Part One:", n*sum(sum(x for x in row if x != -1) for row in board))
    n, board = find_last_winner(nums, boards)
    print("Part Two:", n*sum(sum(x for x in row if x != -1) for row in board))

def load_data():
    with open('input') as data:
        numbers = list(map(int, data.readline().strip().split(',')))
        data.readline()
        boards = []
        board = []
        for line in data:
            if line == '\n':
                boards.append(board)
                board = []
            else:
                board.append(list(map(int, line.strip().split())))
        return numbers, boards

def find_first_winner(nums, boards):
    for n in nums:
        for board in boards:
            for row in board:
                for i,x in enumerate(row):
                    if x == n:
                        row[i] = -1
                if all(x == -1 for x in row):
                    return n, board
            for i in range(5):
                if all(row[i] == -1 for row in board):
                    return n, board

def find_last_winner(nums, boards):
    winners = set()
    for n in nums:
        for ib,board in enumerate(boards):
            if ib in winners:
                continue
            for row in board:
                for ir,x in enumerate(row):
                    if x == n:
                        row[ir] = -1
                if all(x == -1 for x in row):
                    winners.add(ib)
                    if len(winners) == len(boards):
                        return n, board
            for i in range(5):
                if all(row[i] == -1 for row in board):
                    winners.add(ib)
                    if len(winners) == len(boards):
                        return n, board

if __name__ == "__main__":
    main()
