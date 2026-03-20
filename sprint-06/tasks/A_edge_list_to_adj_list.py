def edge_list_to_adj_list(edge_list: list[int], nodes_count: int) -> list[int]:
    adj_list = [[0, []] for _ in range(nodes_count)]
    for edge in edge_list:
        edge_index = edge[0] - 1
        adj_list[edge_index][0] += 1
        adj_list[edge_index][1].append(edge[1])

    return adj_list


def main():
    nodes_count, edges_count = map(int, (input().split()))
    edge_list = [list(map(int, (input().split()))) for _ in range(edges_count)]
    adj = edge_list_to_adj_list(edge_list, nodes_count)
    for edge in adj:
        if edge[1]:
            print(edge[0], end=' ')
            print(*edge[1])
        else:
            print(edge[0])

if __name__ == '__main__':
    main()