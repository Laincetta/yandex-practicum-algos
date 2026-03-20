"""
Гоша реализовал структуру данных Дек, максимальный размер которого определяется заданным числом.
Методы push_back(x), push_front(x), pop_back(), pop_front() работали корректно. Но, если в деке было много элементов,
программа работала очень долго. Дело в том, что не все операции выполнялись за O(1). Помогите Гоше! Напишите эффективную
реализацию.
Внимание: при реализации используйте кольцевой буфер.

Формат ввода
В первой строке вводится целое число n — количество команд (1 ≤ n ≤ 100000).
Во второй строке — целое число m — максимальный размер дека (1 ≤ m ≤ 50000).
В следующих n строках идут команды:
- push_back(value) — добавить элемент в конец дека
- push_front(value) — добавить элемент в начало дека
- pop_front() — удалить первый элемент и вывести его
- pop_back() — удалить последний элемент и вывести его
Value — целое число по модулю не превосходящее 1000.

Формат вывода
Для каждой команды pop_front() и pop_back() вывести удалённый элемент.
Если операция push невозможна (дек заполнен) или pop невозможен (дек пуст), вывести "error".
Вывод каждой операции — на отдельной строке.


-- ПРИНЦИП РАБОТЫ --
Я реализовал дек на кольцевом буфере фиксированной длины.

У буфера есть два указателя - head и tail, и два поля:
- size — количество элементов, которые сейчас находятся в деке
- capacity — максимально допустимое количество элементов (размер буфера)

Буфер работает по кольцевому принципу: если tail или head выходит за границы, он оборачивается в начало/конец с помощью операции (индекс % capacity).

head указывает на начало дека (место, откуда удаляются или куда добавляются элементы через push_back/pop_back),
tail — на конец дека (где происходит push_front/pop_front).

Добавление:
- push_front(value): сначала записываем значение по индексу tail, затем двигаем tail вправо (tail + 1) % capacity, и увеличиваем size
- push_back(value): сначала двигаем head влево (head - 1) % capacity, потом записываем по новому индексу и увеличиваем size

Удаление:
- pop_front(): сначала двигаем tail влево (tail - 1) % capacity, выводим элемент из этой ячейки и уменьшаем size
- pop_back(): выводим элемент по индексу head, затем двигаем head вправо (head + 1) % capacity и уменьшаем size

Я вдохновился реализацией очереди на кольцевом буфере из урока 9 второго спринта.


-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Перед каждой операцией я проверяю, можно ли её выполнять: если дек полный - не даю ничего добавлять, если пустой - не даю удалять.
Так что ни выхода за границы, ни обращения к неинициализированным ячейкам быть не может.

Указатели head и tail двигаются с помощью деления по модулю - это гарантирует, что мы всегда остаёмся в пределах допустимых индексов.

head и tail отвечают за разные стороны дека: через head работают push_back и pop_back, через tail - push_front и pop_front.
Каждый из них двигается независимо, в зависимости от операции. Это исключает конфликты и помогает поддерживать правильный порядок элементов.


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Все четыре операции — push_front, push_back, pop_front и pop_back — работают за O(1), потому что не требуют сдвига элементов и не зависят от текущего количества данных в деке.
Добавление - это просто запись по нужному индексу и сдвиг одного указателя (head или tail), что занимает фиксированное количество шагов.
Удаление - это чтение по индексу и тоже сдвиг указателя, без дополнительных действий.
=> общая временная сложность тоже будет O(1)

Реаллокаций и копирований нет, потому что размер буфера фиксированный => амортизированная сложность тоже остаётся O(1) (все операции абсолютно всегда выполняются за O(1))


-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Если в деке находится N элементов, то они хранятся в массиве длины capacity, где capacity в худшем случае = N => O(N)
Кроме этого, храним еще несколько полей: head, tail, size, capacity - они занимают O(1) памяти.
Таким образом, общая пространственная сложность составляет O(N) + O(1) ~ O(N), где N — максимально возможное число элементов в деке.
"""


class DequeError(Exception):
    pass

class DequeIsEmptyError(DequeError):
    pass

class DequeIsFullError(DequeError):
    pass

class Deque:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.deque = [0] * self.capacity
        self.size = 0
        self.head = 0
        self.tail = 0

    @property
    def is_full(self) -> bool:
        return self.size == self.capacity

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    def push_back(self, value: int):
        if self.is_full:
            raise DequeIsFullError
        self.head = (self.head - 1) % self.capacity
        self.deque[self.head] = value
        self.size += 1

    def push_front(self, value: int):
        if self.is_full:
            raise DequeIsFullError
        self.deque[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def pop_front(self) -> int:
        if self.is_empty:
            raise DequeIsEmptyError
        self.tail = (self.tail - 1) % self.capacity
        self.size -= 1
        value = self.deque[self.tail]
        return value

    def pop_back(self) -> int:
        if self.is_empty:
            raise DequeIsEmptyError
        value = self.deque[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    deque = Deque(m)
    for _ in range(n):
        command = input().split()
        try:
            if command[0] == 'push_front':
                value = int(command[1])
                deque.push_front(value)
            elif command[0] == 'push_back':
                value = int(command[1])
                deque.push_back(value)
            elif command[0] == 'pop_front':
                print(deque.pop_front())
            elif command[0] == 'pop_back':
                print(deque.pop_back())
        except DequeError:
            print('error')