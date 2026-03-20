def count_bst(nums: list[int]):
    if len(nums) <= 1:
        return 1

    total_combs = 0
    for root in nums:
        left = [x for x in nums if x < root]
        right = [x for x in nums if x > root]
        combs = count_bst(left) * count_bst(right)
        total_combs += combs
    return total_combs


if __name__ == '__main__':
    n = int(input())
    nums = list(range(1, n+1))
    print(count_bst(nums))