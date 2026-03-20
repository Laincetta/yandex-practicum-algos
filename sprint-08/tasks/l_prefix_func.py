def prefix_func(string: str):
    prefix_fun = [0 for _ in range(len(string))]
    L = len(prefix_fun)
    prefix = ''
    for i in range(L):
        prefix += string[i]
        eigenprefix = ''
        max_match = 0
        for j in range(len(prefix) - 1):
            eigenprefix += prefix[j]
            if prefix[-j - 1:] == eigenprefix:
                max_match = max(max_match, len(eigenprefix))
                prefix_fun[i] = max_match

    return prefix_fun


def main():
    s_arr = input().strip()
    prefix = prefix_func(s_arr)
    print(*prefix)


if __name__ == '__main__':
    main()