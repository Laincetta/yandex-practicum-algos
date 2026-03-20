def get_flower_beds_squares(flower_beds: list[list[int]]) -> list[list[int]]:
    flower_beds.sort()
    res = []
    start, end = flower_beds[0][0], flower_beds[0][1]
    for cur_start, cur_end in flower_beds[1:]:
        if cur_start <= end:
            end = max(cur_end, end)
        else:
            res.append([start, end])
            start = cur_start
            end = cur_end

    res.append([start, end])

    return res



if __name__ == '__main__':
    n = int(input())
    flower_beds = [list(map(int, input().split())) for _ in range(n)]
    ans = get_flower_beds_squares(flower_beds)
    for i in range(len(ans)):
        print(*ans[i])