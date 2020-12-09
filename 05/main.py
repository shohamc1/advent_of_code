import math
with open('input.txt') as f:
    str = f.read()

str = str.split('\n')
ids = []

def findRow(s):
    low = 0
    high = 127

    s_low = 0
    s_high = 7

    for char in s:
        if (char == 'F'):
            high = low + math.floor((high - low) / 2)
        elif (char == 'B'):
            low = low + math.ceil((high - low) / 2)
        elif (char == 'R'):
            s_high = s_low + math.floor((s_high - s_low) / 2)
        elif (char == 'L'):
            s_low = s_low + math.ceil((s_high - s_low) / 2)
    
    ids.append(s_low + low*8)
    return (s_low + low*8)
        
lst = []

for string in str:
    lst.append(findRow(string))

print(max(lst))

p2 = 0
for ide in sorted(lst):
    if ide + 1 not in lst and ide + 2 in lst:
        p2 = ide + 1

print(p2)