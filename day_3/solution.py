import re
import numpy as np

with open("puzzle_input.txt", 'r') as file:
    data = file.read().replace('\n', ' ')

sets_of_muls = re.findall(r'mul\(\d+,\d+\)',data)
numbers_to_mul = [(re.search(r'\(\d+,\d+\)',i)[0]) for i in sets_of_muls]

tuple_list = []
for i in numbers_to_mul:
    x = int((re.findall(r'\d+',i))[0])
    y = int((re.findall(r'\d+',i))[1])
    tuple_list.append((x,y))

p1_answer = sum([np.prod(i) for i in tuple_list])

print(f"Answer to part 1 is {p1_answer}")


part_2_tuple_list_strings =[]
cleaned_data = re.findall(r"mul\(\d+.\d+\)|do\(\)|don't\(\)",data)
enabled=True
for i in cleaned_data:
    if i == "do()":
        enabled = True
    elif i == "don't()":
        enabled = False
    else:
        if enabled:
            part_2_tuple_list_strings.append(i)

part_2_tuple_list = []
for i in part_2_tuple_list_strings:
    x = int((re.findall(r'\d+',i))[0])
    y = int((re.findall(r'\d+',i))[1])
    part_2_tuple_list.append((x,y))

p2_answer = sum([np.prod(i) for i in part_2_tuple_list])

print(f"Answer to part 1 is {p2_answer}")

