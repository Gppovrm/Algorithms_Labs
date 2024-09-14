from unittest import TestCase, main
from Laba_4.task5 import prefix_function


class PrefixFunction(TestCase):
    def test_example_1(self):
        s = 'aaaAAA'
        self.assertEqual(prefix_function(s), [0, 1, 2, 0, 0, 0])

    def test_example_2(self):
        s = 'abacaba'
        self.assertEqual(prefix_function(s), [0, 0, 1, 0, 1, 2, 3])


if __name__ == '__main__':
    main()
