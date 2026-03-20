def even_letters_only(s: str) -> str:
    return ''.join(ch for ch in s if (ord(ch) - ord('a') + 1) % 2 == 0)


def main():
    a = input().strip()
    b = input().strip()

    a_even = even_letters_only(a)
    b_even = even_letters_only(b)

    if a_even < b_even:
        print(-1)
    elif a_even > b_even:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
