floor, pos = 0, 0
for i, c in enumerate(open('input').read().strip()):
    floor += 1 if c == '(' else -1
    if not pos and floor < 0:
        pos = i + 1
print(floor, pos)
