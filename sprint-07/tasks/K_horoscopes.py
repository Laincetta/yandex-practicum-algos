def lcs_indices(A: list[int], B: list[int]) -> tuple[int, list[int], list[int]]:
    A = [0] + A
    B = [0] + B
    n, m = len(A) - 1, len(B) - 1

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i] == B[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = n, m
    idxA, idxB = [], []

    while i > 0 and j > 0:
        if A[i] == B[j]:
            idxA.append(i)
            idxB.append(j)
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    idxA.reverse()
    idxB.reverse()

    return dp[n][m], idxA, idxB


def main():
    n = int(input())
    A = list(map(int, input().split()))
    m = int(input())
    B = list(map(int, input().split()))

    length, idxA, idxB = lcs_indices(A, B)

    print(length)
    if length > 0:
        print(*idxA)
        print(*idxB)

if __name__ == "__main__":
    main()