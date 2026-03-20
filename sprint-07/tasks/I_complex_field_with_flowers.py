def get_max_flow_collected_way(flower_field: list[list[int]], n: int, m: int) -> tuple[int, str]:
    dp = [[-1 for _ in range(m + 2)] for _ in range(n + 2)]

    for i in range(n - 1, -1, -1):
        for j in range(m):
            dp_i = i + 1
            dp_j = j + 1
            max_step = max(dp[dp_i][dp_j-1], dp[dp_i+1][dp_j]) if  max(dp[dp_i][dp_j-1], dp[dp_i+1][dp_j]) != -1 else 0
            dp[dp_i][dp_j] = max_step + flower_field[i][j]

    max_flow_collected = dp[1][m]
    max_flow_collected_way = []

    s_i, s_j = 1, m
    while not (s_i == n and s_j == 1):
        if dp[s_i][s_j-1] >= dp[s_i+1][s_j]:
            s_j -= 1
            max_flow_collected_way.append('R')
        else:
            s_i += 1
            max_flow_collected_way.append('U')

    max_flow_collected_way_str = ''.join(reversed(max_flow_collected_way))

    return max_flow_collected, max_flow_collected_way_str


def main():
    n, m = tuple(map(int, input().split()))
    flower_field = [list(map(int, input().strip())) for _ in range(n)]
    max_flow_collected, max_flow_collected_way = get_max_flow_collected_way(flower_field, n, m)
    print(max_flow_collected)
    print(max_flow_collected_way)

if __name__ == '__main__':
    main()