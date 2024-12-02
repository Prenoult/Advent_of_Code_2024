import os

# part 1
with open('./Day 2/input.txt', 'r') as file:
    content = file.read().splitlines()

def is_ascending(list):
    return list == sorted(list)

def is_descending(list):
    return list == sorted(list, reverse=True)

def is_difference_ok(list, min_diff, max_diff):
    return all(min_diff <= abs(list[i] - list[i + 1]) <= max_diff for i in range(len(list) - 1))

def is_report_safe(report):
    return (is_ascending(report) | is_descending(report)) & is_difference_ok(report, 1, 3)

def count_safe_reports(list):
    reports = []
    for line in list:
        numbers = [int(number) for number in line.split()] 
        reports.append(is_report_safe(numbers))
    return reports.count(True)

print("Part 1: ", count_safe_reports(content))
