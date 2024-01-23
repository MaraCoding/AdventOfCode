import re

def file_as_lines(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]

def find_part_number_sum(input:list):
    for line in input:
        pass
def main():
    file_path = r"C:\Users\User\PycharmProjects\AdventOfCode\Day_3\sample_input.txt"
    input = file_as_lines(file_path)
    find_part_number_sum(input)
if __name__ == "__main__":
    main()

    #group numbers
    #are there symbols adjacent to numbers in current line
    #go through line, find the index of the last digit of every number
    #find index of every symbol. Compare indexes, if they are within 1 of eachother then they are valid.
    magnitudes = []
