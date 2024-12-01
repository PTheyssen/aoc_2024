from collections import Counter

def main():
    with open('./input.txt') as f:
        lists = f.read().splitlines()
        list1 = [int(l.split(' ')[0]) for l in lists]
        list2 = [int(l.split(' ')[-1]) for l in lists]
        print(f"Solution Part 1: {solve_part1(list1, list2)}")
        print(f"Solution Part 2: {solve_part2(list1, list2)}")        


def solve_part1(list_1: list[int], list_2: [int]):
    assert(len(list_1) == len(list_2))
    l1_sorted = sorted(list_1)
    l2_sorted = sorted(list_2)
    distance = 0
    for i in range(len(list_1)):
        distance += abs(l1_sorted[i] - l2_sorted[i])
    return distance


def solve_part2(list_1: list[int], list_2: [int]):
    assert(len(list_1) == len(list_2))
    counter_l2 = Counter(list_2)
    similarity_score = 0
    for i in range(len(list_1)):
        similarity_score += list_1[i] * counter_l2[list_1[i]]
    return similarity_score


if __name__ == '__main__':
    main()
