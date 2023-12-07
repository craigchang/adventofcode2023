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
  mini, maxi = 0, 0
  for i in range(len(rec_times)):
    rec_time = rec_times[i]
    for hold in range(rec_time + 1): # find min hold speed that beats record
      if rec_distances[i] < (rec_time - hold) * hold:
        mini = hold
        break
    for hold in range(rec_time + 1, 0, -1): # find max hold speed that beats record
      if rec_distances[i] < (rec_time - hold) * hold:
        maxi = hold
        break
    wins[i] = maxi - mini + 1 # calc min max diff for num wins
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