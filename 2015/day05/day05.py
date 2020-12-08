from re import search, findall

nice1, nice2 = 0, 0
for line in open('input'):
    nice1 += all([len(findall('[aeiou]', line)) > 2,
                 not search('ab|cd|pq|xy', line),
                 search(r'(\w)\1', line)])
    nice2 += all([search(r'(\w\w).*\1', line),
                  search(r'(\w)\w\1', line)])
print(nice1, nice2)
