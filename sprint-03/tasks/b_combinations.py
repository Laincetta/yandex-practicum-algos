ALPHABET = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

def get_combs(order: str, N: int, current_str="", result = None) -> list[str]:
    if result is None:
        result = []

    if len(current_str) == N:
        result.append(current_str)
        return

    if len(current_str) < N:
        for ch in ALPHABET[order[0]]:
            get_combs(order[1:], N, current_str + ch, result)

    return result

if __name__ == '__main__':
    order = input()
    print(*get_combs(order, len(order)))