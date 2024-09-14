from unittest import TestCase, main
from Laba_2.task5 import process_commands


class CommP(TestCase):
    def test_example_1(self):
        commands = [
            "insert 2",
            "insert 5",
            "insert 3",
            "exists 2",
            "exists 4",
            "next 4",
            "prev 4",
            "delete 5",
            "next 4",
            "prev 4"
        ]
        self.assertEqual(process_commands(commands), ['true', 'false', '5', '3', 'none', '3'])


if __name__ == '__main__':
    main()
