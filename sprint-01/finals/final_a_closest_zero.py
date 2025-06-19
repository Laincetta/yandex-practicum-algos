"""
Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить, имеет длину n, то есть состоит из n
одинаковых идущих подряд участков. Каждый участок либо пустой, либо на нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей на этой улице. Поэтому ему важно для каждого участка знать
расстояние до ближайшего пустого участка. Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.

Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы. Дома в городе Тимофея нумеровались в
том порядке, в котором строились, поэтому их номера на карте никак не упорядочены. Пустые участки обозначены нулями.

Формат ввода
В первой строке дана длина улицы —– n (1 ≤ n ≤ 106). В следующей строке записаны n целых неотрицательных чисел — номера
домов и обозначения пустых участков на карте (нули). Гарантируется, что в последовательности есть хотя бы один ноль.
Номера домов (положительные числа) уникальны и не превосходят 109.

Формат вывода
Для каждого из участков выведите расстояние до ближайшего нуля. Числа выводите в одну строку, разделяя их пробелами.
"""

from typing import List
from math import ceil, floor


def get_distances(plots: List[int], n: int) -> List[int]:
    if n == 1:
        return [0]

    zero_indexes = [-1] * n  # -1 для домов, индекс для нулей
    distances = [0] * n      # результат

    for i in range(n):
        if plots[i] == 0:
            zero_indexes[i] = i

    left = right = first_left = -1

    for i in range(n):
        if zero_indexes[i] != -1:
            left = first_left = zero_indexes[i]
            break

    for i in range(left + 1, n):
        if zero_indexes[i] != -1:
            right = zero_indexes[i]
            distance = right - left

            # Если количество домов между нулями нечётное
            if (distance - 1) % 2 == 1:
                mid = left + distance // 2
                half_dist = distance // 2
                for j in range(half_dist):
                    distances[mid + j] = half_dist - j
                    distances[mid - j] = half_dist - j
            else:
                # Если чётное
                mid_right = left + ceil(distance / 2)
                mid_left = left + floor(distance / 2)
                half_dist = floor(distance / 2)
                for j in range(half_dist):
                    distances[mid_right + j] = half_dist - j
                    distances[mid_left - j] = half_dist - j

            left = right  # Двигаем левый ноль вперёд

    # Заполняем участки слева от самого первого нуля
    if first_left != 0:
        k = 1
        for i in range(first_left - 1, -1, -1):
            distances[i] = k
            k += 1

    # Заполняем участки справа от последнего найденного нуля
    if right != n - 1 and right != -1:
        k = 1
        for i in range(right + 1, n):
            distances[i] = k
            k += 1

    # Если ноль был только один
    if right == -1:
        k = 1
        for i in range(first_left + 1, n):
            distances[i] = k
            k += 1

    return distances


n = int(input())
plots = list(map(int, input().split()))
distances = get_distances(plots, n)

print(*distances)