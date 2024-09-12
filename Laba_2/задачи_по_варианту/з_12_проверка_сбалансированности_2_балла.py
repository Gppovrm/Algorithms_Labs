class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def add_node(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._add_node(self.root, key)

    def _add_node(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._add_node(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._add_node(node.right, key)

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def balance(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left) if node.left else 0
        right_height = self.height(node.right) if node.right else 0
        return right_height - left_height


with open("input.txt", "r") as in_file, open("output.txt", "w") as out_file:
    n = int(in_file.readline())

    if n == 0:
        out_file.write(str(0))
    else:

        nodes = [int(in_file.readline().split()[0]) for _ in range(n)]

        tree = BST()

        for node in nodes:
            tree.add_node(node)

        queue = [tree.root]
        while queue:
            node = queue.pop(0)
            out_file.write(f"{tree.balance(node)}\n")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

# import random
#
#
# def generate_unbalanced_tree(n):
#     nodes = random.sample(range(-10**9, 10**9), n)
#     random.shuffle(nodes)
#
#     with open('input.txt', 'w') as f:
#         f.write(f"{n}\n")
#         for i in range(n):
#             left = 0
#             right = 0
#             if i + 1 < n:
#                 right = nodes[i + 1]
#             f.write(f"{nodes[i]} {left} {right}\n")
#
# generate_unbalanced_tree(20000)
