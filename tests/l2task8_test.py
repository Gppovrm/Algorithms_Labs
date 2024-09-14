from unittest import TestCase, main
from Laba_2.task8 import get_height


class ReturnH(TestCase):
    def test_example_1(self):
        nodes = [[-2, 0, 2], [8, 4, 3], [9, 0, 0], [3, 6, 5], [6, 0, 0], [0, 0, 0]]

        self.assertEqual(get_height(nodes), 4)


if __name__ == '__main__':
    main()
