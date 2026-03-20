"""
Васе нужно распечатать свой список дел на сегодня. Помогите ему напишите функцию, которая печатает все его дела.
Известно, что дел у Васи не больше 5000.
Внимание в этой задаче не нужно считывать входные данные. Нужно написать только функцию, которая принимает на вход
голову списка и печатает его элементы.

Формат ввода
Длина списка не превосходит 5000 элементов. Список не бывает пустым.

Вы можете ознакомиться с инструкцией по работе с Make на платформе в разделе "Начало тема «Введение в алгоритмы»,
урок «Оптимизация ввода и вывода»

Формат вывода
Функция должна напечатать элементы списка по одному в строке.
"""


import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node: 'Node') -> None:
    cur_node = node
    while cur_node is not None:
        print(cur_node.value)
        cur_node = cur_node.next_item


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    solution(node0)
    # Output is:
    # node0
    # node1
    # node2
    # node3


if __name__ == '__main__':
    test()