def bin_search(n: int, list: list[int], target: int) -> int:
    result = -2
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if list[mid] >= target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

def days_to_buy_bcls(n: int, savings: list[int], s: int) -> list[int]:
    day_number_buy_fst = bin_search(n, savings, s) + 1
    day_number_buy_scnd = bin_search(n, savings, 2 * s) + 1 # +1 добавляем тк номер = индекс + 1
    result = [day_number_buy_fst, day_number_buy_scnd]
    return result

if __name__ == '__main__':
    n = int(input())
    savings = list(map(int, input().split()))
    s = int(input())
    print(*days_to_buy_bcls(n, savings, s))