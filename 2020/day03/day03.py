def main():
    rows = []
    with open('input') as data:
        rows = [line.strip() for line in data]
    length = len(rows[0])
    def trees(down, right):
        ''' Return number of trees encountered by going 'down' and 'right' over
        all 'rows' '''
        pos = right
        trees_found = 0
        for row in rows[down::down]:
            trees_found += row[pos] == '#'
            pos = (pos + right) % length
        return trees_found
    part1 = trees(1, 3)
    part2 = trees(1, 1) * part1 * trees(1, 5) * trees(1, 7) * trees(2, 1)
    print(part1, part2)

if __name__ == "__main__":
    main()
