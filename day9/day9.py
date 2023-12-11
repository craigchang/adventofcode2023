# https://adventofcode.com/2023/day/9

def read_file(filepath):
  with open(filepath, "r") as f:
    histories = []
    for l in f.readlines():
      histories.append(list(map(int, l.strip().split())))
    return histories

def get_sequences(history: list):
  sequences = [history.copy()]
  while any(sequences[-1]): # loop until last seq has all zeros
    new_seq = []
    curr_seq = sequences[-1]
    for i in range(1, len(curr_seq)):
      new_seq.append(curr_seq[i] - curr_seq[i-1])
    sequences.append(new_seq)
  return sequences

def part1():
  sum_vals = 0
  for h in [get_sequences(h) for h in read_file("day9/input.txt")]:
    h[-1].append(0)
    for seq in range(len(h)-2, -1, -1):
      h[seq].append(h[seq+1][-1] + h[seq][-1]) # last val of next seq + last val of curr seq
    sum_vals += h[0][-1]
  print("Part 1:", sum_vals)

def part2():
  sum_vals = 0
  for h in [get_sequences(h) for h in read_file("day9/input.txt")]:
    h[-1].append(0)
    for seq in range(len(h)-2, -1, -1):
      h[seq].insert(0, h[seq][0] - h[seq+1][0]) # first val of curr seq - first val of next seq
    sum_vals += h[0][0]
  print("Part 2:", sum_vals)

part1()
part2()

[].insert