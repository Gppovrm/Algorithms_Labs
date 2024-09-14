from unittest import TestCase, main
from Laba_2.task4 import process_commands


class CommP(TestCase):
    def test_example_1(self):
        commands = [
            "+ 1",
            "+ 4",
            "+ 3",
            "+ 3",
            "? 1",
            "? 2",
            "? 3",
            "+ 2",
            "? 3"
        ]
        self.assertEqual(process_commands(commands), [1, 3, 4, 3])


if __name__ == '__main__':
    main()
