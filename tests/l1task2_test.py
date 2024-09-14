from unittest import TestCase, main
from Laba_1.task2 import min_refills

class Refills(TestCase):
    def test_example_1(self):
        x = [200, 375, 550, 750]
        d = 950
        m = 400
        n = 4
        result = min_refills(x, d, m, n)
        self.assertEqual(result, 2)

    def test_example_2(self):
        x = [1, 2, 5, 9]
        d = 10
        m = 3
        n = 4
        result = min_refills(x, d, m, n)
        self.assertEqual(result, -1)

    def test_example_3(self):
        x = [100, 150]
        d = 200
        m = 250
        n = 2
        result = min_refills(x, d, m, n)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    main()
