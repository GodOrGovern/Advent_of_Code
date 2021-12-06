def main():
    valid = 0
    for line in open('input'):
        a, b, c = map(int, line.strip().split())
        valid += a+b > c and a+c > b and b+c > a
    print(valid)

if __name__ == "__main__":
    main()
