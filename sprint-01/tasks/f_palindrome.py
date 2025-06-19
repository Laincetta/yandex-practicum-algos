"""
Помогите Васе понять, будет ли фраза палиндромом. Учитываются только буквы и цифры, заглавные и строчные буквы
считаются одинаковыми.
Решение должно работать за O(N), где N — длина строки на входе.

В единственной строке записана фраза или слово. Буквы могут быть только латинские. Длина текста не
превосходит 20000 символов.
Фраза может состоять из строчных и прописных латинских букв, цифр, знаков препинания.

Выведите «True», если фраза является палиндромом, и «False», если не является.
"""


def if_palindrome(string: str) -> bool:
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    chars = []

    for char in string:
        char = char.lower()
        if char in alphabet:
            chars.append(char)

    chars = ''.join(chars)
    chars_reverse = ''.join(reversed(chars))
    return chars == chars_reverse


string = input()
print(if_palindrome(string))