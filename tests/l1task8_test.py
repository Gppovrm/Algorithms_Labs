from unittest import TestCase, main
from Laba_1.task8 import max_lectures


class MaxLects(TestCase):

    def test_example_1(self):
        n = 1
        lects = [[5, 10]]
        self.assertEqual(max_lectures(lects), 1)

    def test_example_2(self):
        n = 3
        lects = [[1, 5], [2, 3], [3, 4]]
        self.assertEqual(max_lectures(lects), 2)


if __name__ == '__main__':
    main()
