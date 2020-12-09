with open('input.txt') as f:
    str = f.read()

str = str.split('\n\n')
lst = [x.split('\n') for x in str]
lst = [[y.split(' ') for y in x] for x in lst]
lst = [[item for sublist in x for item in sublist] for x in lst]

part1 = 0
check_field = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

for item in lst:
    # check passport
    gen_str = ""
    gen_str = gen_str.join(item)
    if all(x in gen_str for x in check_field):
        counter += 1

print(part1)