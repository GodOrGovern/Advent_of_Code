def main():
    valid1, valid2 = 0, 0
    with open('input') as data:
        for line in data:
            nums, char, pswd = line.split(' ')
            low, high = [int(n) for n in nums.split('-')]
            valid1 += low <= pswd.count(char[0]) <= high
            valid2 += (pswd[low-1] == char[0]) ^ (pswd[high-1] == char[0])
    print(valid1, valid2)

if __name__ == "__main__":
    main()
