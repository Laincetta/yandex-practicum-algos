import sys
sys.setrecursionlimit(10**6)


def edge_list_to_adj_list(edge_list: list[int], nodes_count: int) -> list[int]:
    adj_list = [[] for _ in range(nodes_count)]
    for edge in edge_list:
        from_inx = edge[0] - 1
        to_inx = edge[1] - 1
        adj_list[from_inx].append(to_inx)

    for i in range(len(adj_list)):
        adj_list[i].sort()

    return adj_list

timer = -1 # start from zero = inx 0
def depth_first_search(color: list[int], adj_list: list[int], start: int, entry: list[int], leave: list[int]):
    global timer
    if color[start] == 'white':
        color[start] = 'grey'
        timer += 1
        entry[start] = timer

    for node in adj_list[start]:
        if color[node] == 'white':
            depth_first_search(color, adj_list, node, entry, leave)

    timer += 1
    leave[start] = timer
    color[start] = 'black'

def main_DFS(adj_list: list[int], nodes_count: int, search_start: int, entry: list[int], leave: list[int]):
    color = ['white'] * nodes_count
    depth_first_search(color, adj_list, search_start, entry, leave)


START = 0
def main():
    nodes_count, edges_count = map(int, (input().split()))
    edge_list = [list(map(int, (input().split()))) for _ in range(edges_count)]
    adj_list = edge_list_to_adj_list(edge_list, nodes_count)

    entry = [None] * len(adj_list)
    leave = [None] * len(adj_list)
    main_DFS(adj_list, nodes_count, START, entry, leave)

    out = [[None, None] for _ in range(len(adj_list))]

    for i in range(len(entry)):
        out[i][0] = entry[i]

    for i in range(len(leave)):
        out[i][1] = leave[i]

    for tin, tout in out:
        print(tin, tout)


if __name__ == '__main__':
    main()