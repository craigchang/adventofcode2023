# https://adventofcode.com/2023/day/10

VALID_NORTH = ["|", "7", "F"]
VALID_WEST = ["-", "L", "F"]
VALID_EAST = ["-", "J", "7"]
VALID_SOUTH = ["|", "L", "J"]

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3

def read_file(filepath):
  with open(filepath, "r") as f:
    grid = []
    for l in f.readlines():
      grid.append(list(l.strip()))
    return grid

def get_S_coords(grid: list):
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] == 'S':
        return (x,y)

def get_S_pipe(grid: list, sX: int, sY: int, max_x: int, max_y: int):
  if sX > 0 and grid[sY][sX-1] in VALID_WEST and sX < max_x and grid[sY][sX+1] in VALID_EAST:
    grid[sY][sX] = "-"
    return [LEFT, RIGHT]
  elif sY > 0 and grid[sY+1][sX] in VALID_SOUTH and sY < max_y and grid[sY-1][sX] in VALID_NORTH:
    grid[sY][sX] = "|"
    return [DOWN, UP]
  elif sX > 0 and grid[sY][sX-1] in VALID_WEST and sY > 0 and grid[sY+1][sX] in VALID_SOUTH:
    grid[sY][sX] = "F"
    return [RIGHT, DOWN]
  elif sX < max_x and grid[sY][sX+1] in VALID_EAST and sY > 0 and grid[sY+1][sX] in VALID_SOUTH:
    grid[sY][sX] = "7"
    return [LEFT, DOWN]
  elif sX > 0 and grid[sY][sX-1] in VALID_WEST and sY < max_y and grid[sY-1][sX] in VALID_NORTH:
    grid[sY][sX] = "L"
    return [LEFT, UP]
  elif sX > 0 and grid[sY][sX-1] in VALID_WEST and sY < max_y and grid[sY-1][sX] in VALID_NORTH:
    grid[sY][sX] = "J"
    return [RIGHT, UP]

def move(grid: list, next_dir: int, curr_pos: list, steps: int):
  curr_pos_x, curr_pos_y = curr_pos
  if next_dir == UP:
    next = grid[curr_pos_y-1][curr_pos_x]
    if next == "|":   next_dir = UP
    elif next == "7": next_dir = LEFT
    elif next == "F": next_dir = RIGHT
    curr_pos_y -= 1
  elif next_dir == DOWN:
    next = grid[curr_pos_y+1][curr_pos_x]
    if next == "|":   next_dir = DOWN
    elif next == "L": next_dir = RIGHT
    elif next == "J": next_dir = LEFT
    curr_pos_y += 1
  elif next_dir == RIGHT:
    next = grid[curr_pos_y][curr_pos_x+1]
    if next == "-":   next_dir = RIGHT
    elif next == "J": next_dir = UP
    elif next == "7": next_dir = DOWN
    curr_pos_x += 1
  elif next_dir == LEFT:
    next = grid[curr_pos_y][curr_pos_x-1]
    if next == "-":   next_dir = LEFT
    elif next == "L": next_dir = UP
    elif next == "F": next_dir = DOWN
    curr_pos_x -= 1
  return (curr_pos_x, curr_pos_y), next_dir, steps+1

def calc_enclosed_tiles(grid: list, max_x: int, max_y: int, loop_coords: set):
  count_tiles = 0
  for y in range(max_y):
    is_outside = True
    for x in range(max_x):
      if (x,y) not in loop_coords:
        grid[y][x] = "O" if is_outside else "I"
        if grid[y][x] == "I":
          count_tiles += 1
      elif (x,y) in loop_coords and (grid[y][x] == "|" or grid[y][x] == "J" or grid[y][x] == "L"):
        is_outside = not is_outside
  return count_tiles

def calc_steps(grid: list, max_x: int, max_y: int, start_pos: tuple, loop_coords: set):
  curr_pos1, curr_pos2 = start_pos, start_pos
  next_dir1, next_dir2 = get_S_pipe(grid, start_pos[0], start_pos[1], max_x, max_y)
  steps1, steps2 = 0, 0

  while True:
    curr_pos1, next_dir1, steps1 = move(grid, next_dir1, curr_pos1, steps1)
    curr_pos2, next_dir2, steps2 = move(grid, next_dir2, curr_pos2, steps2)
    loop_coords.add(curr_pos1)
    loop_coords.add(curr_pos2)
    if curr_pos1 == curr_pos2:
      break
  
  return steps1

def main():
  grid = read_file("day10/input.txt")
  start_pos = get_S_coords(grid)
  max_x, max_y = len(grid[0]), len(grid)
  loop_coords = set(start_pos)

  print("Part 1:", calc_steps(grid, max_x, max_y, start_pos, loop_coords))
  print("Part 2:", calc_enclosed_tiles(grid, max_x, max_y, loop_coords))

main()