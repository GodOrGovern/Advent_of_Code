def main():
    ids = set()
    val = {'F': 0, 'B': 1, 'L': 0, 'R': 1}
    with open('input') as data:
        for line in data:
            ids.add(sum((val[n] << (9-i)) for i, n in enumerate(line[:-1])))
    print(max(ids))
    for cur in ids:
        if cur+1 not in ids and cur+2 in ids:
            print(cur+1)
            break


if __name__ == "__main__":
    main()
