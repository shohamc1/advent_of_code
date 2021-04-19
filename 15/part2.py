input_string = "1,17,0,10,18,11,6"

numbers = {int(i):index 
        for index,i in enumerate(input_string.split(","),start=1)}

n = len(numbers)+1
number_to_be_spoken = 0
all_nums = [int(i) for i in input_string.split(",")]

while n<30000000:
    all_nums.append(number_to_be_spoken)
    if number_to_be_spoken in numbers.keys():
        next_number = n - numbers[number_to_be_spoken]
        numbers[number_to_be_spoken] = n
        number_to_be_spoken = next_number
    else:
        numbers[number_to_be_spoken] = n
        number_to_be_spoken = 0
    n+=1

print(number_to_be_spoken)