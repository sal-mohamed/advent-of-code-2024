from collections import Counter

with open("puzzle_input.txt") as f:
    list_1=[]
    list_2=[]

    for line in f:
        line_list=line.split()
        list_1.append(int(line_list[0]))
        list_2.append(int(line_list[-1]))

zipped_lists = list(zip(sorted(list_1),sorted(list_2)))

differences = []
for pair in zipped_lists:
    difference = abs(pair[0]-pair[1])
    differences.append(difference)

p1_answer = sum(differences)
print(f"Answer to part 1 is: {p1_answer}")

similarity_scores = []
for i in list_1:
    similarity_score = i*Counter(list_2)[i]
    similarity_scores.append(similarity_score)

p2_answer = sum(similarity_scores)
print(f"Answer to part 2 is: {p2_answer}")