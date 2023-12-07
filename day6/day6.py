# https://adventofcode.com/2023/day/6

import re
import math

def read_file1():
  with open("day6/input.txt", "r") as f:
    rec_times = list(map(int, (re.findall("Time: (.*)", f.readline().strip())[0]).split()))
    rec_distances = list(map(int, (re.findall("Distance: (.*)", f.readline().strip())[0]).split()))
  return rec_times, rec_distances

def read_file2():
  with open("day6/input.txt", "r") as f:
    rec_times = [int("".join(re.findall("Time: (.*)", f.readline().strip())[0].split()))]
    rec_distances = [int("".join(re.findall("Distance: (.*)", f.readline().strip())[0].split()))]
  return rec_times, rec_distances

def calculate_wins(rec_times, rec_distances, wins):
  for i in range(len(rec_times)):
    rec_time = rec_times[i]
    for hold in range(rec_time + 1):
      if rec_distances[i] < (rec_time - hold) * hold:
        wins[i] += 1
  return math.prod(wins)

def part1():
  rec_times, rec_distances = read_file1()
  wins = [0] * len(rec_times)
  print(calculate_wins(rec_times, rec_distances, wins))

def part2():
  rec_times, rec_distances = read_file2()
  wins = [0] * len(rec_times)
  print(calculate_wins(rec_times, rec_distances, wins))

part1()
part2()