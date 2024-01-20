# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# ['3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green']
# if 0 was possible, how would our input change?
# How do I make sure returns stay consistent? I forgot that I added another value to unpack so I should've automatically added another one to my false scenario
def parse_input(file_path: str):
    with open(file_path, "r") as f:
        return f.readlines()

def parse_valid_games(game: str, game_constraints: dict):
    game_index, game_data = game.strip().split(":")
    game_number = int(game_index.split(" ")[1])
    game_rounds  = game_data.split(";")
    min_cubes = {"red": 0, "green": 0, "blue":0}

    for sub_round in game_rounds:
        cubes_in_round = sub_round.strip().split(",")
        for cubes in cubes_in_round:
            cube_number, cube_color = cubes.strip().split(" ")
            cube_number = int(cube_number)
            min_cubes[cube_color] = max(cube_number, min_cubes[cube_color])
    power = 1
    for item in min_cubes:
        power = power * min_cubes[item]
    return game_number, power
def main():
    game_constraints = {"red":12, "green": 13, "blue":14}
    file_path = r"C:\Users\User\PycharmProjects\AdventOfCode\Day_2\puzzle_input.txt"
    # file_path = r"C:\Users\User\PycharmProjects\AdventOfCode\Day_2\sample_input.txt"
    game_data = parse_input(file_path)
    sum = 0
    power_sum = 0
    for game in game_data:
        game_number, power = parse_valid_games(game, game_constraints)
        sum += game_number
        power_sum += power
    print(sum)
    print(power_sum)

if __name__ == "__main__":
    main()