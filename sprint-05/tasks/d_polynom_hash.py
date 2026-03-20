# h(s) = (((s1 * a + s2) * a + s3) * a + ... + sn) mod m
# h(s) = (s1 * a^(n-1) + s2 * a^(n-2) + ... + s_n) mod m
def get_hash(s: str, base: int, mod: int) -> int:
    h = 0
    for ch in s:
        h = (h * base + ord(ch)) % mod
    return h

if __name__ == '__main__':
    a = int(input())  # base
    m = int(input())  # mod
    s = input()
    print(get_hash(s, a, m))