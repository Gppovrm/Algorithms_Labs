from unittest import TestCase, main
from Laba_1.task7 import max_shoes_count


class MaxShoesCount(TestCase):
    def test_example_1(self):
        self.assertEqual(max_shoes_count(10, [6, 2, 8]), 2)

    def test_example_2(self):
        self.assertEqual(max_shoes_count(3, [10, 20]), 0)


if __name__ == '__main__':
    main()
