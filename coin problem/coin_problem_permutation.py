from collections import defaultdict


def coin_permutation_iterative(coins, m, memo={0: 1}):
    for i in range(1, m + 1):
        memo[i] = 0
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            memo[i] = memo[i] + memo[subproblem]
    return memo[m]


def coin_permutation_memo(coins, m, memo={0: 1}):
    if m in memo:
        return memo[m]

    answer = 0
    for coin in coins:
        subproblem = m - coin
        if subproblem < 0:
            continue

        answer += coin_permutation_memo(coins, subproblem, memo)

    memo[m] = answer
    return answer


def coin_permutation(coins, m):
    """
    Given state m = 5
    -> explore:
        ->5-1 -> 4-4 -> return 1
              -> 4-1 -> ... -> 1-1 -> return 1

        ->5-4 -> 1-1 -> return 1

        ->5-5 return 1

    explore all possible paths
    """
    if m == 0:
        return 1

    answer = 0
    for coin in coins:
        subproblem = m - coin
        if subproblem < 0:
            continue

        answer += coin_permutation(coins, subproblem)

    return answer


if __name__ == "__main__":
    print(coin_permutation([1, 4, 5], 5))  # 4+1, 1+4, 5, 1+1+1+1+1 -> 4
    print(
        coin_permutation([1, 4, 5], 6)
    )  # 4+1+1, 1+1+4, 1+4+1, 5+1, 1+5, +1+1+1+1+1+1 -> 6
    print(coin_permutation_memo([1, 4, 5], 50))
    print(coin_permutation_memo([1, 4, 5], 500))

    print(coin_permutation_iterative([1, 4, 5], 50))
    # print(coin_permutation_iterative([1, 4, 5], 500))
