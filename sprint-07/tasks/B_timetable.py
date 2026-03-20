def get_time_table(meetings: list[tuple[int]], n: int) -> list[int]:
    meetings.sort(key=lambda x: (x[1], x[0]))

    time_table = []
    last_end = float('-inf')

    for start, end in meetings:
        if start == end or start >= last_end:
            last_end = end
            s = int(start) if start.is_integer() else start
            e = int(end) if end.is_integer() else end
            time_table.append((s, e))

    return time_table

def main():
    n = int(input())
    meetings = [tuple(map(float, input().split())) for _ in range(n)]
    time_table = get_time_table(meetings, n)
    print(len(time_table))
    for start, end in time_table:
        print(start, end)

if __name__ == '__main__':
    main()