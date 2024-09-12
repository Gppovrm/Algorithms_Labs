class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def _add_node(self, node, key):
        if key < node.key:
            if node.left:
                self._add_node(node.left, key)
            else:
                node.left = Node(key)
        else:
            if node.right:
                self._add_node(node.right, key)
            else:
                node.right = Node(key)

    def add_node(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._add_node(self.root, key)

    def height(self, node):
        if not node:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))


with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w',
                                                                  encoding='utf-8') as output_file:
    n = int(input_file.readline().strip())

    nodes = [list(map(int, input_file.readline().strip().split())) for _ in range(n)]
    tree = BST()
    for key, left, right in nodes:
        tree.add_node(key)

    height = tree.height(tree.root)
    output_file.write(str(height))

# import random
# import time
#
# def generate_max_test_case():
#     max_key = 10**9
#     n = int(input())
#     random.seed(time.time())
#
#     with open('input.txt', 'w') as f:
#         f.write(str(n) + '\n')
#         for i in range(n):
#             key = random.randint(-max_key, max_key)
#             left = random.randint(0, n) if i > 0 else 0
#             right = random.randint(0, n) if i > 0 else 0
#             f.write(f"{key} {left} {right}\n")
#
# generate_max_test_case()
