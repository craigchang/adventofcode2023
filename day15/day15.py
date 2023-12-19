# https://adventofcode.com/2023/day/15

def read_file():
  with open("day15/input.txt", "r") as f:
    return f.readline().strip().split(",")

def find_hash(s: str):
  curr = 0
  for c in s:
    curr = ((curr + ord(c)) * 17) % 256
  return curr

def remove_from_box(boxes: list, s: str):
  label = s.split("-")[0]
  box = find_hash(label)
  for slot in boxes[box]:
    if label in slot:
      boxes[box].remove(slot)
      break

def update_box(boxes: list, s: str):
  label, focal, = s.split("=")
  box = find_hash(label)
  ct = 0
  for slot in boxes[box]:
    if label in slot:
      boxes[box][ct] = label + " " + focal
      break
    ct += 1
  else:
    boxes[box].append(label + " " + focal)

def calc_focusing_power(boxes: list):
  total = 0
  for box in range(len(boxes)):
    for slot in range(len(boxes[box])):
      box_num, focal = boxes[box][slot].split()
      total += (box+1) * (slot+1) * int(focal)
  return total

def part1():
  seq = read_file()
  print("Part 1:", sum([find_hash(s) for s in seq]))

def part2():
  seq = read_file()
  boxes = [[] for i in range(256)]

  for s in seq:
    if "=" in s:
      update_box(boxes, s)
    elif "-" in s:
      remove_from_box(boxes, s)

  print("Part 2:", calc_focusing_power(boxes))

part1()
part2()