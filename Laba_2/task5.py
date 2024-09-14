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
            self.inserting(self.root, key)

    def inserting(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                root.left = self.inserting(root.left, key)
        elif key > root.val:
            if root.right is None:
                root.right = Node(key)
            else:
                root.right = self.inserting(root.right, key)
        root.size = 1 + self.get_size(root.left) + self.get_size(root.right)
        return root

    def get_size(self, root):
        if root is None:
            return 0
        return root.size

    def exists_node(self, root, key):
        if root is None:
            return False
        if key == root.val:
            return True
        elif key < root.val:
            return self.exists_node(root.left, key)
        else:
            return self.exists_node(root.right, key)

    def exists(self, key):
        return self.exists_node(self.root, key)

    def next_node(self, root, key):
        if root is None:
            return "none"
        if key < root.val:
            left_next = self.next_node(root.left, key)
            if left_next != "none":
                return left_next
            else:
                return root.val
        else:
            return self.next_node(root.right, key)

    def next(self, key):
        return self.next_node(self.root, key)

    def prev_node(self, root, key):
        if root is None:
            return "none"
        if key > root.val:
            right_prev = self.prev_node(root.right, key)
            if right_prev != "none":
                return right_prev
            else:
                return root.val
        else:
            return self.prev_node(root.left, key)

    def prev(self, key):
        return self.prev_node(self.root, key)

    def find_min(self, root):
        while root.left is not None:
            root = root.left
        return root.val

    def delete_node(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                min_val = self.find_min(root.right)
                root.val = min_val
                root.right = self.delete_node(root.right, min_val)
        if root is not None:
            root.size = 1 + self.get_size(root.left) + self.get_size(root.right)
        return root

    def delete(self, key):
        self.root = self.delete_node(self.root, key)


def process_commands(operations):
    bst = BST()
    ans = []

    for line in operations:
        command, x = line.split()
        if command == "insert":
            bst.insert(int(x))
        elif command == "delete":
            bst.delete(int(x))
        elif command == "exists":
            result = bst.exists(int(x))
            ans.append('true' if result else "false")
            # output_file.write("true\n" if result else "false\n")
        elif command == "next":
            result = bst.next(int(x))
            # output_file.write(f"{result}\n")
            ans.append(f"{result}")
        elif command == "prev":
            result = bst.prev(int(x))
            # output_file.write(f"{result}\n")
            ans.append(f"{result}")
    return ans


def main():
    with open('input.txt', 'r', encoding='utf-8') as input_file, open('output.txt', 'w',
                                                                      encoding='utf-8') as output_file:
        commands = input_file.readlines()
        ans = process_commands(commands)
        for elem in ans:
            output_file.write(f'{elem}\n')


if __name__ == '__main__':
    main()
