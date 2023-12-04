# https://adventofcode.com/2023/day/4

import re

def read_file():
    with open("day4/input.txt", "r") as f:
        cards = []
        for l in f.readlines():
            tokens = re.findall("Card\s+(\d+): (.+) \| (.+)", l)[0]
            cards.append([int(tokens[0])-1, tokens[1].strip().split(), tokens[2].strip().split()])
        return cards

def get_card_copies_recursive(i: int, winning_cards_dict: dict):
    num_winning_cards = winning_cards_dict[i]
    total_num_cards = 1
    for i in range(i + 1, i + 1 + num_winning_cards):
        total_num_cards += get_card_copies_recursive(i, winning_cards_dict)
    return total_num_cards

def part1():
    cards = read_file()
    total_pts = 0
    for card_num, win_nums, hand_nums in cards:
        points = 0
        for num in hand_nums:
            if num in win_nums:
                points = 1 if points == 0 else points * 2
        total_pts += points
    print("Part 1:", total_pts)

def part2():
    cards = read_file()
    win_cards_dict = dict()
    total_cards = 0

    for card_num, win_nums, hand_nums in cards:
        if card_num not in win_cards_dict:
            win_cards_dict[card_num] = sum([1 for num in hand_nums if num in win_nums])
    
    for i in range(len(win_cards_dict.items())):
        num_winning_cards = win_cards_dict[i]
        for j in range(i + 1, i + 1 + num_winning_cards):
            total_cards += get_card_copies_recursive(j, win_cards_dict) # get copy of cards
        total_cards += 1 # include current card
    print("Part 2:", total_cards)

part1()
part2()