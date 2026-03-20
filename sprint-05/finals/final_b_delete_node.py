"""
https://contest.yandex.ru/contest/24810/submits/?success=142005866

-- ПРИНЦИП РАБОТЫ --

Я реализовал алгоритм удаления узла из бинарного дерева поиска (BST).
Поиск удаляемого узла осуществляется сверху вниз, одновременно
запоминается его родитель (parent). Далее обрабатываем три кейса:

1) детей нет. Заменяем у родителя ссылку на удаляемый узел на null.

2) 1 ребёнок. "Поднимаем" ребёнка на место удаляемого узла:
   у родителя меняем ссылку old -> child (метод replace_child).

3) 2 ребёнка. Берём successor — минимальный узел в правом поддереве (аналогично можно было взять max (predecessor, если
   не ошибаюсь) в левом и менять значение удаляемого узла на него):
       идём в node.right и затем налево до упора. У преемника нет левого ребёнка,
       значит его удаление — кейс 1) или 2) =>:
            копируем значение successor в удаляемый узел (node.value = successor.value);
            удаляем сам successor по алгоритму 1) или 2) в зависимости от наличия правого ребенка


-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --

- В кейсах 1) и 2) мы лишь убираем узел и (при наличии) подвешиваем его единственного ребёнка
  на место x. Порядок ключей сохраняется, так как ребёнок уже удовлетворял ограничениям поддерева x.

- В кейсе 3) мы выбираем successor = min(node.right). По определению у successor
  нет левого ребёнка, его ключ строго больше любого ключа в поддереве node.left и не больше любого ключа в поддереве
  node.right, то есть находится ровно между левым и правым поддеревом node. Копируя значение successor в node,
  мы сохраняем порядок относительно обоих поддеревьев. После этого удаляем successor на его месте:
  это всегда 1)-й или 2)-й кейсы, не затрагивающие остальное дерево => они на корректность BST повлиять не могут


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --

Поиск удаляемого узла — O(h). В кейсах 1) и 2) все сводится к элементарной операции переприсваивания ссылка, что является
операцией за O(1) => O(h) + O(1) = O(h).
В кейсе 3): поиск successor — спуск по левым ссылкам внутри правого поддерева. Это тоже O(h). => O(h) + O(h) = O(2h) = O(h)
Итого в любом случае O(h).


-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --

Алгоритм выполняется in-place. Дополнительная память используется только для нескольких локальных переменных.
Стек вызовов не используется, т.к. реализация у нас не рекурсивная, а итеративная.
=> O(1).
"""


def replace_child(root: 'Node', parent: 'Node', old: 'Node', new: 'Node') -> 'Node':
    if parent is None:
        root = new
    elif parent.left is old:
        parent.left = new
    else:
        parent.right = new
    return root


def remove(root, key) -> 'Node':
    parent = None
    node = root
    while node is not None and node.value != key:
        if key < node.value:
            parent = node
            node = node.left
        else:
            parent = node
            node = node.right

    if node is None:
        return root

    if node.left is None or node.right is None:
        if node.left is not None:
            root = replace_child(root, parent, node, node.left)
        else:
            root = replace_child(root, parent, node, node.right)
        return root

    p_successor = None
    successor = node.right
    while successor.left is not None:
        p_successor = successor
        successor = successor.left

    node.value = successor.value

    if p_successor is None:
        node.right = successor.right
    else:
        p_successor.left = successor.right

    return root