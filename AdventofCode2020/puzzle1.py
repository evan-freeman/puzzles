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


if __name__ == "__main__":
    sample_input = [1721, 979, 366, 299, 675, 1456]
    input1 = open("input1.txt", "r").read()
    input1_list = [int(x) for x in input1.split("\n") if x]

    print(puzzle1(sample_input))
    print(puzzle1slow(sample_input))

    print(puzzle1(input1_list))
    print(puzzle1slow(input1_list))
