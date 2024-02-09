def options_in_maze(position):
    """The rabbit is in the upper left corner and wants to go to the lower right corner.
    How many ways are there if the rabbit can only go right or down?
    -------------------------
    |   x   |       |       |
    -------------------------
    |       |       |       |
    -------------------------
    |       |       |   G   |
    -------------------------
    """
    TARGET = (1, 1)
    # rabbit arrived at the target position
    if position[0] == TARGET[0] or position[1] == TARGET[1]:
        return 1

    answer = 0
    for direction in [(-1, 0), (0, -1)]:
        new_position = (position[0] + direction[0], position[1] + direction[1])
        if new_position[0] >= TARGET[0] and new_position[1] >= TARGET[1]:
            # if it is a valid state
            answer += options_in_maze(new_position)

    return answer


def options_in_maze_with_memo(n, m, memo={(1, 1): 1}):
    """The rabbit is in the upper left corner and wants to go to the lower right corner.
    How many ways are there if the rabbit can only go right or down?
    -------------------------
    |   x   |       |       |
    -------------------------
    |       |       |       |
    -------------------------
    |       |       |   G   |
    -------------------------
    """

    # rabbit arrived at the target position
    if (n, m) in memo:
        return memo[(n, m)]

    answer = 0
    for direction in [(-1, 0), (0, -1)]:
        new_position = (n + direction[0], m + direction[1])
        if new_position[0] >= 1 and new_position[1] >= 1:
            # if it is a valid state
            answer += options_in_maze(new_position)
    memo[(n, m)] = answer
    return memo[(n, m)]


def maze_iterative(m, n):
    memo = {}

    # if the rabit hits the corner there is only one way to go to the end-state
    for i in range(1, n + 1):
        memo[(i, 1)] = 1
    for j in range(1, m + 1):
        memo[(1, j)] = 1

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            # the solution of both options combined
            memo[(i, j)] = memo[(i - 1, j)] + memo[(i, j - 1)]

    return memo[(n, m)]


if __name__ == "__main__":
    print("RECURSIVE:")
    print(options_in_maze((3, 2)))
    print(options_in_maze((3, 3)))
    print(options_in_maze((6, 6)))

    print("RECURSIVE MEMO:")
    print(options_in_maze_with_memo(3, 2))
    print(options_in_maze_with_memo(3, 3))
    print(options_in_maze_with_memo(6, 6))

    print("ITERATIVE:")
    print(maze_iterative(3, 2))
    print(maze_iterative(3, 3))
    print(maze_iterative(6, 6))

    # print(options_in_maze((6, 9)))
