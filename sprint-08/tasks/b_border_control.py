def can_pass(a: str, b: str) -> bool:
    if a == b:
        return True

    la, lb = len(a), len(b)
    if abs(la - lb) > 1:
        return False

    if la == lb:
        diff = 0
        for i in range(la):
            if a[i] != b[i]:
                diff += 1
                if diff > 1:
                    return False
        return True

    if la > lb:
        a, b = b, a
        la, lb = lb, la

    i = j = 0
    diff = 0
    while i < la and j < lb:
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            diff += 1
            if diff > 1:
                return False
            j += 1
    return True


def main():
    a = input().strip()
    b = input().strip()
    print("OK" if can_pass(a, b) else "FAIL")


if __name__ == "__main__":
    main()
