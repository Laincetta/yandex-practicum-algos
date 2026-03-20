def sift_down(heap, idx) -> int:
    n = len(heap) - 1
    while idx * 2 <= n:
        left = idx * 2
        right = left + 1

        if right <= n:
            if heap[idx] < max(heap[left], heap[right]):
                if heap[left] > heap[right]:
                    heap[idx], heap[left] = heap[left], heap[idx]
                    idx = left
                else:
                    heap[idx], heap[right] = heap[right], heap[idx]
                    idx = right
            else:
                break
        else:
            if heap[idx] < heap[left]:
                heap[idx], heap[left] = heap[left], heap[idx]
                idx = left
            else:
                break
    return idx


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5


if __name__ == '__main__':
    test()