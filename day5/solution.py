from collections import defaultdict

def main():
    with open("./input.txt", "r") as file:
        all_input = file.read().splitlines()
        separate = all_input.index("")
        page_ordering_rules = all_input[:separate]
        updates = [[int(p) for p in x.split(',')] for x in all_input[separate+1:]]

        rules = defaultdict(list)
        for rule in page_ordering_rules:
            x, y = [int(n) for n in rule.split("|")]
            # add predecessor to y
            rules[x].append(y)

        solution_part1, incorrect_updates = solve_part1(rules, updates)
        print(f"Solution Part 1: {solution_part1}")
        print(f"Solution Part 2: {solve_part2(rules, incorrect_updates)}")
        return all_input, rules, updates


def solve_part1(rules, updates) -> int:
    # condition check for each number all predecessors
    # if they have conflicting rule, this lookup quickly via hashmap (edges)
    solution = 0
    incorrect_updates = []
    for update in updates:
        # print("update: ", update)
        valid = True
        for i in range(len(update)-1, -1, -1):
            curr_page_checked = update[i]
            for j in range(i):
                if update[j] in rules[curr_page_checked]:
                    # print("update[j]: ", update[j])
                    # print("curr_page_checked: ", curr_page_checked)
                    # print(rules[curr_page_checked])
                    valid = False
        if valid:
            # add middle page number
            solution += update[len(update)//2]
        else:
            incorrect_updates.append(update)
    return solution, incorrect_updates


def solve_part2(rules, incorrect_updates) -> int:
    # find topological sort using Kahn's algorithm
    # build graph every time for each update + rules
    corrected_updates = []
    solution = 0
    for incorr_update in incorrect_updates:
        result = []
        in_degree = defaultdict(int)
        nodes = incorr_update
        curr_rules = defaultdict(list)
        for n in nodes:
            for m in rules[n]:
                if m in nodes:
                    curr_rules[n].append(m)
                    in_degree[m] += 1
        # big question unique solution or sorting needed,
        # or different way of correct (only swapping few pages?)
        s = []
        for n in nodes:
            has_no_incoming = True
            for r in curr_rules.values():
                if n in r:
                    has_no_incoming = False
            if has_no_incoming:
                s.append(n)
        while s:
            next_n = s.pop()
            result.append(next_n)
            for neigh in curr_rules[next_n]:
                in_degree[neigh] -= 1
                if in_degree[neigh] == 0:
                    s.append(neigh)
        corrected_updates.append(result)
        solution += result[len(result) // 2]
    return solution


if __name__ == '__main__':
    all_input, rules, updates = main()
