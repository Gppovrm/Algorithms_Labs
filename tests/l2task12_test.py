from unittest import TestCase, main
from Laba_2.task12 import build_tree_from_list, get_balances


class BalanceTree(TestCase):
    def test_example_1(self):
        nodes = [
            [-2, 0, 2],
            [8, 4, 3],
            [9, 0, 0],
            [3, 6, 5],
            [6, 0, 0],
            [0, 0, 0]
        ]
        expected_out = [3, -1, 0, 0, 0, 0]

        tree = build_tree_from_list(nodes)
        balances = get_balances(tree)

        self.assertEqual(balances, expected_out)


if __name__ == '__main__':
    main()
