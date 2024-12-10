import re
from collections import defaultdict

def find_trailheads(line):
    line_as_string = "".join(line)
    trailheads = re.finditer("0",line_as_string)
    if trailheads:
        return [m.start(0) for m in trailheads]
    else:
        return

def search_directions(row_index,height, position, starting_coords):
    height = int(height)
    if height == 9:
        global complete_trails
        complete_trails += 1
        global endpoint_tracker
        endpoint_tracker[starting_coords].append((row_index,position))
        return 
    #check north
    north_row = row_index - 1
    if data[north_row][position] != "." and int(data[north_row][position]) == height + 1:
        search_directions(north_row,height+1,position,starting_coords)
    #check south
    south_row = row_index + 1
    if data[south_row][position] != "." and int(data[south_row][position]) == height + 1:
        search_directions(south_row,height+1,position,starting_coords)
    #check east
    if data[row_index][position+1] != "." and int(data[row_index][position+1]) == height + 1:
        search_directions(row_index,height+1,position+1,starting_coords)
    #check west
    if data[row_index][position-1] != "." and int(data[row_index][position-1]) == height + 1:
        search_directions(row_index,height+1,position-1,starting_coords)
    return
    

with open("puzzle_input.txt") as f:
    data = [list(line.rstrip()) for line in f]

#pad grid
top_and_bottom_padding = ["." for i in range(len(data[1]))]
data.insert(0,top_and_bottom_padding)
data.append(top_and_bottom_padding)
for line in data:
    line.insert(0,".")
    line.append(".")

endpoint_tracker = defaultdict(list)
complete_trails = 0

for idx,line in enumerate(data):
    trailheads = find_trailheads(line)
    if len(trailheads) > 0:
        for trailhead in trailheads:
            starting_coords = (idx,trailhead)
            search_directions(idx,0,int(trailhead),starting_coords)
           
p2_answer = complete_trails

individual_endpoints = 0
for value in endpoint_tracker.values():
    deduped_endpoints = set(value)
    individual_endpoints += len(deduped_endpoints)

p1_answer = individual_endpoints

print(f"Answer to part 1 is {p1_answer}")
print(f"Answer to part 2 is {p2_answer}")