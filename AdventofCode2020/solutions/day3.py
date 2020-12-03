# Use modular arithmetic, DOG!


def vector_addition(x, y):
    for i in range(len(x)):
        x[i] = x[i] + y[i]
    return x


def puzzle5(input, position=[0, 0]):
    hill = [x for x in input.split("\n") if x]
    tree_count = 0
    hill_width = len(hill[0])
    hill_height = len(hill)
    slope = [3, 1]
    while position[1] < hill_height:
        x = (position[0]) % hill_width
        y = position[1]
        tree_count += hill[y][x] == "#"
        position = vector_addition(position, slope)
    return tree_count


def puzzle6(input):
    pass


if __name__ == "__main__":
    sample_input3 = "..##.......\n#...#...#..\n.#....#..#.\n..#.#...#.#\n.#...##..#.\n..#.##.....\n.#.#.#....#\n.#........#\n#.##...#...\n#...##....#\n.#..#...#.#"

    input3 = open("inputs/input3.txt", "r").read()

    # print(puzzle5(sample_input3))
    print(puzzle5(input3))

    # print(puzzle6(sample_input3))
    # print(puzzle6(input3))
