def main():
    part1, part2 = 0, 0
    for group in open('input').read()[:-1].split('\n\n'):
        yes = {y for y in group if vote != '\n'}
        part1 += len(yes)
        for person in group.split('\n'):
            yes.intersection_update({y for y in person})
        part2 += len(yes)
    print(part1, part2)

if __name__ == "__main__":
    main()
