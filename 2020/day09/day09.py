from collections import defaultdict

nums = [int(n) for n in open('input').read().strip().split()]
prev25 = defaultdict(int)
for i, x in enumerate(nums[:25]):
    for y in nums[i+1:25]:
        prev25[x+y] += 1
pos = 25
while nums[pos] in prev25:
    for n in nums[pos-24:pos]:
        prev25[nums[pos-25]+n] -= 1
    pos += 1
    for n in nums[pos-25:pos]:
        prev25[nums[pos]+n] += 1
print(nums[pos])
for i1, n1 in enumerate(nums[:-1]):
    val = n1 + nums[i1+1]
    for i2, n2 in enumerate(nums[i1+2:]):
        if val == nums[pos]:
            print(min(nums[i1:i1+i2+1]) + max(nums[i1:i1+i2+1]))
            break
        val += n2
    if val == nums[pos]:
        break
