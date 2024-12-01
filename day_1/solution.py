with open("puzzle_input.txt") as f:
    list_1=[]
    list_2=[]

    for line in f:
        line_list=line.split()
        list_1.append(int(line_list[0]))
        list_2.append(int(line_list[-1]))

sorted_list_1 = sorted(list_1)
sorted_list_2 = sorted(list_2)

zipped_lists = list(zip(sorted_list_1,sorted_list_2))

differences = []
for pair in zipped_lists:
    difference = abs(pair[0]-pair[1])
    differences.append(difference)

p1_answer = sum(differences)
print(p1_answer)
