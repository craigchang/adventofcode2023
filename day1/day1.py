# https://adventofcode.com/2023/day/1

import re

num_dict = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9'
}

def numToDigits(num: str):
  return num_dict[num] if not num.isnumeric() else num

def readFile():
  with open("day1/input.txt", "r") as f:
    return f.readlines()

def part1():
  calibration_values = 0
  for l in readFile():
    matched = re.findall("\d", l)
    calibration_values += int(matched[0] + matched[-1])
  print(calibration_values)

def part2():
  calibration_values = 0
  for l in readFile():
    matched = re.findall("(?=(\d|one|two|three|four|five|six|seven|eight|nine))", l)
    calibration_values += int(numToDigits(matched[0]) + numToDigits(matched[-1]))
  print(calibration_values)

part1()
part2()