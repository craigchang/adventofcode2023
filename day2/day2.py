# https://adventofcode.com/2023/day/2

import re

def calc_cubes(color: str, min_color: int, cube: str): # calculate color count and min
    found = re.findall('(\d+) ' + color, cube)
    count_color = int(found[0]) if found else 0
    min_color = count_color if count_color > min_color else min_color
    return count_color, min_color

def main():
    with open("day2/input.txt", "r") as f:
        possible_games, total_power = [], 0

        for game in f.readlines():
            tokens = re.findall('Game (\d+): (.*)', game.strip())[0]
            game_id, game_sets = int(tokens[0]), tokens[1].split(";")

            possible_game = True
            min_red, min_green, min_blue = 0, 0, 0

            for gs in game_sets:
                cubes = gs.split(", ")
                for c in cubes:
                    count_red, min_red = calc_cubes('red', min_red, c)
                    count_green, min_green = calc_cubes('green', min_green, c)
                    count_blue, min_blue = calc_cubes('blue', min_blue, c)
                    if count_red > 12 or count_green > 13 or count_blue > 14:
                        possible_game = False
                        
            total_power += min_red * min_green * min_blue
            if possible_game:
                possible_games.append(game_id)

        print("Part 1: ", sum(possible_games))
        print("Part 2: ", total_power)

main()