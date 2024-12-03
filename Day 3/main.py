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