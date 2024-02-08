import unittest
import time


def fibonacci_cached_bottum_up(fib):
    memo = {0: 0, 1: 1}

    for i in range(2, fib + 1):
        result = memo[i - 1] + memo[i - 2]
        memo[i] = result

    return memo[fib]


def fibonacci_sequence_cached(fib: int, memo={0: 0, 1: 1}):
    if fib in memo:
        return memo[fib]

    memo[fib] = fibonacci_sequence_cached(fib - 1) + fibonacci_sequence_cached(fib - 2)
    return memo[fib]


def fibonacci_sequence(fib: int):
    if fib == 0:
        return 0
    if fib == 1:
        return 1

    return fibonacci_sequence(fib - 1) + fibonacci_sequence(fib - 2)


class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        assert fibonacci_sequence(0) == 0
        assert fibonacci_sequence(1) == 1
        assert fibonacci_sequence(2) == 1
        assert fibonacci_sequence(3) == 2
        assert fibonacci_sequence(4) == 3
        assert fibonacci_sequence(5) == 5
        assert fibonacci_sequence(6) == 8
        assert fibonacci_sequence(7) == 13
        assert fibonacci_sequence(8) == 21
        assert fibonacci_sequence(9) == 34
        assert fibonacci_sequence(10) == 55
        assert fibonacci_sequence(11) == 89
        assert fibonacci_sequence(12) == 144
        assert fibonacci_sequence(13) == 233
        assert fibonacci_sequence(14) == 377
        assert fibonacci_sequence(15) == 610

    def test_fibonacci_bottom_up(self):
        assert fibonacci_cached_bottum_up(0) == 0
        assert fibonacci_cached_bottum_up(1) == 1
        assert fibonacci_cached_bottum_up(2) == 1
        assert fibonacci_cached_bottum_up(3) == 2
        assert fibonacci_cached_bottum_up(4) == 3
        assert fibonacci_cached_bottum_up(5) == 5
        assert fibonacci_cached_bottum_up(6) == 8
        assert fibonacci_cached_bottum_up(7) == 13
        assert fibonacci_cached_bottum_up(8) == 21
        assert fibonacci_cached_bottum_up(9) == 34
        assert fibonacci_cached_bottum_up(10) == 55
        assert fibonacci_cached_bottum_up(11) == 89
        assert fibonacci_cached_bottum_up(12) == 144
        assert fibonacci_cached_bottum_up(13) == 233
        assert fibonacci_cached_bottum_up(14) == 377
        assert fibonacci_cached_bottum_up(15) == 610

    def test_fibonacci_cached(self):
        assert fibonacci_sequence_cached(0) == 0
        assert fibonacci_sequence_cached(1) == 1
        assert fibonacci_sequence_cached(2) == 1
        assert fibonacci_sequence_cached(3) == 2
        assert fibonacci_sequence_cached(4) == 3
        assert fibonacci_sequence_cached(5) == 5
        assert fibonacci_sequence_cached(6) == 8
        assert fibonacci_sequence_cached(7) == 13
        assert fibonacci_sequence_cached(8) == 21
        assert fibonacci_sequence_cached(9) == 34
        assert fibonacci_sequence_cached(10) == 55
        assert fibonacci_sequence_cached(11) == 89
        assert fibonacci_sequence_cached(12) == 144
        assert fibonacci_sequence_cached(13) == 233
        assert fibonacci_sequence_cached(14) == 377
        assert fibonacci_sequence_cached(15) == 610


if __name__ == "__main__":
    FIB_NUM = 50
    # unittest.main()
    start = time.time()
    print(fibonacci_sequence_cached(FIB_NUM))
    end = time.time()
    print("caches took: {}seconds".format(end - start))

    start = time.time()
    print(fibonacci_cached_bottum_up(FIB_NUM))
    end = time.time()
    print("bottum up took: {}seconds".format(end - start))

    start = time.time()
    print(fibonacci_sequence(FIB_NUM))
    end = time.time()
    print("normal took: {}seconds".format(end - start))
