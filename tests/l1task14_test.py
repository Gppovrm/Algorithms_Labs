from unittest import TestCase, main
from Laba_1.task14 import maxValue


class MaxVal(TestCase):
    def test_example_1(self):
        self.assertEqual(maxValue('1+5'), 6)
    def test_example_2(self):
        self.assertEqual(maxValue('5-8+7*4-8+9'), 200)


if __name__ == '__main__':
    main()
