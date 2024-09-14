from unittest import TestCase, main
from Laba_2.task3 import process_commands


class Comm(TestCase):
    def test_example_1(self):
        commands = [
            "+ 1",
            "+ 3",
            "+ 3",
            "> 1",
            "> 2",
            "> 3",
            "+ 2",
            "> 1"
        ]
        self.assertEqual(process_commands(commands), [3, 3, 0, 2])


if __name__ == '__main__':
    main()
