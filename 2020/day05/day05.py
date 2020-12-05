def main():
    max_id = 0
    ids = set()
    with open('input') as data:
        for line in data:
            pos = {'F': 0, 'B': 1, 'L': 0, 'R': 1}
            row = sum((pos[n] << (6-i)) for i, n in enumerate(line[:7]))
            col = sum((pos[n] << (2-i)) for i, n in enumerate(line[7:10]))
            seat_id = row*8 + col
            ids.add(seat_id)
            max_id = max(seat_id, max_id)
    print(max_id)
    for row in range(128):
        for col in range(8):
            cur = row*8 + col
            if cur not in ids and cur-1 in ids and cur+1 in ids:
                print(cur)


if __name__ == "__main__":
    main()
