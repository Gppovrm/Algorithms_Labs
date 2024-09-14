from unittest import TestCase, main
from Laba_4.task2 import tresure_map


class TresureMap(TestCase):
    def test_example_1(self):
        s = 'treasure'
        self.assertEqual(tresure_map(s), 8)
    def test_example_2(self):
        s = 'you will never find the treasure'
        self.assertEqual(tresure_map(s), 146)


if __name__ == '__main__':
    main()
