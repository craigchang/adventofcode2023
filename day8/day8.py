# https://adventofcode.com/2023/day/8

import re
import math

def read_file(filepath):
  with open(filepath, "r") as f:
    nodes = dict()
    directions = f.readline().strip()
    f.readline() # empty line
    while True:
      line = f.readline().strip()
      if not line:
        break
      start, next_l, next_r = re.findall("([A-Za-z0-9]{3})", line)
      nodes[start] = (next_l, next_r)
    return directions, nodes

def make_step(node: str, dir: int, steps: int, directions: str, nodes: dict):
  if dir == len(directions): # repeat directions if needed
    dir = 0
  next = nodes[node][1] if directions[dir] == 'R' else nodes[node][0]
  return dir, next, steps+1
  
def part1():
  directions, nodes = read_file("day8/input.txt")
  current, dir, steps = 'AAA', 0, 0

  while current != 'ZZZ':
    dir, current, steps = make_step(current, dir, steps, directions, nodes)
    dir += 1

  print("Part 1:", steps)

def part2():
  directions, nodes = read_file("day8/input.txt")
  dir = 0
  paths = [[start, 0] for start,dirs in nodes.items() if start.endswith("A")] # all starting locations, store as [curr, steps]

  while True:
    for p in range(len(paths)):
      curr, steps = paths[p]
      if curr.endswith('Z'): # if path reached its end, skip
        continue
      dir, paths[p][0], paths[p][1] = make_step(curr, dir, steps, directions, nodes)
    dir += 1
    if all([paths[p][0].endswith('Z') for p in range(len(paths))]): # if all paths ended
      break
    
  print("Part 2:", math.lcm(*[paths[i][1] for i in range(len(paths))])) # find lcm of all steps in each path

part1()
part2()