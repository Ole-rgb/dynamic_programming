import math


def quattronacci(n: int) -> int:
    q = [None] * max(4, n)

    q[0] = q[1] = q[2] = q[3] = 1

    for i in range(4, n):
        q[i] = q[i - 1] + q[i - 2] + q[i - 3] + q[i - 4]

    return q[n - 1]


if __name__ == "__main__":
    print(quattronacci(3))
    print(quattronacci(4))
    print(quattronacci(5))
