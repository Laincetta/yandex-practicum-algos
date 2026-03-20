def get_max_grab(gold_heaps: list[tuple[int]], max_weight: int) -> list[int]:
    gold_heaps.sort(key=lambda x: (-x[0]))

    max_grab = 0
    weight_left = max_weight

    for price, weight in gold_heaps:
        if weight_left == 0:
            break

        take = min(weight_left, weight)
        weight_left -= take
        max_grab += price * take

    return max_grab

def main():
    max_weight = int(input())
    n = int(input())
    gold_heaps = [tuple(map(int, input().split())) for _ in range(n)]
    max_grab = get_max_grab(gold_heaps, max_weight)
    print(max_grab)

if __name__ == '__main__':
    main()