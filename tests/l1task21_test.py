from unittest import TestCase, main
from Laba_1.task21 import function


class Cards(TestCase):
    def test_example_1(self):
        n, m, r = [i for i in '6 2 C'.split()]
        s1, s2 = 'KD KC AD 7C AH 9C'.split(), '6D 6C'.split()
        result = function(s1, s2, r)
        self.assertEqual(result, 'YES')

    def test_example_2(self):
        n, m, r = [i for i in '4 1 D '.split()]
        s1, s2 = '9S KC AH 7D'.split(), '8D'.split()
        result = function(s1, s2, r)
        self.assertEqual(result, 'NO')
    # def test_example_2(self):
    #     my_cards = {'S': ['9'], 'C': ['K'], 'D': ['A', '8'], 'H': []}
    #     opp_cards = {'S': ['9'], 'C': ['K'], 'D': ['A', '7'], 'H': []}
    #     r = 'D'
    #     result = function(my_cards, opp_cards, r)
    #     self.assertEqual(result, 'NO')


if __name__ == '__main__':
    main()
