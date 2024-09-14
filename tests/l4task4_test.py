from unittest import TestCase, main
from Laba_4.task4 import func


class SubstringEquality(TestCase):
    def test_example_1(self):
        s = 'trololo'
        q = 4
        input_f = ['0 0 7\n', '2 4 3\n', '3 5 1\n', '1 3 2\n']
        ans = func(s, q, input_f)
        self.assertEqual(ans, ['Yes', 'Yes', 'Yes', 'No'])


if __name__ == '__main__':
    main()
