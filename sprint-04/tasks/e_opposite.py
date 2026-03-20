"""
Вася решил запутать маму —– делать дела в обратном порядке. Список его дел теперь хранится в двусвязном списке.
Напишите функцию, которая вернёт список в обратном порядке.
Внимание: в этой задаче не нужно считывать входные данные. Нужно написать только функцию, которая принимает на
вход голову двусвязного списка и возвращает голову перевёрнутого списка.

Формат ввода
Функция принимает на вход единственный аргумент — голову двусвязного списка.
Длина списка не превосходит 1000 элементов. Список не бывает пустым.

Формат вывода
Функция должна вернуть голову развернутого списка.
"""


import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class DoubleConnectedNode:
        def __init__(self, value, next=None, prev=None):
            self.value = value
            self.next = next
            self.prev = prev


def solution(head: 'Node') -> 'Node':
    new_head = None
    cur_node = head
    while cur_node is not None:
        cur_node.prev, cur_node.next = cur_node.next, cur_node.prev
        new_head = cur_node
        cur_node = cur_node.prev

    return new_head


def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)
    assert new_head is node3
    assert node3.next is node2
    assert node2.next is node1
    assert node2.prev is node3
    assert node1.next is node0
    assert node1.prev is node2
    assert node0.prev is node1


if __name__ == '__main__':
    test()