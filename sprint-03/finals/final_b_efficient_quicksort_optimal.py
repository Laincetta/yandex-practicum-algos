"""
-- ПРИНЦИП РАБОТЫ --
Выбираем опорный элемент (pivot) случайным образом при помощи randint().
Берём два указателя: left слева, right справа.
Двигаем left вправо, пока элемент больше pivot по компаратору.
Двигаем right влево, пока элемент меньше pivot по компаратору.
Когда оба указателя остановились на элементах, стоящих в противоположных нужному порядку — меняем их местами.
Повторяем, пока left не превысит right.
После разделения рекурсивно сортируем левую и правую части.
Так постепенно массив становится отсортированным без дополнительных затрат памяти O(N).

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Pivot делит массив на две части: слева — все "меньше" него, справа — "больше".
Каждая рекурсия уменьшает размер задачи.
В итоге элементы оказываются на своих местах — итоговый массив отсортирован

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
в среднем будем иметь O(N log N): O(N) чтобы пройтись по текущей части массива в каждой итерации,
+ домножим на число разбиений которое равно O(log N) -> O(N) * O(log N) = O(N log N)

В худшем случае, как и в обычной версии quicksort, возможна и O(N^2) в случае если pivot выбирается плохо: крайний слева или
справа элемент

Амортизированная сложность будет O(N log N), т.к. худший случай попадается редко -> O(N^2) невозможна. В среднем за все
время сортировки кол-во операций "разбиения" и "обмена" распределится равномерно -> O(N log N)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Имеем O(1) затрат на дополнительные переменные, операции и т.д. + эти O(1) затрат * на глубину рекурсии т.е. O(log N) в
среднем случае или O(N) в худшем случае (при неудачном pivot на каждом шаге и O(N^2) временной сложности).
=> O(log N) - в среднем
или O(N) в худшем
"""
import functools
from random import randint


@functools.total_ordering
class Participant:
    def __init__(self, login, problems, fine):
        self.login = login
        self.problems = problems
        self.fine = fine

    def __lt__(self, other):
        return (self.problems, -self.fine, other.login) < (other.problems, -other.fine, self.login)

    def __eq__(self, other):
        return (self.problems, self.fine, self.login) == (other.problems, other.fine, other.login)


def partition(participants: list[Participant], pivot: Participant, left: int, right: int) -> tuple[int, int]:
    while left <= right:
        while participants[left] > pivot:
            left += 1
        while pivot > participants[right]:
            right -= 1

        if left <= right:
            participants[left], participants[right] = participants[right], participants[left]
            left += 1
            right -= 1
    return left, right


def efficient_quick_sort(participants: list[Participant], low: int, high: int) -> None:
    if low >= high:
        return

    pivot = participants[randint(low, high)]
    left, right = low, high

    left, right = partition(participants, pivot, left, right)
    efficient_quick_sort(participants, low, right)
    efficient_quick_sort(participants, left, high)


if __name__ == '__main__':
    n = int(input())
    participants = [Participant(login, int(p), int(f)) for login, p, f in (input().split() for _ in range(n))]
    efficient_quick_sort(participants, 0, len(participants) - 1)
    for participant in participants:
        print(participant.login)