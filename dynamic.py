def factorial(n, memo={}):
    # TODO: implement the factorial function using dynamic programming
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = 1
        return 1
    memo[n] = n * factorial(n - 1, memo)
    return memo[n]

# The task is related to climbing stairs. Imagine you have to climb n stairs, starting with the stair number 0. At each step, you can either climb 1 stair or 2 stairs. The task is to compute the total number of distinct ways you can climb the n stairs.
#
# For example, for n = 4, the output should be total_ways(n) = 5, as 4 = 1 + 1 + 1 + 1, 4 = 1 + 1 + 2, 4 = 1 + 2 + 1, 4 = 2 + 1 + 1, and 4 = 2 + 2, totalling to 5 different ways.
def total_ways(n):
    # TODO: implement
    return total_ways_eff(n)


def total_ways_eff(n, cache={}):
    if n in cache:
        return cache[n]
    if n < 1:
        return 0
    elif n == 1:
        cache[1] = 1
        return 1
    elif n == 2:
        cache[1] = 1
        return 2
    cache[n] = total_ways_eff(n - 1, cache) + total_ways_eff(n - 2, cache)
    return cache[n]

def min_steps(n, cache={}):
    # TODO: Implement the function here
    if n in cache:
        return cache[n]
    if n == 1:
        cache[1] = 1
        return 1
    elif n == 2:
        cache[n] = 2
        return 2
    if n % 2 == 0:
        cache[n] = 1 + min(min_steps(n - 1, cache), min_steps(n / 2, cache))
    else:
        cache[n] = 1 + min_steps(n - 1, cache)
    return cache[n]


def coin_change(coins, amount: int):
    # TODO: implement the dynamic programming solution
    ways = [0] * int(amount + 1)
    ways[0] = 1
    for one_coin in coins:
        amt = one_coin
        for amt in range(one_coin, amount + 1):
            ways[amt] += ways[amt - one_coin]
    return ways[amount]


def how_many_perfect_squares(n):
    # TODO: implement the function
    perfect_squares = smaller_perfect_squares(n)
    perfect_squares.reverse()
    required_perfect_squares = n
    while len(perfect_squares) > 1:
        remaining = n
        required_additions = 0
        for perfect_square in perfect_squares:
            counter = int(remaining / perfect_square)
            remaining -= counter * perfect_square
            required_additions += counter
            if remaining == 0:
                break
        if required_additions < required_perfect_squares and remaining == 0:
            required_perfect_squares = required_additions
        perfect_squares = perfect_squares[1:]
    return required_perfect_squares


def smaller_perfect_squares(limit):
    perfect_squares = []
    i = 1
    while i * i <= limit:
        perfect_squares.append(i * i)
        i += 1
    return perfect_squares

def how_many_perfect_squares_dp(n):
    dp = [n] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            square = j ** 2
            if square > i:
                break
            dp[i] = min(dp[i], dp[i - square] + 1)
    return dp[-1]


if __name__ == "__main__":
    print(how_many_perfect_squares_dp(4))