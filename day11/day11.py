# https://adventofcode.com/2023/day/11

import math

def read_file(filepath):
  with open(filepath, "r") as f:
    grid = []
    for l in f.readlines():
      grid.append(list(l.strip()))
    return grid

def add_empty_rows_and_cols(grid: list, max_x: int, max_y: int, factor: int):
  # find where to add cols
  new_cols = []
  for x in range(max_x): # loop by col
    no_galax = True
    for y in range(max_y): # check each in col
      if grid[y][x] == "#":
        no_galax = False
    if no_galax:
      new_cols.append(x)

  # find where to add rows
  new_rows = []
  for y in range(max_y): # loop by row
    no_galax = True
    for x in range(max_x): # check each in row
      if grid[y][x] == "#":
        no_galax = False
    if no_galax:
      new_rows.append(y)

  # add additional cols
  offset = 0
  for col in new_cols:
    for y in range(max_y):
      for f in range(factor-1):
        grid[y].insert(col+offset, ".")
    offset += (factor-1)
  
  max_x = len(grid[0]) # re-calc max x grid

  # add additional rows
  offset = 0
  for row in new_rows:
    for f in range(factor-1):
      grid.insert(row+offset, ["."] * max_x)
    offset += (factor-1)
  
  return

def calc_sum_paths(grid: list, max_x: int, max_y: int):
  distances = []
  galaxies = [(x,y) for y in range(max_y) for x in range(max_x) if grid[y][x] == "#"]
  
  for i in range(len(galaxies)):
    for j in range(i+1,len(galaxies)):
      (g1x, g1y), (g2x, g2y) = galaxies[i], galaxies[j]
      distances.append(abs(g2y - g1y) + abs(g2x - g1x))
  return distances

def part1(filename):
  grid = read_file(filename)
  add_empty_rows_and_cols(grid, len(grid[0]), len(grid), 2)
  dists = calc_sum_paths(grid, len(grid[0]), len(grid))
  print(sum(dists))

def part2(filename):
  grid = read_file(filename)
  add_empty_rows_and_cols(grid, len(grid[0]), len(grid), 1)
  distances_1 = calc_sum_paths(grid, len(grid[0]), len(grid))

  grid = read_file(filename)
  add_empty_rows_and_cols(grid, len(grid[0]), len(grid), 10)
  distances_10 = calc_sum_paths(grid, len(grid[0]), len(grid))
  sum_paths = sum(distances_10)

  diffs = [distances_10[i] - distances_1[i] for i in range(len(distances_1))] # diff between 10 and 100

  # use diff to extrapolate other measurements by factor of 10, up to 1000000
  for i in [100, 1000, 10000, 100000, 1000000]:
    diffs = [diffs[i] * 10 for i in range(len(diffs))]
    sum_paths = sum_paths + sum(diffs)

  print(sum_paths)

part1("day11/input.txt")
part2("day11/input.txt")

# 82000210 too low