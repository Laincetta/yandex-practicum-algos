def if_equal(string: str, other: str) -> str:
    if len(string) != len(other):
        return 'NO'
    size = len(string)

    statements = {}
    statements_reversed = {}
    for i in range(size):
        if string[i] != other[i]:
            if (string[i] not in statements) and (other[i] not in statements_reversed):
                statements[string[i]] = other[i]
                statements_reversed[other[i]] = string[i]
            else:
                if string[i] in statements and statements[string[i]] != other[i]:
                    return 'NO'
                elif other[i] in statements_reversed and statements_reversed[other[i]] != string[i]:
                    return 'NO'
    return 'YES'


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    print(if_equal(str1, str2))