# https://adventofcode.com/2023/day/12

def read_file(filepath):
  with open(filepath, "r") as f:
    grids, grid = [], [] 
    for l in f.readlines():
      if not l.strip():
        grids.append(grid)
        grid = []
        continue
      grid.append(list(l.strip()))
    grids.append(grid)
    return grids

def is_vertical_reflection(grid: list, max_x: int, max_y: int, x: int):
  x1, x2 = x, x+1
  while x1 >= 0 and x2 < max_x:  # check pairs of cols
    for y in range(max_y):
      if grid[y][x1] != grid[y][x2]:
        return False
    x1 -= 1
    x2 += 1
  return True

def check_vertical(grid: list, max_x: int, max_y: int, exclude: int=-1):
  for x in range(max_x-1):
    if x == exclude:
      continue
    for y in range(max_y):
      if grid[y][x] != grid[y][x+1]:
        break
    else:
      if is_vertical_reflection(grid, max_x, max_y, x):
        return x + 1
  return 0

def is_horizontal_reflection(grid: list, max_y: int, y: int):
  y1, y2 = y, y+1
  while y1 >= 0 and y2 < max_y: # check pairs of rows
    if grid[y1] != grid[y2]:
      return 0
    y1 -= 1
    y2 += 1
  return True

def check_horizontal(grid: list, max_y: int, exclude: int=-1):
  for y in range(max_y-1):
    if y == exclude:
      continue
    elif grid[y] == grid[y+1] and is_horizontal_reflection(grid, max_y, y):
      return y + 1
  return 0

def find_reflection(grid: list, max_x: int, max_y: int, exclude_x: int=-1, exclude_y:int=-1):
  v = check_vertical(grid, max_x, max_y, exclude_x-1)
  h = check_horizontal(grid, max_y, exclude_y-1) if v <= 0 else 0
  return (v,h)

def main():
  grids = read_file("day13/input.txt")
  total, previous = 0, []

  for grid in grids:
    v,h = find_reflection(grid, len(grid[0]), len(grid))
    previous.append((v,h))
    total += h * 100 if v == 0 else v

  print("Part 1:", total)

  total, grid_num = 0, 0
  for grid in grids:
    max_x, max_y = len(grid[0]), len(grid)
    found = False
    for y in range(max_y):
      for x in range(max_x):
        grid_copy = [y[:] for y in grid]
        grid_copy[y][x] = "#" if grid_copy[y][x] == "." else "."
        prev_xr, prev_yr = previous[grid_num]
        v,h = find_reflection(grid_copy, max_x, max_y, prev_xr, prev_yr)
        if (v,h) != (prev_xr, prev_yr) and (v,h) != (0,0): # if found different
          total += h * 100 if v == 0 else v
          found = True
          break
      if found:
        break
    grid_num += 1

  print("Part 2:", total)

main()