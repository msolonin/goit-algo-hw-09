import timeit

ATTEMPTS = 2
COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(coins_sum):
    count_coins = {}
    for coin in COINS:
        count = coins_sum // coin
        if count > 0:
            count_coins[coin] = count
        coins_sum -= coin * count
    return count_coins


def find_min_coins(coins_sum):
    min_coins_required = [0] + [float("inf")] * coins_sum
    last_coin_used = [0] * (coins_sum + 1)
    for s in range(1, coins_sum + 1):
        for coin in COINS:
            if s >= coin and min_coins_required[s - coin] + 1 < min_coins_required[s]:
                min_coins_required[s] = min_coins_required[s - coin] + 1
                last_coin_used[s] = coin
    count_coins = {}
    current_sum = coins_sum
    while current_sum > 0:
        coin = last_coin_used[current_sum]
        count_coins[coin] = count_coins.get(coin, 0) + 1
        current_sum = current_sum - coin
    return count_coins


if __name__ == "__main__":
    cons_sum_small = 113
    cons_sum_large = 158917
    result_coins_greedy = find_coins_greedy(cons_sum_small)
    result_min_coins = find_min_coins(cons_sum_small)
    print(f"For greedy algorithm: {result_coins_greedy}")
    print(f"For min algorithm: {result_min_coins}")
    result_coins_greedy_large = find_coins_greedy(cons_sum_large)
    result_min_coins_large = find_min_coins(cons_sum_large)
    print(f"For greedy algorithm: {result_coins_greedy_large}")
    print(f"For min algorithm: {result_min_coins_large}")
    time_small_greedy = timeit.timeit(lambda: find_coins_greedy(cons_sum_small), number=ATTEMPTS)
    time_small_min = timeit.timeit(lambda: find_min_coins(cons_sum_small), number=ATTEMPTS)
    time_large_greedy = timeit.timeit(lambda: find_coins_greedy(cons_sum_large), number=ATTEMPTS)
    time_large_min = timeit.timeit(lambda: find_min_coins(cons_sum_large), number=ATTEMPTS)
    print(f"{'| Algorithm': <26} | {'Time small data': <26} | {'Time large data': <26}")
    print(f"|{'-'*25} | {'-'*26} | {'-'*19}")
    print(f"| {'Greedy': <24} | {time_small_greedy: <26} | {time_large_greedy: <20}")
    print(f"| {'Minimal': <24} | {time_small_min: <26} | {time_large_min: <25}")
