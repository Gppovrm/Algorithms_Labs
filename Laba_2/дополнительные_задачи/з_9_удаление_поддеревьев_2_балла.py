def delete_subtree_node(bst, key):
    try:
        left_k, right_k = bst[key][0], bst[key][1]
        bst.pop(key)
        if left_k is not None:
            delete_subtree_node(bst, left_k)
        if right_k is not None:
            delete_subtree_node(bst, right_k)
    except:
        pass
    return len(bst)


with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w',
                                                                  encoding='utf-8') as output_file:
    n = int(input_file.readline())
    nodes = [[int(i) for i in input_file.readline().split()] for _ in range(n)]
    bst = {}
    for key in nodes:
        left_k, right_k = key[1], key[2]
        if left_k == 0:
            left_k = None
        else:
            left_k = nodes[left_k - 1][0]
        if right_k == 0:
            right_k = None
        else:
            right_k = nodes[right_k - 1][0]
        bst[key[0]] = [left_k, right_k]

    m = int(input_file.readline())
    removes = [int(i) for i in input_file.readline().split()]

    for key in removes:
        output_file.write(f'{delete_subtree_node(bst, key)}\n')
