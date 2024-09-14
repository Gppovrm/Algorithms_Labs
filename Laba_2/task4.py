class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

        self.size = 1


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._inserting(self.root, key)

    def _inserting(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                root.left = self._inserting(root.left, key)
        elif key > root.val:
            if root.right is None:
                root.right = Node(key)
            else:
                root.right = self._inserting(root.right, key)
        root.size = 1 + self.get_size(root.left) + self.get_size(root.right)
        return root

    def get_size(self, root):
        if root is None:
            return 0
        return root.size

    def _find_k_node(self, root, k):
        if root is None:
            return 0
        left_size = self.get_size(root.left)
        if k == left_size + 1:
            return root.val
        elif k < left_size + 1:
            return self._find_k_node(root.left, k)
        else:
            return self._find_k_node(root.right, k - left_size - 1)

    def find_k(self, k):
        return self._find_k_node(self.root, k)


def process_commands(operations):
    bst = BST()
    result = []
    for operation in operations:
        if operation.startswith('+'):
            _, x = operation.split()
            bst.insert(int(x))
        elif operation.startswith('?'):
            _, x = operation.split()
            result.append(bst.find_k(int(x)))
    return result


def main():
    with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w',
                                                                      encoding='utf-8') as output_file:
        commands = input_file.readlines()
        result = process_commands(commands)
        for elem in result:
            output_file.write(f'{elem}\n')


if __name__ == '__main__':
    main()
