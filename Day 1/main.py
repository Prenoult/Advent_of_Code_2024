import os

# part 1
with open('./Day 1/input.txt', 'r') as file:
    content = file.read().splitlines()

first_numbers = sorted([int(line.split()[0]) for line in content if line.strip()]) 
second_numbers = sorted([int(line.split()[1]) for line in content if line.strip()]) 

def calculate_differences (list1, list2):
    return [abs(a - b) for a, b in zip(list1, list2)]

differences = calculate_differences(first_numbers, second_numbers)

print("Part 1: ", sum(differences))

# part 2
def calculate_similarity_scores(list1, list2):
    similarity_scores = []
    for num in list1:
        occurrence = list2.count(num)
        similarity_scores.append(num * occurrence)
    return similarity_scores

print("Part 2: ", sum(calculate_similarity_scores(first_numbers, second_numbers)))