from unittest import TestCase, main
from Laba_2.task2 import garland


class Garland(TestCase):
    def test_example_1(self):
        self.assertEqual(garland(8, 15), 9.75)

    def test_example_2(self):
        self.assertEqual(garland(692, 532.81), 446113.34)

    def test_minn(self):
        self.assertEqual(garland(3, 10), 0.0)
    def test_maxx(self):
        self.assertEqual(garland(1000, 1000), 935814.25)

if __name__ == '__main__':
    main()
