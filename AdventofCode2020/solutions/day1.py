def puzzle1(lst):
    compliments = {}
    for x in lst:
        if x not in compliments:
            y = 2020 - x
            compliments[y] = x
        else:
            return x * compliments[x]


def puzzle1maybefaster(lst):
    compliments = {}
    for x in lst:
        if x not in compliments:
            compliments[2020 - x] = x
        else:
            return x * compliments[x]


def puzzle1slow(lst):
    for x in lst:
        for y in lst:
            if x != y and x + y == 2020:
                return x * y


def puzzle2(lst):
    comps1 = {}
    comps2 = {}
    for x in lst:
        if x not in comps2:
            for s in comps1:
                z = s - x
                comps2[z] = [x, comps1[s]]
            s = 2020 - x
            comps1[s] = x
        else:
            return x * comps2[x][0] * comps2[x][1]


def puzzle2maybefaster(lst):
    comps1 = {}
    comps2 = {}
    for x in lst:
        if x not in comps2:
            for s in comps1:
                z = s - x
                comps2[z] = {0: x, 1: comps1[s]}
            s = 2020 - x
            comps1[s] = x
        else:
            return x * comps2[x][0] * comps2[x][1]


def puzzle2slow(lst, target=2020):
    for x in lst:
        for y in lst:
            for z in lst:
                if x != y and y != z and x + y + z == target:
                    return x * y * z


if __name__ == "__main__":
    sample_input = [1721, 979, 366, 299, 675, 1456]
    input1 = open("input1.txt", "r").read()
    input1_list = [int(x) for x in input1.split("\n") if x]

    print(puzzle1(sample_input))
    print(puzzle1slow(sample_input))

    print(puzzle1(input1_list))
    print(puzzle1slow(input1_list))

    print(puzzle2(sample_input))
    print(puzzle2slow(sample_input))

    print(puzzle2(input1_list))
    print(puzzle2slow(input1_list))
