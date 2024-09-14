from unittest import TestCase, main
from Laba_4.task6 import z_function


class ZFunction(TestCase):
    def test_example_1(self):
        s = 'aaaAAA'
        self.assertEqual(z_function(s), [2, 1, 0, 0, 0])

    def test_example_2(self):
        s = 'abacaba'
        self.assertEqual(z_function(s), [0, 1, 0, 3, 0, 1])


if __name__ == '__main__':
    main()
