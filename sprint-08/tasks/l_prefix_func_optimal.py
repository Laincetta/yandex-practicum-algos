def prefix_function(string: str):
    n = len(string)
    pi = [0] * n
    for i in range(1, n):
        k = pi[i - 1]
        while k > 0 and string[k] != string[i]:
            k = pi[k - 1]
        if string[k] == string[i]:
            k += 1
        pi[i] = k
    return pi



def main():
    s_arr = input().strip()
    prefix = prefix_function(s_arr)
    print(*prefix)


if __name__ == '__main__':
    main()