def get_first_num(string: str) -> str:
    for character in string:
        if character.isdigit():
            return character

def get_last_num(string: str) -> str:
    string = string[::-1]
    for character in string:
        if character.isdigit():
            return character


def get_lines_of_text(file_path) -> list:
    with open(file_path) as f:
        return f.readlines()

def main():
    file_path = r"/Day_1/sample_file.txt"
    lines_of_text = get_lines_of_text(file_path)
    total = 0
    for string in lines_of_text:
        digit_pair = int(get_first_num(string) + get_last_num(string))
        total += digit_pair

    print(f"Total is {total}")


if __name__ == '__main__':
    main()
