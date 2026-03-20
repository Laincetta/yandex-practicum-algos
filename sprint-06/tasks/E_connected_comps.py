import sys
sys.setrecursionlimit(10**6)


def edge_list_to_adj_list(edge_list: list[int], nodes_count: int) -> list[int]:
    adj_list = [[] for _ in range(nodes_count)]
    for edge in edge_list:
        from_inx = edge[0] - 1
        to_inx = edge[1] - 1
        adj_list[from_inx].append(to_inx)
        adj_list[to_inx].append(from_inx)

    for i in range(len(adj_list)):
        adj_list[i].sort()

    return adj_list


def depth_first_search(color: list[int], adj_list: list[int], start: int, current_color: str, components: list[list[int]]):
    if color[start] == '-1':
        color[start] = current_color

    for node in adj_list[start]:
        if color[node] == '-1':
            depth_first_search(color, adj_list, node, current_color, components)

    color[start] = current_color

    color_num = int(current_color)
    comp_inx = color_num - 1
    start_inx = start + 1
    components[comp_inx].append(start_inx)

def count_comps(adj_list: list[int], nodes_count: int, search_start: int) -> (int, list[list[int]]):
    color = ['-1'] * nodes_count
    components = []
    current_color = 0
    for i in range(search_start, len(color)):
        if color[i] == '-1':
            current_color += 1
            components.append([])
            string_color = str(current_color)
            depth_first_search(color, adj_list, i, string_color, components)
    return current_color, components


SEARCH_START_INX = 0
def main():
    nodes_count, edges_count = map(int, (input().split()))
    edge_list = [list(map(int, (input().split()))) for _ in range(edges_count)]
    adj_list = edge_list_to_adj_list(edge_list, nodes_count)

    count_connected_comps, connected_comps = count_comps(adj_list, nodes_count, SEARCH_START_INX)
    print(count_connected_comps)
    for comp in connected_comps:
        print(*sorted(comp))


if __name__ == '__main__':
    main()