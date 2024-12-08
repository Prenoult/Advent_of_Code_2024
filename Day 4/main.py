with open('./Day 4/input.txt', 'r') as file:
    content = file.read().splitlines()
# part 1
grid = [list(row) for row in content]

def find_word_in_direction(grid, word, x, y, dx, dy):
    rows, cols = len(grid), len(grid[0])
    for i in range(len(word)):
        nx, ny = x + i * dx, y + i * dy
        if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[i]:
          return False
    return True

def count_word_in_grid(grid, word):
    directions = [
        (0,1),    # right
        (0,-1),   # left
        (1,0),    # bottom
        (-1,0),   # top
        (1,1),    # bottom-right
        (-1,1),   # top-right
        (1,-1),   # bottom-left
        (-1,-1)   # top-left
    ]
    count = 0
    rows, cols = len(grid), len(grid[0])

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if find_word_in_direction(grid, word, x, y, dx, dy):
                    count += 1

    return count

print("Part 1: ", count_word_in_grid(grid, "XMAS"))

# part 2
def conditionA(grid, x, y):
  return (grid[x-1][y-1] == "M" and grid[x-1][y+1] == "M" and 
          grid[x+1][y-1] == "S" and grid[x+1][y+1] == "S")

def conditionB(grid, x, y):
  return (grid[x-1][y-1] == "S" and grid[x-1][y+1] == "S" and 
          grid[x+1][y-1] == "M" and grid[x+1][y+1] == "M")

def conditionC(grid, x, y):
  return (grid[x-1][y-1] == "M" and grid[x-1][y+1] == "S" and 
          grid[x+1][y-1] == "M" and grid[x+1][y+1] == "S") 

def conditionD(grid, x, y):
  return (grid[x-1][y-1] == "S" and grid[x-1][y+1] == "M" and 
          grid[x+1][y-1] == "S" and grid[x+1][y+1] == "M") 

def find_xmas(grid):
  rows, cols = len(grid), len(grid[0])
  count = 0

  for x in range(1, rows - 1):
    for y in range(1, cols - 1):
      if (
        grid[x][y] == "A" and 
        (conditionA(grid, x, y) or conditionB(grid, x, y) or 
         conditionC(grid, x, y) or conditionD(grid, x, y))
      ):
         count += 1
  
  return count

print("Part 2: ", find_xmas(grid))

