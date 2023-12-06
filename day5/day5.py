# https://adventofcode.com/2023/day/5

import re

maps = dict()

def read_map(f: any):
  map_lines = []
  for l in f:
    if not l.strip():
      return map_lines
    map_lines += [[int(i) for i in l.strip().split()]]
  return map_lines

def read_file(part1: bool):
  with open("day5/input.txt", "r") as f:
    seeds, pairs = [], []
    if part1:
      seeds = list(map(int, re.findall("seeds: (.*)", f.readline())[0].split()))
    else:
      pairs = re.findall("(\d+) (\d+)", f.readline())
    
    for l in f:
      if l.strip() == "":
        continue
      if (l.startswith("seed-to-soil map:")):
        maps['seed_to_soil'] = read_map(f)
      if (l.startswith("soil-to-fertilizer map:")):
        maps['soil_to_fert'] = read_map(f)
      if (l.startswith("fertilizer-to-water map:")):
        maps['fert_to_water'] = read_map(f)
      if (l.startswith("water-to-light map:")):
        maps['water_to_light'] = read_map(f)
      if (l.startswith("light-to-temperature map:")):
        maps['light_to_temp'] = read_map(f)
      if (l.startswith("temperature-to-humidity map:")):
        maps['temp_to_hum'] = read_map(f)
      if (l.startswith("humidity-to-location map:")):
        maps['hum_to_loc'] = read_map(f)
  return seeds, pairs

def calc_map(source: int, mapping: list):
  for m in mapping:
    d, s, r = m
    if s <= source and source <= s+r-1:
      return d + (source - s)
  return source

def calc_map_rev(source: int, mapping: list):
  for m in mapping:
    s, d, r = m
    if s <= source and source <= s+r-1:
      return d + (source - s)
  return source

def calc_seed_to_loc(seed: int):
  soil = calc_map(seed, maps['seed_to_soil'])
  fert = calc_map(soil, maps['soil_to_fert'])
  water = calc_map(fert, maps['fert_to_water'])
  light = calc_map(water, maps['water_to_light'])
  temp = calc_map(light, maps['light_to_temp'])
  hum = calc_map(temp, maps['temp_to_hum'])
  loc = calc_map(hum, maps['hum_to_loc'])
  return loc

def calc_loc_to_seed(loc: int):
  hum = calc_map_rev(loc, maps['hum_to_loc'])
  temp = calc_map_rev(hum, maps['temp_to_hum'])
  light = calc_map_rev(temp, maps['light_to_temp'])
  water = calc_map_rev(light, maps['water_to_light'])
  fert = calc_map_rev(water, maps['fert_to_water'])
  soil = calc_map_rev(fert, maps['soil_to_fert'])
  seed = calc_map_rev(soil, maps['seed_to_soil'])
  return seed

def part1():
  seeds, pairs = read_file(True)
  min_loc = float('inf')
  for seed in seeds:
    loc = calc_seed_to_loc(seed)
    if loc < min_loc:
      min_loc = loc
  print(min_loc)

def part2():
  seeds, pairs = read_file(False)
  min_seed = min([int(pairs[i][0]) for i in range(len(pairs))])
  min_loc = 0
  seed_found = False

  while not seed_found:
    seed = calc_loc_to_seed(min_loc)
    if seed > min_seed:
      for pair in pairs:
        start, length = list(map(int, pair))
        if start <= seed and seed < start+length: # if within range of pairs
          seed_found = True
          break
      if seed_found: break
    min_loc += 1
  print(min_loc)

part1()
part2() # very unoptimized, will revisit. loc: 51399228, seed: 2774900233