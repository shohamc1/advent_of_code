with open('input.txt') as f:
    str = f.read()

str = str.split('\n\n')
str.pop(len(str) - 1)
str = [x.split('\n') for x in str]

counter = 0

for group in str:
    a = "".join(group)
    print(group, len(set(a)))
    counter += len(set(a))

print(counter)