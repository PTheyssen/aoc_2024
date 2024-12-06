from collections import deque

def main():
    with open("./input.txt", "r") as file:
        words = file.read().splitlines()
        print(f"Solution Part 1: {solve_part1(words)}")
        print(f"Solution Part 2: {solve_part2(words)}")
        return words

def is_valid_XMAS(words, positions) -> bool:
    stack = ["S", "A", "M"]
    for (i, j) in positions:
        if 0 > i or i >= len(words):
            return False
        if 0 > j or j >= len(words):
            return False
        nextChar = stack.pop()
        if words[i][j] != nextChar:
            return False
    return True

def solve_part1(words: str) -> int:
    solution = 0
    for i in range(len(words[0])):
        for j in range(len(words)):
            if words[i][j] == "X":
                candidates = [
                    # left
                    [(i, j-1), (i, j-2), (i, j-3)],
                    # right
                    [(i, j+1), (i, j+2), (i, j+3)],
                    # top
                    [(i+1, j), (i+2, j), (i+3, j)],
                    # bottom
                    [(i-1, j), (i-2, j), (i-3, j)],
                    # right top diagonal
                    [(i-1, j+1), (i-2, j+2), (i-3, j+3)],
                    # right bottom diagonal
                    [(i+1, j+1), (i+2, j+2), (i+3, j+3)],
                    # left top diagonal
                    [(i-1, j-1), (i-2, j-2), (i-3, j-3)],
                    # left bottom diagonal
                    [(i+1, j-1), (i+2, j-2), (i+3, j-3)]
                ]
                valid_cand = [x for x in candidates if is_valid_XMAS(words, x)]
                solution += len(valid_cand)
    return solution



def is_valid_X_MAS(words, positions) -> bool:
    """
    M.S
    .A.
    M.S
    ---
    M.M
    .A.
    S.S
    ---
    S.M
    .A.
    S.M
    ---
    S.S
    .A.
    M.M

    check all A's
    """
    ## think about mathematical group / symmetry of this
    valid_sequences = [
        ["M", "S", "S", "M"],
        ["M", "M", "S", "S"],
        ["S", "M", "M", "S"],
        ["S", "S", "M", "M"],
    ]
    curr_sequence = []
    for (i, j) in positions:
        if 0 > i or i >= len(words):
            return False
        if 0 > j or j >= len(words):
            return False
        curr_sequence.append(words[i][j])
    if curr_sequence in valid_sequences:
        return True
    return False

def solve_part2(words: str) -> int:
    solution = 0
    for i in range(len(words[0])):
        for j in range(len(words)):
            if words[i][j] == "A":
                candidates = [
                    [(i-1, j-1), (i-1, j+1), (i+1, j+1), (i+1, j-1)],
                ]
                valid_cand = [x for x in candidates if is_valid_X_MAS(words, x)]
                solution += len(valid_cand)
    return solution

if __name__ == '__main__':
    # words 140 x 140 matrix
    words = main()
