from unittest import TestCase, main
from Laba_2.task16 import process_commands


class KMax(TestCase):
    def test_exaple_1(self):
        commands = [
            "+1 5",
            "+1 3",
            "+1 7",
            "0 1",
            "0 2",
            "0 3",
            "-1 5",
            "+1 10",
            "0 1",
            "0 2",
            "0 3"
        ]
        expected_out = [7,
                        5,
                        3,
                        10,
                        7,
                        3]

        self.assertEqual(process_commands(commands), expected_out)


if __name__ == '__main__':
    main()
