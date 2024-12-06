import re

def main():
    with open("./input.txt", "r") as file:
        instructions = file.read()
        print(f"Solution Part 1: {solve_part1(instructions)}")
        print(f"Solution Part 2: {solve_part2(instructions)}")


def solve_part1(instructions: str) -> int:
    valid_instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", instructions)
    result = 0
    for instruction in valid_instructions:
        x, y = instruction[4:-1].split(',')
        result += int(x) * int(y)
    return result


def solve_part2(instructions: str) -> int:
    valid_instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", instructions)
    result = 0
    enabled = True
    for instruction in valid_instructions:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif enabled:
            x, y = instruction[4:-1].split(',')
            result += int(x) * int(y)
    return result


if __name__ == '__main__':
    main()
