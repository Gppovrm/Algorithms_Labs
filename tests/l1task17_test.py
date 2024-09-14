from unittest import TestCase, main
from Laba_1.task17 import knight_move_number


class KnightMove(TestCase):
    def test_example_1(self):
        self.assertEqual(knight_move_number(1), 8)

    def test_example_2(self):
        self.assertEqual(knight_move_number(2), 16)


if __name__ == '__main__':
    main()
