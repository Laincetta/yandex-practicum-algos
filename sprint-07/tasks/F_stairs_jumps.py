MOD = 10 ** 9 + 7
def dp_get_max_jump_ways(n: int, k: int):
    dp = [0] * n
    dp[0] = 1

    for i in range(1, n):
        start = max(0, i - k)
        for j in range(start, i):
            dp[i] = (dp[i] + dp[j])

    return dp[n - 1] % MOD

def main():
    n, k = map(int, input().split())
    print(dp_get_max_jump_ways(n, k))

if __name__ == "__main__":
    main()
