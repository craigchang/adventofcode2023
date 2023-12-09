# https://adventofcode.com/2023/day/7

from functools import cmp_to_key

cards_map = {
  'A':14, 
  'K':13,
  'Q':12,
  'J':11,
  'T':10, 
  '9':9,
  '8':8,
  '7':7,
  '6':6,
  '5':5,
  '4':4,
  '3':3,
  '2':2
}

HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIR = 2
THREE_KIND = 3
FULL_HOUSE = 4
FOUR_KIND = 5
FIVE_KIND = 6

def read_file():
  with open("day7/input.txt", "r") as f:
    hands = []
    for l in f.readlines():
      hand, bid = l.strip().split()
      hands.append([hand, int(bid)])
    return hands
  
def get_hand_type(hand):
  hand_map = dict()
  for c in hand:
    if c not in hand_map:
      hand_map[c] = 1
    else:
      hand_map[c] += 1
  values = list(hand_map.values())

  if 5 in values:
    return FIVE_KIND
  elif 4 in values:
    return FOUR_KIND
  elif 3 in values and 2 in values:
    return FULL_HOUSE
  elif 3 in values:
    return THREE_KIND
  elif values.count(2) == 2:
    return TWO_PAIR
  elif 2 in values:
    return ONE_PAIR
  else:
    return HIGH_CARD

def get_hand_with_joker(hand: str):
  best_hand = hand
  best_hand_type = get_hand_type(best_hand)
  if 'J' in hand:
    for k,v in cards_map.items():
      new_hand = hand.replace("J", k)
      new_hand_type = get_hand_type(new_hand)
      if new_hand_type > best_hand_type or new_hand_type == best_hand_type and compare_hand_by_card(new_hand, best_hand):
        best_hand = new_hand
        best_hand_type = get_hand_type(best_hand)
  return best_hand

def compare_hands(hand_a: str, hand_a_type: int, hand_b: str, hand_b_type: int):
  if hand_a_type > hand_b_type:
    return 1
  elif hand_a_type < hand_b_type:
    return -1
  else:
    return compare_hand_by_card(hand_a, hand_b)

def compare_hand_by_card(hand_a,hand_b):
  for i in range(len(hand_a)):
    if cards_map[hand_a[i]] > cards_map[hand_b[i]]:
      return 1
    elif cards_map[hand_a[i]] < cards_map[hand_b[i]]:
      return -1
  return 0

def sort_compare(hand_a: tuple, hand_b: tuple):
  hand_a, hand_b = hand_a[0], hand_b[0]
  return compare_hands(hand_a, get_hand_type(hand_a), hand_b, get_hand_type(hand_b))

def sort_compare_with_joker(hand_a: tuple, hand_b: tuple):
  hand_a, hand_b = hand_a[0], hand_b[0]
  return compare_hands(hand_a, get_hand_type(get_hand_with_joker(hand_a)), hand_b, get_hand_type(get_hand_with_joker(hand_b)))

def get_rank(hands: list):
  return sum([hands[i][1] * (i+1) for i in range(len(hands))])

def part1():
  hands = read_file()
  ordered_hands = sorted(hands, key=cmp_to_key(sort_compare))
  print("Part 1:", get_rank(ordered_hands))

def part2():
  cards_map['J'] = 1
  hands = read_file()
  ordered_hands = sorted(hands, key=cmp_to_key(sort_compare_with_joker))
  print("Part 2:", get_rank(ordered_hands))

part1()
part2()
