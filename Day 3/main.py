import re

# part 1
with open('./Day 3/input.txt', 'r') as file:
    content = file.read()

def get_multiplication_tuples(text):
  pattern = r"mul\((\d+),(\d+)\)"
  return [[int(a), int(b)] for a,b in re.findall(pattern, text)]

def get_product_from_multiplication_tuples(lst):
   return [a*b for a,b in lst]

print(
  "Part 1:",
  sum(get_product_from_multiplication_tuples(get_multiplication_tuples(content)))
) 

# part 2
def get_eligible_multiplication_tuples(text):
  pattern = r"(do\(\)|don't\(\))|mul\((\d+),(\d+)\)"
  enabled = True
  eligible_tuples = []

  for match in re.finditer(pattern, text):
    command = match.group(0)

    if command == "do()":
      enabled = True
    elif command == "don't()":
      enabled = False
    elif enabled and command.startswith("mul"):
      x,y = int(match.group(2)), int(match.group(3))
      eligible_tuples.append((x,y))

  return eligible_tuples

print(
  "Part 2:",
  sum(get_product_from_multiplication_tuples(get_eligible_multiplication_tuples(content)))
)