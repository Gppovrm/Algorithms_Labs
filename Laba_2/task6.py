def is_BST(tree_nodes, i_node, low, high):
    if i_node == -1:
        return True
    if tree_nodes[i_node][0] < low or tree_nodes[i_node][0] > high:
        return False
    return (is_BST(tree_nodes, tree_nodes[i_node][1], low, tree_nodes[i_node][0]) and
            is_BST(tree_nodes, tree_nodes[i_node][2], tree_nodes[i_node][0], high))


def test_is_BST(tree_nodes):
    return 'CORRECT' if len(tree_nodes) == 0 or is_BST(tree_nodes, 0, -2 ** 32, 2 ** 32) else 'INCORRECT'


def main():
    with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w',
                                                                      encoding='utf-8') as output_file:
        n = int(input_file.readline())
        tree_nodes = [list(map(int, input_file.readline().split())) for _ in range(n)]

        output_file.write(test_is_BST(tree_nodes))


if __name__ == '__main__':
    main()
