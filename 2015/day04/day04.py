from hashlib import md5

data = 'yzbqklnj'
num1 = 0
while md5((data+str(num1)).encode()).hexdigest()[:5] != '00000':
    num1 += 1
num2 = num1
while md5((data+str(num2)).encode()).hexdigest()[:6] != '000000':
    num2 += 1
print(num1, num2)
