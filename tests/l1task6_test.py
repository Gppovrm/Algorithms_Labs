from unittest import TestCase, main
from Laba_1.task6 import f_sort


class MaxSalary(TestCase):
    def test_example_1(self):
        self.assertEqual(f_sort(['21', '2'], 2), ['2', '21'])

    def test_example_2(self):
        self.assertEqual(f_sort(['23', '39', '92'], 3), ['92', '39', '23'])


if __name__ == "__main__":
    main()
