"""
-- ПРИНЦИП РАБОТЫ --
Сначала выбираем произвольную стартовую вершину (в нашем случае вершину с индексом 0).
Заводим два множества (set):
- added: вершины, которые уже попали в остов,
- not_added: вершины, которые ещё не включены.

Также используем приоритетную очередь, а точнее ее стоковую в Python реализацию heapq (позволит нам сильно сэкономить
время на переборе), куда кладём все рёбра, исходящие из текущего остова.
Так как heapq реализован по принципу min-heap, то заносим веса рёбер с минусом, чтобы доставать (опять с минусом) уже максимальные.

Далее:
- на каждом шаге извлекается ребро с наибольшим весом, которое соединяет остов с новой вершиной,
- новая вершина переносится из not_added в added,
- все рёбра этой вершины помещаются в очередь (кроме тем, которые ведут в вершины из added),
- вес выбранного ребра добавляется к общей сумме.

Так продолжается, пока не будут добавлены все вершины (в этом случае возвращается сумма весов остова), или пока очередь
не опустеет, но вершины ещё остались (в этом случае граф несвязный, и выводится сообщение "Oops! I did it again").


-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Алгоритм всегда поддерживает инвариант: множество вершин added образует связный подграф без циклов, а очередь содержит
рёбра, которые соединяют этот подграф с вершинами вне него.
На каждом шаге выбирается ребро с наибольшим весом среди всех возможных, способных расширить текущее дерево.
Такое ребро гарантированно соединяет остов с новой вершиной и не образует цикл.

После того как все вершины окажутся добавлены, мы получаем дерево, содержащее все вершины графа и имеющее максимальный
суммарный вес. Если же очередь рёбер опустеет раньше, значит граф несвязный и построить остов невозможно.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Сначала мы строим список смежности, что занимает O(E).

Дальнейшая работа идёт в алгоритме Прима. Каждое ребро не более одного раза попадает в очередь и не более одного раза
извлекается из неё -> 2E. Каждая операция вставки или удаления из очереди с приоритетами выполняется за O(log V),
где V - количество вершин.

Таким образом, совокупное время работы алгоритма составляет O(E + 2E * log V) ~ O(E * log V)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Для хранения графа используется список смежности, что занимает O(V + E) памяти.
При чтении входных данных дополнительно хранится список рёбер, что также требует O(E).

В процессе работы алгоритма хранятся:
- очередь рёбер-кандидатов (массив edges) (в худшем случае до O(E)),
- множества добавленных и не добавленных вершин (added, not_added) (O(V) в сумме),
- несколько вспомогательных переменных (O(1)).

Имеем: O(V + E + E + E + V + 1) ~ O(2V + 3E + 1) ~ O(V + E)
"""


import heapq


def edge_list_to_adj_list(edge_list: list[list[int]], nodes_count: int) -> list[int]:
    adj_list = [[] for _ in range(nodes_count)]
    for edge in edge_list:
        from_inx = edge[0] - 1
        to_inx = edge[1] - 1
        weight = edge[2]
        adj_list[from_inx].append((to_inx, weight))
        adj_list[to_inx].append((from_inx, weight))
    return adj_list


def add_vertex(adj_list, not_added, added, edges, cur_inx: int):
    if cur_inx in not_added:
        not_added.remove(cur_inx)
    added.add(cur_inx)

    for to, w in adj_list[cur_inx]:
        if to not in added:
            heapq.heappush(edges, (-w, to))  # -w, т.к. нужен max-heap

    while edges:
        w, v = heapq.heappop(edges)
        if v not in added:
            return v, -w
    return None


def get_max_spanning_tree(adj_list, nodes_count):
    if nodes_count == 1:
        return 0

    not_added = set(range(nodes_count))
    added = set()
    edges = []

    first = add_vertex(adj_list, not_added, added, edges, 0)
    if first is None:
        return "Oops! I did it again"

    sum_weight = 0
    next_to_add, weight = first
    sum_weight += weight

    while not_added and next_to_add is not None:
        res = add_vertex(adj_list, not_added, added, edges, next_to_add)
        if res is None:
            break
        next_to_add, weight = res
        sum_weight += weight

    if len(added) == nodes_count:
        return sum_weight
    return "Oops! I did it again"


def main():
    nodes_count, edges_count = map(int, input().split())
    edge_list = [list(map(int, input().split())) for _ in range(edges_count)]
    adj_list = edge_list_to_adj_list(edge_list, nodes_count)

    max_spanning_tree_weight = get_max_spanning_tree(adj_list, nodes_count)
    print(max_spanning_tree_weight)


if __name__ == '__main__':
    main()
