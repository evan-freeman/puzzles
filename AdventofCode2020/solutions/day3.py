# Use modular arithmetic, DOG!


def vector_addition(x, y):
    for i in range(len(x)):
        x[i] = x[i] + y[i]
    return x


def puzzle5(input, slope=[3, 1], clean_input=True, hill=None):
    # Flag to avoid cleaning multiple times in puzzle 6
    if clean_input:
        hill = [x for x in input.split("\n") if x]
    position = [0, 0]
    tree_count = 0
    hill_width = len(hill[0])
    hill_height = len(hill)
    while position[1] < hill_height:
        x = position[0] % hill_width
        y = position[1]
        tree_count += hill[y][x] == "#"
        position = vector_addition(position, slope)
    return tree_count


def puzzle6(input):
    hill = [x for x in input.split("\n") if x]
    slope_list = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    answers = []
    for slope in slope_list:
        answers.append(puzzle5(input, slope=slope, clean_input=False, hill=hill))
    output = 1
    for answer in answers:
        output *= answer
    return output


if __name__ == "__main__":
    sample_input3 = "..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#"
    input3 = open("inputs/input3.txt", "r").read()

    print(puzzle5(sample_input3))
    print(puzzle5(input3))
    print(puzzle6(sample_input3))
    print(puzzle6(input3))
