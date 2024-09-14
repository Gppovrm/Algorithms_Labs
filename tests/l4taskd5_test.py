from unittest import TestCase, main
from Laba_4.taskd5 import KMP


class KMPtest(TestCase):
    def test_example_1(self):
        s = 'ababbababa'.strip()
        t = 'aba'.strip()
        result = KMP(s, t)
        expt = [0, 5, 7]
        self.assertEqual(result, expt)


if __name__ == '__main__':
    main()
