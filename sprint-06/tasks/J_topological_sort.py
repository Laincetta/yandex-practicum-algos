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

topologic_sort = []
def depth_first_search(color: list[int], adj_list: list[int], start: int):
    global topologic_sort
    if color[start] == 'white':
        color[start] = 'grey'

    for node in adj_list[start]:
        if color[node] == 'white':
            depth_first_search(color, adj_list, node)

    color[start] = 'black'
    start_num = start + 1
    topologic_sort.append(start_num)

def main_DFS(adj_list: list[int], nodes_count: int, search_start: int):
    color = ['white'] * nodes_count
    for i in range(search_start, len(color)):
        if color[i] == 'white':
            depth_first_search(color, adj_list, i)


SEARCH_START_INX = 0
def main():
    nodes_count, edges_count = map(int, (input().split()))
    edge_list = [list(map(int, (input().split()))) for _ in range(edges_count)]
    adj_list = edge_list_to_adj_list(edge_list, nodes_count)

    main_DFS(adj_list, nodes_count, SEARCH_START_INX)
    global topologic_sort
    print(*topologic_sort[::-1])


if __name__ == '__main__':
    main()