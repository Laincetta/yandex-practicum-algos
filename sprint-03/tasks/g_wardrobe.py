def count_sort(arr: list[int], n: int, count_colors: int) -> list[int]:
    colors_total = [0 for i in range(count_colors)]
    for color in arr:
        colors_total[color] += 1

    k = 0
    for i in range(len(colors_total)):
        for j in range(colors_total[i]):
            arr[k] = i
            k += 1

    return arr




if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    COUNT_COLORS = 3 # 0, 1, 2
    arr = count_sort(arr, n, COUNT_COLORS)
    print(*arr)