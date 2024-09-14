from unittest import TestCase, main
from Laba_1.task1 import knapsack


class Knapsack(TestCase):
    def test_example_1(self):
        n = 3
        w = 50
        items = [[60, 20], [100, 50], [120, 30]]
        result = knapsack(n, w, items)
        # self.assertAlmostEqual(result, 180.0000, places=4)
        self.assertEqual(result, 180.0000)

    def test_example_2(self):
        n = 1
        w = 10
        items = [[500, 30]]
        result = knapsack(n, w, items)
        self.assertAlmostEqual(result, 166.6667, places=4)


if __name__ == '__main__':
    main()
