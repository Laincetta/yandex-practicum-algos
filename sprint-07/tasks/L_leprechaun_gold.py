def get_max_gold_weight(weights: list[int], n: int, M: int) -> int:
    M_z = M + 1 # M's from zero
    dp = [0] * M_z

    for weight in weights:
        for i in range(M, weight - 1, -1):
            if i >= weight:
                dp[i] = max(dp[i], weight + dp[i - weight])

    max_gold_weight = dp[M]
    return max_gold_weight

def main():
    n, M = tuple(map(int, input().split()))
    weights = list(map(int, input().split()))

    max_gold_weight = get_max_gold_weight(weights, n, M)
    print(max_gold_weight)

if __name__ == '__main__':
    main()