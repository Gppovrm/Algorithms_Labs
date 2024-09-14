from unittest import TestCase, main
from Laba_1.task22 import counter


class AttractivePatterns(TestCase):
    def test_example_1(self):
        self.assertEqual(counter(2, 2), 14)

    def test_example_2(self):
        self.assertEqual(counter(3, 3), 322)


if __name__ == '__main__':
    main()
