def is_more_by_digits(number1: str, number2: str) -> bool: # n1 V n2
    return int(number1 + number2) > int(number2 + number1)


def sort_by_digits(arr: list[str], n: int) -> list[str]:
    for i in range(1, n):
        j = i
        while j > 0 and is_more_by_digits(arr[j], arr[j - 1]):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


def get_biggest_num(numbers: list[str], n: int) -> int:
    numbers = sort_by_digits(numbers, n)
    big_number = int("".join(numbers))
    return big_number

if __name__ == '__main__':
    n = int(input())
    numbers = input().split()
    print(get_biggest_num(numbers, n))