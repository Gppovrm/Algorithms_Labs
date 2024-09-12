from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

from typing import List


class Node:
    def __init__(self, key: int) -> None:
        self.left = None
        self.right = None
        self.key = key


def in_order(root: Node, file_output) -> None:
    if root:
        in_order(root.left, file_output)
        file_output.write(str(root.key) + ' ')
        in_order(root.right, file_output)


def pre_order(root: Node, file_output) -> None:
    if root:
        file_output.write(str(root.key) + ' ')
        pre_order(root.left, file_output)
        pre_order(root.right, file_output)


def post_order(root: Node, file_output) -> None:
    if root:
        post_order(root.left, file_output)
        post_order(root.right, file_output)
        file_output.write(str(root.key) + ' ')


def build_tree(nodes: List[List[int]]) -> Node:
    tree = [Node(key) for key, _, _ in nodes]
    for i, (key, left, right) in enumerate(nodes):
        if left != -1:
            tree[i].left = tree[left]
        if right != -1:
            tree[i].right = tree[right]
    return tree[0]


def main() -> None:
    with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w',
                                                                      encoding='utf-8') as output_file:
        n = int(input_file.readline().strip())
        nodes = [list(map(int, input_file.readline().split())) for _ in range(n)]

        root = build_tree(nodes)

        in_order(root, output_file)
        output_file.write('\n')
        pre_order(root, output_file)
        output_file.write('\n')
        post_order(root, output_file)
        output_file.write('\n')


