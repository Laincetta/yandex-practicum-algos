"""
Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей. Соседним считается элемент,
находящийся от текущего на одну ячейку влево, вправо, вверх или вниз. Диагональные элементы соседними не считаются.
Например, в матрице A соседними элементами для (0, 0) будут 2 и 0. А для (2, 1) –— 1, 2, 7, 7.

В первой строке задано n — количество строк матрицы. Во второй — количество столбцов m. Числа m и n не превосходят 1000.
В следующих n строках задана матрица. Элементы матрицы — целые числа, по модулю не превосходящие 1000.
В последних двух строках записаны координаты элемента, соседей которого нужно найти. Индексация начинается с нуля.

Напечатайте нужные числа в возрастающем порядке через пробел.
"""


def get_neighbours(matrix: list[list[int]], y: int, x: int) -> list[int]:
    neighbours = []
    height = len(matrix)
    width = len(matrix[0])

    directions = [[-1, 0], [0, -1], [0, 1], [1, 0]] # up, left, right, down

    for dir_y, dir_x in directions:
        new_y = y + dir_y
        new_x = x + dir_x
        if (0 <= new_y <= height - 1) and (0 <= new_x <= width - 1):
            neighbours.append(matrix[y + dir_y][x + dir_x])

    return neighbours


def main() -> None:
    height = int(input())
    width = int(input())

    matrix = [list(map(int, input().split())) for _ in range(height)]

    y = int(input())
    x = int(input())

    for neighbour in sorted(get_neighbours(matrix, y, x)):
        print(neighbour, end=' ')


if __name__ == "__main__":
    main()
