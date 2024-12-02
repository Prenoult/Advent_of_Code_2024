# part 1
with open('./Day 2/input.txt', 'r') as file:
    content = file.read().splitlines()

def is_ascending(lst):
    return lst == sorted(lst)

def is_descending(lst):
    return lst == sorted(lst, reverse=True)

def is_difference_ok(lst, min_diff, max_diff):
    return all(min_diff <= abs(lst[i] - lst[i + 1]) <= max_diff for i in range(len(lst) - 1))

def is_report_safe(report):
    return (is_ascending(report) or is_descending(report)) and is_difference_ok(report, 1, 3)

def count_safe_reports(lst):
    safe_reports = []
    for line in lst:
        report = [int(number) for number in line.split()] 
        if is_report_safe(report): 
            safe_reports.append(report)
    return len(safe_reports)

print("Part 1: ", count_safe_reports(content))

# part 2
def get_sub_lsts(lst):
    return [lst[:i] + lst[i+1:] for i in range(len(lst))]

def count_safe_reports_with_tolerance(lst):
    safe_reports = []
    for line in lst:
        report = [int(number) for number in line.split()]
        if not is_report_safe(report):
            for sub_lst in get_sub_lsts(report):
                if is_report_safe(sub_lst):
                    safe_reports.append(report)
                    break
        else:
            safe_reports.append(report)
    return len(safe_reports)

print("Part 2: ", count_safe_reports_with_tolerance(content))