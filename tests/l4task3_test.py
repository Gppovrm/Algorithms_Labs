from unittest import TestCase, main
from Laba_4.task3 import rabin_karp


class FindPatternSrt(TestCase):
    def test_example_1(self):
        p = 'aba'
        t = 'abaCaba'
        self.assertEqual(rabin_karp(p, t), f'2\n1 5')

    def test_example_2(self):
        p = 'Test'
        t = 'testTesttesT'
        self.assertEqual(rabin_karp(p, t), f'1\n5')

    def test_example_3(self):
        p = 'aaaaa'
        t = 'baaaaaaa'
        self.assertEqual(rabin_karp(p, t), f'3\n2 3 4')


if __name__ == '__main__':
    main()
