# https://adventofcode.com/2023/day/3

import re

def read_file():
    with open("day3/input.txt", "r") as f:
        return [l.strip() for l in f.readlines()]

def is_symbol_nearby(x: int, y: int, max_x: int, max_y: int, lines: list):
    return x > 0 and x < max_x and y > 0 and y < max_y and re.match("[^0-9.]", lines[y][x])

def main():
    lines = read_file()
    max_x, max_y, sum_part_nums, gear_dict = len(lines[0]), len(lines), 0, dict()

    for y in range(max_y): # for each line
        num_coord, num_str = [], ""
        for x in range(max_x):
            if re.match("[0-9]", lines[y][x]):
                num_coord.append((x,y))
                num_str += lines[y][x]
            if re.match("[^0-9]", lines[y][x]) or x == max_x - 1: # part num ends or eol
                for px,py in num_coord: # for each coord in part num, check all adjacent symbols
                    for sx, sy in [(px-1,py), (px+1, py), (px, py-1), (px, py+1), (px-1, py-1), (px-1, py+1), (px+1, py-1), (px+1, py+1)]:
                        if is_symbol_nearby(sx, sy, max_x, max_y, lines):
                            if lines[sy][sx] == "*": # if gear found, store parts near this gear in dict
                                if (sx,sy) not in gear_dict:
                                    gear_dict[(sx,sy)] = []
                                gear_dict[(sx,sy)].append(int(num_str))
                            sum_part_nums += int(num_str)
                            break
                    else:
                        continue
                    break
                num_coord, num_str = [], ""

    sum_gear_ratio = sum([v[0] * v[1] for v in gear_dict.values() if len(v) == 2])
    
    print("Part 1: ", sum_part_nums)
    print("Part 2: ", sum_gear_ratio)
        
main()