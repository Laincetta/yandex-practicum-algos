from collections import defaultdict

def insert_lines(init_line: str, lines: list[tuple[str, int]], n: int) -> str:
    inserts = defaultdict(list)
    for t_i, pos in lines:
        inserts[pos].append(t_i)

    result = []
    for i in range(len(init_line) + 1):
        if i in inserts:
            result.extend(inserts[i])
        if i < len(init_line):
            result.append(init_line[i])
    return ''.join(result)


def main():
    init_line = input().strip()
    n = int(input())
    lines = [input().split() for _ in range(n)]
    for i in range(n):
        lines[i] = (lines[i][0], int(lines[i][1]))
    print(insert_lines(init_line, lines, n))


if __name__ == '__main__':
    main()
