def print_bubble_sort(n: int, stream: list[int]) -> None:
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if stream[j] > stream[j + 1]:
                stream[j], stream[j + 1] = stream[j + 1], stream[j]
                swapped = True
        if swapped:
            print(*stream)
        else:
            if i == 0:
                print(*stream)
            break

if __name__ == '__main__':
    n = int(input())
    stream = list(map(int, input().split()))
    print_bubble_sort(n, stream)
