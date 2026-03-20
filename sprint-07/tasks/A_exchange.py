def get_max_profit(prices: list[int], n: int) -> int:
    total_profit = 0
    for i in range(n - 1):
        cur_profit = prices[i + 1] - prices[i]
        if cur_profit > 0:
            total_profit += cur_profit
    return total_profit


def main():
    n = int(input())
    prices = list(map(int, input().split()))
    max_profit = get_max_profit(prices, n)
    print(max_profit)


if __name__ == '__main__':
    main()