def bin_search_recursion(n: int, list: list[int], target: int, left: int, right: int) -> int:
    if left > right:
        return -2

    mid = (left + right) // 2
    if list[mid] >= target:
        res = bin_search_recursion(n, list, target, left, mid - 1)
        if res == -2:
            return mid
        else:
            return res
    else:
        return bin_search_recursion(n, list, target, mid + 1, right)


def days_to_buy_bcls(n: int, savings: list[int], s: int) -> list[int]:
    day_number_buy_fst = bin_search_recursion(n, savings, s, 0, n - 1) + 1
    day_number_buy_scnd = bin_search_recursion(n, savings, 2 * s, 0, n - 1) + 1 # +1 добавляем тк номер = индекс + 1
    result = [day_number_buy_fst, day_number_buy_scnd]
    return result

if __name__ == '__main__':
    n = int(input())
    savings = list(map(int, input().split()))
    s = int(input())
    print(*days_to_buy_bcls(n, savings, s))