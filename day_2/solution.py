from itertools import pairwise

def find_differences(report):
    differences = [y - x for x,y in pairwise(report)]
    return differences

def check_all_asc_or_desc(difference_list):
    if all(i < 0 for i in difference_list):
        return True
    elif all(i > 0 for i in difference_list):
        return True
    else:
        return False
    
def check_safety(report_difference_values):
    abs_differences = [abs(i) for i in report_difference_values]
    valid_values_check = all(e in valid_differences for e in abs_differences)
    return valid_values_check

with open("puzzle_input.txt") as f:
    data=[list(map(int,line.split())) for line in f]

valid_differences = [1,2,3]

number_valid_reports = 0
for i in data:
    report_differences = find_differences(i)
    asc_or_desc = check_all_asc_or_desc(report_differences)
    if asc_or_desc:
        check_validity = check_safety(report_differences)
        if check_validity:
            number_valid_reports+=1

print(f"Part 1 answer is {number_valid_reports}")

part_2_valid_reports = 0
for report in data:
    for idx in range(len(report)):
        amended_report = report[:idx] + report[idx+1:]
        report_differences = find_differences(amended_report)
        asc_or_desc = check_all_asc_or_desc(report_differences)
        if asc_or_desc:
            check_validity = check_safety(report_differences)
            if check_validity:
                part_2_valid_reports+=1
                break

print(f"Part 2 answer is {part_2_valid_reports}")