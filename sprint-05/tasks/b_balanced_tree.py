import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def if_balanced(root):
    if root is None:
        return True, 0

    left_balanced, left_height = if_balanced(root.left)
    right_balanced, right_height = if_balanced(root.right)

    balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
    height = max(left_height, right_height) + 1

    return balanced, height


def solution(root):
    balanced, _ = if_balanced(root)
    return balanced


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == '__main__':
    test()
