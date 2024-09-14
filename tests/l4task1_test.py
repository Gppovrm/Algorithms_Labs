from unittest import TestCase, main
from Laba_4.task1 import find_pattern_naive


class FindPatternSrt(TestCase):
    def test_example_1(self):
        p = 'aba'
        t = 'abaCaba'
        self.assertEqual(find_pattern_naive(p, t), f'2\n1 5')


if __name__ == '__main__':
    main()
