# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# ['3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green']
# if 0 was possible, how would our input change?
# How would I consolidate the two parts into one script? Should I?
def parse_input(file_path: str):
    with open(file_path, "r") as f:
        return f.readlines()

def parse_valid_games(game: str, game_constraints: dict):
    game_index, game_data = game.strip().split(":")
    game_number = int(game_index.split(" ")[1])
    game_rounds  = game_data.split(";")

    for round in game_rounds:
        cubes_in_round = round.strip().split(",")
        for cubes in cubes_in_round:
            cube_number, cube_color = cubes.strip().split(" ")
            cube_number = int(cube_number)
            if cube_number > game_constraints[cube_color]:
                return 0
    return game_number

def main():
    game_constraints = {"red":12, "green": 13, "blue":14}
    file_path = r"C:\Users\User\PycharmProjects\AdventOfCode\Day_2\puzzle_input.txt"
    # file_path = r"C:\Users\User\PycharmProjects\AdventOfCode\Day_2\sample_input.txt"
    game_data = parse_input(file_path)
    sum = 0
    power_sum = 0
    for game in game_data:
        game_number= parse_valid_games(game, game_constraints)
        sum += game_number
    print(sum)

if __name__ == "__main__":
    main()