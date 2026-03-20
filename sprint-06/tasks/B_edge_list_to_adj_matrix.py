def edge_list_to_adj_matrix(edge_list: list[int], nodes_count: int) -> list[int]:
    adj_matrix = [[0] * nodes_count for _ in range(nodes_count)]
    for edge in edge_list:
        i_inx = edge[0] - 1
        j_inx = edge[1] - 1
        adj_matrix[i_inx][j_inx] = 1

    return adj_matrix


def main():
    nodes_count, edges_count = map(int, (input().split()))
    edge_list = [list(map(int, (input().split()))) for _ in range(edges_count)]
    matrix = edge_list_to_adj_matrix(edge_list, nodes_count)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=' ')
        print()


if __name__ == '__main__':
    main()