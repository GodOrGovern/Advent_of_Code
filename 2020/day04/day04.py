from re import match

def main():
    ''' There's probably a much nicer way to do this but it just werks so don't
    insult my spaghetti '''
    valid1, valid2 = 0, 0
    with open('input') as data:
        for pasprt in data.read().split('\n\n'):
            invalid = False
            fields = set()
            for field in pasprt.split():
                name, val = field.split(':')
                fields.add(name)
                if invalid:
                    continue
                if name == 'byr' and (val < '1920' or val > '2002'):
                    invalid = True
                elif name == 'iyr' and (val < '2010' or val > '2020'):
                    invalid = True
                elif name == 'eyr' and (val < '2020' or val > '2030'):
                    invalid = True
                elif name == 'hgt':
                    hgt = match('(\d{2}|\d{3})(cm|in)', val)
                    if not hgt:
                        invalid = True
                        continue
                    num, unit = int(hgt.group(1)), hgt.group(2)
                    if not invalid and unit == 'cm' and (num < 150 or num > 193):
                        invalid = True
                    elif unit == 'in' and (num < 59 or num > 76):
                        invalid = True
                elif name == 'hcl' and not match('^#[a-f0-9]{6}$', val):
                    invalid = True
                elif name == 'ecl' and val not in {'amb','blu','brn','gry','grn','hzl','oth'}:
                    invalid = True
                elif name == 'pid' and len(val) != 9:
                    invalid = True
            if len(fields-{'cid'}) == 7:
                valid1 += 1
                valid2 += not invalid
    print(valid1, valid2)

if __name__ == "__main__":
    main()
