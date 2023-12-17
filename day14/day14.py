# https://adventofcode.com/2023/day/14

def read_file(filepath):
  with open(filepath, "r") as f:
    return [list(l.strip()) for l in f.readlines()]

def tilt_north(grid: list, max_x: int, max_y: int):
  for x in range(max_x):
    round_rocks = 0
    prev_cube_rock = 0
    for y in range(max_y+1):
      if y == max_y or grid[y][x] == "#":
        for y_new in range(prev_cube_rock, y, 1):
          if round_rocks > 0:
            grid[y_new][x] = "O"
            round_rocks -= 1
          else:
            grid[y_new][x] = "."
        prev_cube_rock = y+1
      elif grid[y][x] == "O":
        round_rocks += 1

def tilt_south(grid: list, max_x: int, max_y: int):
  for x in range(max_x):
    round_rocks = 0
    prev_cube_rock = 0
    for y in range(max_y+1):
      if y == max_y or grid[y][x] == "#":
        for y_new in range(y-1, prev_cube_rock-1, -1):
          if round_rocks > 0:
            grid[y_new][x] = "O"
            round_rocks -= 1
          else:
            grid[y_new][x] = "."
        prev_cube_rock = y+1
      elif grid[y][x] == "O":
        round_rocks += 1

def tilt_west(grid: list, max_x: int, max_y: int):
  for y in range(max_y):
    round_rocks = 0
    prev_cube_rock = 0
    for x in range(max_x+1):
      if x == max_x or grid[y][x] == "#":
        for x_new in range(prev_cube_rock, x, 1):
          if round_rocks > 0:
            grid[y][x_new] = "O"
            round_rocks -= 1
          else:
            grid[y][x_new] = "."
        prev_cube_rock = x + 1
      elif grid[y][x] == "O":
        round_rocks += 1

def tilt_east(grid: list, max_x: int, max_y: int):
  for y in range(max_y):
    round_rocks = 0
    prev_cube_rock = 0
    for x in range(max_x+1):
      if x == max_x or grid[y][x] == "#":
        for x_new in range(x-1, prev_cube_rock-1, -1):
          if round_rocks > 0:
            grid[y][x_new] = "O"
            round_rocks -= 1
          else:
            grid[y][x_new] = "."
        prev_cube_rock = x + 1
      elif grid[y][x] == "O":
        round_rocks += 1

def calc_load_level(grid: list, max_y: int):
  total_load, load_level = 0, max_y
  for y in range(max_y):
    total_load += grid[y].count('O') * load_level
    load_level -= 1
  return total_load

def part1():
  grid = read_file("day14/input.txt")
  max_x, max_y = len(grid[0]), len(grid)
  tilt_north(grid, max_x, max_y)
  print("Part 1:", calc_load_level(grid, max_y))

def part2():
  grid = read_file("day14/input.txt")
  max_x, max_y, results, st = len(grid[0]), len(grid), [], 0

  while(True):
    tilt_north(grid, max_x, max_y)
    n = calc_load_level(grid, max_y)
    tilt_west(grid, max_x, max_y)
    w = calc_load_level(grid, max_y)
    tilt_south(grid, max_x, max_y)
    s = calc_load_level(grid, max_y)
    tilt_east(grid, max_x, max_y)
    e = calc_load_level(grid, max_y)

    if (n,w,s,e) in results:
      st = results.index((n,w,s,e))
      break
    results.append((n,w,s,e))

  results = results[st:len(results)]
  print("Part 2:", results[(1000000000 - st) % (len(results)) - 1][3])

part1()
part2()