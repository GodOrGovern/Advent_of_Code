code1, code2 = '', ''
(x1, y1), (x2, y2) = (1, 1), (2, 0)
pad1, pad2 = ('123', '456', '789'), ('00100', '02340', '56789', '0ABC0', '00D00')
move = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
for line in open('input'):
    for c in line.strip():
        dx, dy = move[c]
        if 0 <= x1+dx < 3 and 0 <= y1+dy < 3:
            x1, y1 = x1 + dx, y1 + dy
        if 0 <= x2+dx < 5 and 0 <= y2+dy < 5 and pad2[x2+dx][y2+dy] != '0':
            x2, y2 = x2 + dx, y2 + dy
    code1, code2 = code1 + pad1[x1][y1], code2 + pad2[x2][y2]
print(code1, code2)
