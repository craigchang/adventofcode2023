# https://adventofcode.com/2023/day/16

UP, LEFT, DOWN, RIGHT = 0,1,2,3
DIRECTIONS = [UP, LEFT, DOWN, RIGHT]

def read_file(filepath):
  with open(filepath, 'r') as f:
    return [l.strip() for l in f.readlines()]

def is_visited_with_direction(grid: list, visited: dict, x: int, y: int, dir: int):
  if (x, y) not in visited:
    visited[(x,y)] = [dir]
  else:
    if dir not in visited[(x,y)]:
      visited[(x,y)].append(dir)
    else:
      return True
  return False

def create_configurations(max_x: int, max_y: int):
  configs = [(0,0,RIGHT),(0,0,DOWN),(max_x-1,0,LEFT),(max_x-1,0,DOWN),(0,max_y-1,RIGHT),(0,max_y-1,UP),(max_x-1,max_y-1,LEFT),(max_x-1,max_y-1,UP)]
  for x in range(0, max_x):
    configs.append((x, 0, DOWN))
    configs.append((x, max_y-1, UP))
  for y in range(0, max_y):
    configs.append((0, y, LEFT))
    configs.append((x, max_y-1, UP))
  return configs

def shoot_new_beam(grid: list, beams: list, visited: dict, max_x: int, max_y: int, beam_x: int, beam_y:int, dir: int):
  while(True):
    if beam_x < 0 or beam_x >= max_x or beam_y < 0 or beam_y >= max_y:
      return
    if grid[beam_y][beam_x] in ['\\', '/', '|', '-'] and is_visited_with_direction(grid, visited, beam_x, beam_y, dir):
      return

    beams[beam_y][beam_x] = '#'

    if grid[beam_y][beam_x] == "\\":
      if dir == UP or dir == DOWN:
        dir = (dir+1) % 4
      elif dir == RIGHT or dir == LEFT:
        dir = (dir-1) % 4
    elif grid[beam_y][beam_x] == "/":
      if dir == UP or dir == DOWN:
        dir = (dir-1) % 4
      elif dir == RIGHT or dir == LEFT:
        dir = (dir+1) % 4
    elif grid[beam_y][beam_x] == "-" and (dir == UP or dir == DOWN):
      shoot_new_beam(grid, beams, visited, max_x, max_y, beam_x+1, beam_y, RIGHT)
      shoot_new_beam(grid, beams, visited, max_x, max_y, beam_x-1, beam_y, LEFT)
      return
    elif grid[beam_y][beam_x] == "|" and (dir == RIGHT or dir == LEFT):
      shoot_new_beam(grid, beams, visited, max_x, max_y, beam_x, beam_y-1, UP)
      shoot_new_beam(grid, beams, visited, max_x, max_y, beam_x, beam_y+1, DOWN)
      return
    
    if dir == RIGHT:
      beam_x += 1
    elif dir == LEFT:
      beam_x -= 1
    elif dir == UP:
      beam_y -= 1
    elif dir == DOWN:
      beam_y += 1

def part1():
  grid = read_file("day16/input.txt")
  max_x, max_y = len(grid[0]), len(grid)
  beams = [['.' for x in range(max_x)] for y in range(max_y)]
  shoot_new_beam(grid, beams, dict(), max_x, max_y, 0, 0, RIGHT)
  print("Part 1:", sum([beams[y].count('#') for y in range(max_y)]))

def part2():
  grid = read_file("day16/input.txt")
  max_x, max_y = len(grid[0]), len(grid)
  beams = [['.' for x in range(max_x)] for y in range(max_y)]
  energized = []
  for config in create_configurations(max_x, max_y):
    x,y,d = config
    beams = [['.' for x in range(max_x)] for y in range(max_y)]
    shoot_new_beam(grid, beams, dict(), max_x, max_y, x, y, d)
    energized.append(sum([beams[y].count('#') for y in range(max_y)]))
  print("Part 2:", max(energized))
      
part1()
part2()