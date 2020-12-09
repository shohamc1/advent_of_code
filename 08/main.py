instructions = []

with open('input.txt') as file:
    for line in file:
        data = line.split()
        instructions.append(data)

# Part 1


def calcAcc(instructions):
    visited = set()
    acc = i = 0
    while i not in visited:
        visited.add(i)
        if i >= len(instructions):
            return acc, True
        instruction, value = instructions[i]
        if instruction == 'nop':
            i += 1
        elif instruction == 'jmp':
            i += int(value)
        else:
            i += 1
            acc += int(value)
    return acc, False


print(calcAcc(instructions)[0])

# Part 2

for i, item in enumerate(instructions):
    instruction, value = item
    if instruction == "acc":
        continue
    if instruction == "nop":
        instructions[i] = ("jmp", value)
        acc, terminated = calcAcc(instructions)
    else:
        instructions[i] = ("nop", value)
        acc, terminated = calcAcc(instructions)
    instructions[i] = [instruction, value]
    if terminated:
        print(acc)
        break