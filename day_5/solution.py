from collections import defaultdict
from itertools import groupby

def find_middle(update_list):
    middle_index = len(update_list)//2
    return int(update_list[middle_index])

rules = defaultdict(set)

with open("puzzle_page_order.txt") as f:
    rules_data = [(line.rstrip()) for line in f]
    for i in rules_data:
        first,second = i.split("|")
        rules[first].add(second)

with open("puzzle_update.txt") as f:
    update_data = [(line.rstrip()).split(",") for line in f]

invalid_updates = []

for update in update_data:
    for idx,num in enumerate(update):
        valid = True
        rest_of_row = [i for i in update if i != num]
        for i in rest_of_row:
            if i in rules[num]:
                if idx > update.index(i):
                    valid = False
                    invalid_updates.append(update)

invalid_updates = (list(invalid_updates for invalid_updates,_ in groupby(invalid_updates)))
valid_updates = [update for update in update_data if update not in invalid_updates]
p1_answer = sum([find_middle(i) for i in valid_updates])
print(f"Answer to p1 is {p1_answer}")

sorted_pages=[]
for idx,update in enumerate(invalid_updates):
    valid = False
    page = update
    n = len(page)
    for i in range(n-1):
        for j in range(n-i-1):
            if str(page[j+1]) in rules[str(page[j])]:
                page[j], page[j+1] = page[j+1], page[j]
    sorted_pages.append(page)

p2_answer = sum([find_middle(i) for i in sorted_pages])
print(f"Answer to p2 is {p2_answer}")