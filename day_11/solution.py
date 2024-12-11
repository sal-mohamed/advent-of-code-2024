from collections import defaultdict

def blink(stones):
    updated_stones = defaultdict(int)
    for stone, count in stones.items():
        if stone == 0:
            updated_stones[1] += count
        elif len(str(stone)) % 2 == 0:
            mid_point = int(len(str(stone)) /2)
            left_stone = str(stone)[:mid_point]
            right_stone = str(stone)[mid_point:]
            updated_stones[int(left_stone)] += count
            updated_stones[int(right_stone)] += count
        else:
            updated_stones[stone*2024] += count
    return updated_stones

with open("puzzle_input.txt") as f:
    data = f.read().split(" ")
data = [int(i) for i in data]
stones = {stone: 1 for stone in data}

p1_stones = stones
for i in range(25):
    p1_stones = blink(p1_stones)

p1_answer = sum(p1_stones.values())
print(f"Answer to part 1 is {p1_answer}")

p2_stones = stones
for i in range(75):
    p2_stones = blink(p2_stones)

p2_answer = sum(p2_stones.values())
print(f"Answer to part 1 is {p2_answer}")
