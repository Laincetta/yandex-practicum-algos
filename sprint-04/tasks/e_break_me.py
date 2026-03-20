def get_hash(s: str, base: int, mod: int) -> int:
    h = 0
    for ch in s:
        h = (h * base + ord(ch)) % mod
    return h

from itertools import product

alphabet = 'abcdefghijklmnopqrstuvwxyz'
base = 1000
mod = 123987123

hashes = {}

for s in product(alphabet, repeat=6):
    string = ''.join(s)
    h = get_hash(string, base, mod)
    if h in hashes and hashes[h] != string:
        print(f"Collision found:\n 1) {hashes[h]}\n 2) {string}\nHash: {h}")
        break
    hashes[h] = string
else:
    print("No collisions found for length 4")
