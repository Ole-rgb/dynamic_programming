import unittest


def greedy_coins(coins, target):
    coins = bubble_sort(coins)
    num_coins = 0
    i = 0
    while target != 0:
        if target < coins[i]:
            i += 1
            continue

        target -= coins[i]
        num_coins += 1

    return num_coins


def min_coins(coins, m):
    if m == 0:
        return 0

    answer = None
    for coin in coins:
        subproblem = m - coin
        if subproblem < 0:
            continue
        answer = min_ignoring_none([answer, min_coins(coins, subproblem) + 1])
    return answer


def min_coins_cached(coins, m, memo={0: 0}):
    if m in memo:
        return memo[m]

    answer = None
    for coin in coins:
        subproblem = m - coin
        if subproblem < 0:
            continue

        answer = min_ignoring_none(
            [answer, min_coins_cached(coins, subproblem, memo) + 1]
        )
    memo[m] = answer
    return memo[m]


def min_coins_iterative(coins, m, memo={0: 0}):
    for i in range(1, m + 1):
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            memo[i] = min_ignoring_none([memo.get(i), memo.get(subproblem) + 1])
    return memo[m]


def min_ignoring_none(arr_with_none):
    return min(filter(lambda x: x != None, arr_with_none))


def bubble_sort(coins):
    for i in range(0, len(coins)):
        for j in range(i + 1, len(coins)):
            if coins[i] < coins[j]:
                tmp = coins[i]
                coins[i] = coins[j]
                coins[j] = tmp
    return coins


class TestMinCoins(unittest.TestCase):
    def test_greedy_coins_coins_desc(self):
        self.assertEqual(greedy_coins([200, 100, 50, 20, 10, 5, 2, 1], 256), 4)
        self.assertEqual(greedy_coins([200, 100, 50, 20, 10, 5, 2, 1], 127), 4)
        self.assertEqual(greedy_coins([200, 100, 50, 20, 10, 5, 2, 1], 13), 3)
        self.assertEqual(greedy_coins([200, 100, 50, 20, 10, 5, 2, 1], 500), 3)

    def test_greedy_coins_coins_asc(self):
        self.assertEqual(greedy_coins([1, 2, 5, 10, 20, 50, 100, 200], 256), 4)
        self.assertEqual(greedy_coins([1, 2, 5, 10, 20, 50, 100, 200], 127), 4)
        self.assertEqual(greedy_coins([1, 2, 5, 10, 20, 50, 100, 200], 13), 3)
        self.assertEqual(greedy_coins([1, 2, 5, 10, 20, 50, 100, 200], 500), 3)

    def test_greedy_error(self):
        self.assertNotEqual(greedy_coins([1, 4, 5], 13), 3)
        self.assertNotEqual(greedy_coins([1, 4, 5], 5), 2)

    def test_min_coins_coin_values(self):
        self.assertEqual(min_coins([1, 4, 5], 1), 1)
        self.assertEqual(min_coins([1, 4, 5], 4), 1)
        self.assertEqual(min_coins([1, 4, 5], 5), 1)

    def test_min_coins_values_between_coin_values(self):
        self.assertEqual(min_coins([1, 4, 5], 2), 2)
        self.assertEqual(min_coins([1, 4, 5], 3), 3)
        self.assertEqual(min_coins([1, 4, 5], 6), 2)
        self.assertEqual(min_coins([1, 4, 5], 7), 3)

    def test_min_coins_values_greed_error_values(self):
        self.assertEqual(min_coins([1, 4, 5], 8), 2)
        self.assertEqual(min_coins([1, 4, 5], 12), 3)
        self.assertEqual(min_coins([1, 4, 5], 13), 3)

    def test_min_coins_cached(self):
        self.assertEqual(min_coins_cached([1, 4, 5], 8), 2)
        self.assertEqual(min_coins_cached([1, 4, 5], 12), 3)
        self.assertEqual(min_coins_cached([1, 4, 5], 13), 3)
        self.assertEqual(min_coins_cached([1, 4, 5], 150), 30)

    def test_min_coins_iterative(self):
        self.assertEqual(min_coins_iterative([1, 4, 5], 8), 2)
        self.assertEqual(min_coins_iterative([1, 4, 5], 12), 3)
        self.assertEqual(min_coins_iterative([1, 4, 5], 13), 3)
        self.assertEqual(min_coins_iterative([1, 4, 5], 150), 30)

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([1, 2, 3]), [3, 2, 1])
        self.assertEqual(bubble_sort([3, 2, 1]), [3, 2, 1])
        self.assertEqual(bubble_sort([1, 3, 2]), [3, 2, 1])


if __name__ == "__main__":
    unittest.main()
    # print(min_coins_cached([1, 4, 5], 8))
