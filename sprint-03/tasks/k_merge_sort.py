def merge(left_arr, right_arr):
    res = []
    i, j = 0, 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            res.append(left_arr[i])
            i += 1
        else:
            res.append(right_arr[j])
            j += 1

    while i < len(left_arr):
        res.append(left_arr[i])
        i += 1

    while j < len(right_arr):
        res.append(right_arr[j])
        j += 1

    return res


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    return merge(left_arr, right_arr)


if __name__ == '__main__':
    print(merge_sort([5, 3, 4, 1, 2]))