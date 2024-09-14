from unittest import TestCase, main
from Laba_1.task5 import max_prize


class Sweets(TestCase):
    def test_example_1(self):
        self.assertEqual(max_prize(6), [1, 2, 3])

    def test_example_2(self):
        self.assertEqual(max_prize(8), [1, 2, 5])

    def test_example_3(self):
        self.assertEqual(max_prize(2), [2])


if __name__ == '__main__':
    main()
