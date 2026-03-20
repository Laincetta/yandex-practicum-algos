if __name__ == '__main__':
    n = int(input())
    groups = [input() for _ in range(n)]
    groups_count = { }
    for group in groups:
        if group not in groups_count:
            groups_count[group] = 0
        groups_count[group] += 1
    for key in groups_count:
        print(key)