from typing import List

def main():
    with open("./input.txt", "r") as file:
        lines = file.read().splitlines()
        reports = [[int(r) for r in l.split(" ")] for l in lines]
        print(f"Solution Part 1: {solve_part1(reports)}")
        print(f"Solution Part 2: {solve_part2(reports)}")


def is_safe(report: List[int]) -> bool:
    if report[0] == report[1]:
        return False
    if report[0] < report[1]: # check all increasing
        for i in range(len(report) - 1):
            step = report[i+1] - report[i]
            if not (1 <= step <= 3):
                return False
    else: # check all decreasing
        for i in range(len(report) - 1):
            step = report[i] - report[i+1]
            if not (1 <= step <= 3):
                return False
    return True


def is_valid_increasing(report: List[int], is_recursive: bool) -> bool:
    for i in range(len(report) - 1):
        step = report[i+1] - report[i]
        if not (1 <= step <= 3):
            if is_recursive:
                return False
            return (is_valid_increasing(report[:i] + report[i+1:], True)
                    or is_valid_increasing(report[:(i+1)] + report[(i+1)+1:], True))
    return True

def is_valid_decreasing(report: List[int], is_recursive: bool) -> bool:
    for i in range(len(report) - 1):
        step = report[i] - report[i+1]
        if not (1 <= step <= 3):
            if is_recursive:
                return False
            return (is_valid_decreasing(report[:i] + report[i+1:], True)
                    or is_valid_decreasing(report[:(i+1)] + report[(i+1)+1:], True))
    return True


def is_safe_part2(report: List[int], is_recursive: bool) -> bool:
    if is_valid_decreasing(report, False) or is_valid_increasing(report, False):
        return True
    return False


def solve_part1(reports: List[List[int]]) -> int:
    safe_reports = 0
    for r in reports:
        if is_safe(r):
            safe_reports += 1
    return safe_reports


def solve_part2(reports: List[List[int]]) -> int:
    safe_reports = 0
    for r in reports:
        if is_safe_part2(r, False):
            safe_reports += 1
    return safe_reports


if __name__ == '__main__':
    main()

    data = [
        [7, 6, 4, 2, 1,],
        [1, 2, 7, 8, 9,],
        [9, 7, 6, 2, 1,],
        [1, 3, 2, 4, 5,],
        [8, 6, 4, 4, 1,],
        [1, 3, 6, 7, 9],
    ]
