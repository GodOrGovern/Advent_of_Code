lights = [[[0, 0] for _ in range(1000)] for _ in range(1000)]
for line in open('input'):
    line = line.split()
    op = line[1] == 'on' if line[0] == 'turn' else 2
    (x1, y1), (x2, y2) = map(int, line[-3].split(',')), map(int, line[-1].split(','))
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            l1, l2 = lights[x][y]
            lights[x][y] = [[0, max(0, l2-1)], [1, l2+1], [not l1, l2+2]][op]
print(sum(sum(light[0] for light in row) for row in lights))
print(sum(sum(light[1] for light in row) for row in lights))
