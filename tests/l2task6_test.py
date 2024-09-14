from unittest import TestCase, main
from Laba_2.task6 import test_is_BST


class TestIsBST(TestCase):

    def test_case_1(self):
        tree_nodes = [[2, 1, 2], [1, -1, -1], [3, -1, -1]]
        self.assertEqual(test_is_BST(tree_nodes), 'CORRECT')

    def test_case_2(self):
        tree_nodes = [[1, 1, 2], [2, -1, -1], [3, -1, -1]]
        self.assertEqual(test_is_BST(tree_nodes), 'INCORRECT')

    def test_case_3(self):
        tree_nodes = []
        self.assertEqual(test_is_BST(tree_nodes), 'CORRECT')

    def test_case_4(self):
        tree_nodes = [[1, -1, 1], [2, -1, 2], [3, -1, 3], [4, -1, 4], [5, -1, -1]]
        self.assertEqual(test_is_BST(tree_nodes), 'CORRECT')

    def test_case_5(self):
        tree_nodes = [[4, 1, 2], [2, 3, 4], [6, 5, 6], [1, -1, -1], [3, -1, -1], [5, -1, -1], [7, -1, -1]]
        self.assertEqual(test_is_BST(tree_nodes), 'CORRECT')

    def test_case_6(self):
        tree_nodes = [[4, 1, -1], [2, 2, 3], [1, -1, -1], [5, -1, -1]]
        self.assertEqual(test_is_BST(tree_nodes), 'INCORRECT')


if __name__ == '__main__':
    main()
