def is_subgen(subgen: str, string: str) -> bool:
    i, j = 0, 0
    while i < len(string) and j < len(subgen):
        if string[i] == subgen[j]:
            j += 1
        i += 1

    return j == len(subgen)


if __name__ == '__main__':
    subgen = input()
    string = input()
    print(is_subgen(subgen, string))