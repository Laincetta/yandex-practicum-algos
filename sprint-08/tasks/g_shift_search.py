def shift_search(X: list[int], A: list[int], n: int, m: int) -> list[int]:
    poses = []
    for i in range(n - m + 1):
        const = abs(X[i] - A[0])
        for j in range(1, m):
            if abs(X[i + j] - A[j]) != const:
                const = -1
                break
        if const != -1:
            num = i + 1
            poses.append(num)

    return poses


def main():
    n = int(input())
    X = list(map(int, input().split()))
    m = int(input())
    A = list(map(int, input().split()))
    print(*shift_search(X, A, n, m))


if __name__ == '__main__':
    main()