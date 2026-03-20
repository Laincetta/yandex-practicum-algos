"""
https://contest.yandex.ru/contest/24810/submits/?success=142005866

-- ПРИНЦИП РАБОТЫ --

Я реализовал алгоритм сортировки кучей (heapsort)
Основная идея: сначала из массива строим бинарную кучу (heap),
где самый приоритетный элемент (вершина кучи) — участник с большим числом решённых задач,
меньшим штрафом и лексикографически меньшим логином.

Строим кучу с помощью метода heapify, просеивая элементы вниз (sift_down).
Затем многократно меняем местами корень (самый приоритетный элемент) с последним элементом
текущей кучи и снова восстанавливаем кучу через sift_down от корня до УЖЕ start - i.

В итоге после прохода по всем элементам массив оказывается отсортированным.
Поскольку сортировка выводит элементы у нас в прямом порядке, то для вывода в соответствии с условием,
необходимо вывести все имена участников в обратном порядке. Делаем это с помощью reversed

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

При построении кучи (heapify) гарантируется, что каждый узел больше
своих детей по заданному компаратору. Значит, на корне всегда находится
лучший элемент среди текущей кучи.

На каждом шаге алгоритма мы удаляем корень и помещаем его в конец массива.
После этого восстанавливаем свойство кучи на оставшейся части элементов.

Таким образом, после завершения цикла массив полностью отсортирован по правилам.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

1) Построение кучи через heapify занимает O(N).
2) Каждый из N шагов извлечения корня требует O(log N) операций sift_down.
   Итого O(N log N).

Это и есть итоговая временная сложность алгоритма: O(N log N).
В худшем, среднем и лучшем случае она одинаковая, т.к. каждый элемент
просеивается вниз максимум на высоту дерева.

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

Алгоритм выполняется in-place, то есть использует сам исходный массив
для хранения кучи. Дополнительные структуры данных не создаются.
Используются лишь несколько вспомогательных переменных (индексы, ссылки).

Итого пространственная сложность = O(1). # у нас же рекурсии нет по сути, все итеративно, отсюда и O(1), разве нет?
                                           Но если бы у нас была рекурсивная реализация sift_down и/или heapify, то
                                           было бы O(h) доп памяти, где h = log2(n) => O(log n)
"""

import functools


@functools.total_ordering
class Participant:
    def __init__(self, login: str, problems: int, fine: int):
        self.login = login
        self.problems = problems
        self.fine = fine

    # меньше кортеж = лучше участник
    def __lt__(self, other: "Participant") -> bool:
        return (-self.problems, self.fine, self.login) < (-other.problems, other.fine, other.login)

    def __eq__(self, other: "Participant") -> bool:
        return (self.problems, self.fine, self.login) == (other.problems, other.fine, other.login)


def sift_down(arr: list['Participant'], i: int, n: int) -> None:
    while True:
        best = i
        left = i * 2 + 1
        right = i * 2 + 2

        # "<" = лучше
        if left < n and arr[left] < arr[best]:
            best = left
        if right < n and arr[right] < arr[best]:
            best = right
        if best == i:
            break

        arr[i], arr[best] = arr[best], arr[i]
        i = best


def heapify(arr: list['Participant']) -> None:
    n = len(arr)
    start = n // 2 - 1
    for i in range(start, -1, -1):
        sift_down(arr, i, n)


def heap_sort(arr: list['Participant']) -> None:
    n = len(arr)
    heapify(arr)
    start = n - 1
    for end in range(start, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end)


def main():
    n = int(input())
    participants = [Participant(login, int(p), int(f))
                    for login, p, f in (input().split() for _ in range(n))]

    heap_sort(participants)
    # reversed т.к. сортируем в прямом порядке, а нужен обратный
    for p in reversed(participants):
        print(p.login)


if __name__ == '__main__':
    main()