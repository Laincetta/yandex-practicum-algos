def get_max_flow_collected(flower_field: list[list[int]], n: int, m: int) -> int:
    dp = [[0 for _ in range(m + 2)] for _ in range(n + 2)]

    for i in range(n - 1, -1, -1):
        for j in range(m):
            dp_i = i + 1
            dp_j = j + 1
            dp[dp_i][dp_j] = max(dp[dp_i][dp_j-1], dp[dp_i+1][dp_j]) + flower_field[i][j]

    max_flow_collected = dp[1][m]

    return max_flow_collected


def main():
    n, m = tuple(map(int, input().split()))
    flower_field = [list(map(int, input().strip())) for _ in range(n)]
    max_flow_collected = get_max_flow_collected(flower_field, n, m)
    print(max_flow_collected)

if __name__ == '__main__':
    main()