from unittest import TestCase, main
from Laba_2.task9 import build_bst, delete_subtree_node


class DelSubTree(TestCase):
    def test_example_1(self):
        nodes = [
            [-2, 0, 2],
            [8, 4, 3],
            [9, 0, 0],
            [3, 6, 5],
            [6, 0, 0],
            [0, 0, 0]
        ]
        bst = build_bst(nodes)
        self.assertEqual(delete_subtree_node(bst, 6), 5)
        self.assertEqual(delete_subtree_node(bst, 9), 4)
        self.assertEqual(delete_subtree_node(bst, 7), 4)
        self.assertEqual(delete_subtree_node(bst, 8), 1)


if __name__ == '__main__':
    main()
