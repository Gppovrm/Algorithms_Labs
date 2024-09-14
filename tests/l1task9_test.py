from unittest import TestCase, main
from Laba_1.task9 import calculate_tariff


class CalculateTariff(TestCase):
    def test_example_1(self):
        n = 980
        a = [1, 9, 90, 900, 1000, 10000, 10000]
        result = calculate_tariff(n, a)
        self.assertEqual(result, 882)

    def test_example_2(self):
        n = 980
        a = [1, 10, 100, 1000, 900, 10000, 10000]
        result = calculate_tariff(n, a)
        self.assertEqual(result, 900)


if __name__ == '__main__':
    main()
