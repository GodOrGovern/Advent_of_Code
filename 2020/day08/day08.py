ops = [line.strip().split() for line in open('input')]
end = len(ops)
def run_code(code):
    cur, acc = 0, 0
    visited = set()
    while cur < end and cur not in visited:
        visited.add(cur)
        acc += int(code[cur][1]) if code[cur][0] == 'acc' else 0
        cur += int(code[cur][1]) if code[cur][0] == 'jmp' else 1
    return cur, acc
change = {'nop': 'jmp', 'jmp': 'nop', 'acc': 'acc'}
for i, (op, val) in enumerate(ops):
    cur, acc = run_code(ops[:i] + [[change[op], val]] + ops[i+1:])
    if cur == end:
        break
print(run_code(ops)[1], acc)
