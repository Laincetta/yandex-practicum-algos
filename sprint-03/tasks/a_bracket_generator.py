def convert_to_psp(n: int, count_open: int, count_close: int, result=None, current_string="") -> list[str]:
    if result is None:
        result = []

    if len(current_string) == 2 * n:
        result.append(current_string)
        return

    if count_open < n:
        convert_to_psp(n, count_open + 1, count_close, result, current_string + '(')

    if count_close < count_open:
        convert_to_psp(n, count_open, count_close + 1, result, current_string + ')')

    return result


if __name__ == '__main__':
    n = int(input())
    for _ in convert_to_psp(n, 0, 0):
        print(_)