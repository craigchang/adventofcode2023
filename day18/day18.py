# https://adventofcode.com/2023/day/18

import matplotlib.pyplot as plt

def print_map(dig_list):
  xs = [pt[0] for pt in dig_list]
  ys = [pt[1] for pt in dig_list]  
  plt.plot(xs, ys)
  plt.show()

def read_file(filepath: str):
  with open(filepath, 'r') as f:
    plan = []
    for l in f.readlines():
      dir, m, color = l.strip().split(" ")
      plan.append((dir, int(m), color.replace('(', '').replace(')', '').replace('#', '')))
    return plan

def shoelace_area(dig_list: list[tuple[int,int]]) -> int:
  area = 0
  for i in range(len(dig_list) - 1):
    x0,y0 = dig_list[i]
    x1,y1 = dig_list[i+1]
    area += x0*y1 - x1*y0
  return .5 * area

def perimeter_length(dig_list: list[tuple[int,int]]) -> int:
    total = 0
    for i in range(len(dig_list)-1):
      x,y = dig_list[i]
      i1 = (i+1) % len(dig_list)
      total += abs(dig_list[i1][0]-x) + abs(dig_list[i1][1]-y)
    return total

def picks_area(area: int, parameter: int) -> int:
  return area - (parameter // 2) + 1

def part1():
  plan = read_file("day18/input.txt")
  x, y = 0,0
  dig_list = [(0,0)]
  for d,m,c in plan: 
    if d == "R":
      x += m
    elif d == "L":
      x -= m
    elif d == "U":
      y += m
    elif d == "D":
      y -= m
    dig_list.append((x,y))
  area = abs(shoelace_area(dig_list))
  perim = perimeter_length(dig_list)
  print("Part 1:", picks_area(area, perim) + perim)

def part2():
  plan = read_file("day18/input.txt")
  x, y = 0,0
  dig_list = [(0,0)]
  for d,m,c in plan: 
    m = int(c[0:5], 16)
    d = int(c[5])
    if d == 0: # R
      x += m
    elif d == 2: # L
      x -= m
    elif d == 1: # D
      y += m
    elif d == 3: # U
      y -= m
    dig_list.append((x,y))
  area = abs(shoelace_area(dig_list))
  perim = perimeter_length(dig_list)
  print("Part 2:", picks_area(area, perim) + perim)

part1()
part2()

