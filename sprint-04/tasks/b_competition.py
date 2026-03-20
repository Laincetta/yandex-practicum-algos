def get_max_segments_len(arr: list[int], n: int) -> int:
    balance = 0
    max_segment_len = 0
    segments = {0: -1}
    for i in range(n):
        balance += arr[i]
        if balance not in segments:
            segments[balance] = i
        else:
            max_segment_len = max(max_segment_len, i - segments[balance])

    return max_segment_len


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    for i in range(n):
        if nums[i] == 0:
            nums[i] = -1
        else:
            nums[i] = 1

    max_len = get_max_segments_len(nums, n)
    print(max_len)