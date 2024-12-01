import os

# part 1
with open('./Day 1/input.txt', 'r') as file:
    content = file.read().splitlines()

first_numbers = []
second_numbers = []

for line in content:
    if line.strip(): 
        numbers = line.split()
        first_numbers.append(int(numbers[0]))
        second_numbers.append(int(numbers[1]))

first_numbers.sort()
second_numbers.sort()

def calculate_differences (list1, list2):
    return [abs(a - b) for a, b in zip(list1, list2)]

differences = calculate_differences(first_numbers, second_numbers)

# res part 1
print(sum(differences))

# part 2
def calculate_similarity_scores(list1, list2):
    similarity_scores = []
    for num in list1:
        occurrence = list2.count(num)
        similarity_scores.append(num * occurrence)
    return similarity_scores

# res part 2
print(sum(calculate_similarity_scores(first_numbers, second_numbers)))