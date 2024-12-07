import re

with open("example_input.txt") as f:
    data = [(line.rstrip()) for line in f]

direction_change_dict = {"^":">",">":"v","v":"<","<":"^"}
obstacle_positions = []


def find_start_position(grid):
    for idx,i in enumerate(grid):
        if re.search(r"\^",i):
            row = idx
            col = i.index("^")
    return row, col

def check_if_obstacle(row,col,direction):
    if direction == "^":
        obstacle_row = row-1
        obstacle_col = col
    elif direction == ">":
        obstacle_row = row
        obstacle_col = col +1
    elif direction == "v":
        obstacle_row = row + 1
        obstacle_col = col
    else:
        obstacle_row = row
        obstacle_col = col - 1
    
    #check if next square is in or out of bounds
    if obstacle_row < 0 or obstacle_row > len(data) -1 or obstacle_col < 0  or obstacle_col > len(data) - 1:
        bounds = False
    else:
        bounds = True

    if bounds == True:
        if data[obstacle_row][obstacle_col] == "#":
            obstacle_positions.append((obstacle_row,obstacle_col))
            return "obstacle"
        else:
            return "no obstacle"
    else:
        return "out of bounds"

def walk(row,col,direction):
    if direction == "^":
        new_row = row-1
        new_col = col
    elif direction == ">":
        new_row = row
        new_col = col +1
    elif direction == "v":
        new_row = row + 1
        new_col = col
    else:
        new_row = row
        new_col = col - 1
    
    
    return new_row,new_col

def rotate(direction):
    new_direction = direction_change_dict[direction]
    return new_direction

grid_size = len(data)

starting_row, starting_col = find_start_position(data)
start_direction = "^"

steps_taken = 0

guarding = True

squares_covered = []

while guarding == True:
    if steps_taken == 0:
        current_row,current_col = walk(starting_row,starting_col,start_direction)
        current_direction = start_direction
        steps_taken +=1
        squares_covered.append((current_row,current_col))
    else:
        if check_if_obstacle(current_row,current_col,current_direction) == "no obstacle":
            current_row, current_col = walk(current_row,current_col,current_direction)
            steps_taken +=1
            squares_covered.append((current_row,current_col))
        elif check_if_obstacle(current_row,current_col,current_direction) == "obstacle":
            current_direction = rotate(current_direction)
        else: 
            guarding = False

distinct_squares = set(squares_covered)
p1_answer = len(distinct_squares)
print(f"Answer to part 1 is {p1_answer}")

obstacle_positions = list(set(obstacle_positions))

possible_square = True


