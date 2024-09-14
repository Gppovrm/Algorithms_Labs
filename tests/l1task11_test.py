from unittest import TestCase, main
from Laba_1.task11 import knapsack


class Knapsack(TestCase):
    def test_example_1(self):
        w = 10
        n = 3
        wi = [1, 4, 8]
        result = knapsack(w, wi, n)
        self.assertEqual(result, 9)


if __name__ == '__main__':
    main()
