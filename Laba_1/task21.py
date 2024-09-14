def function(s1, s2, r):
    my_cards = {'S': [], 'C': [], 'D': [], 'H': []}
    opp_cards = {'S': [], 'C': [], 'D': [], 'H': []}

    for my_card_m_r in s1:
        my_cards[my_card_m_r[1]].append(my_card_m_r[0])

    for oppo_card_m_r in s2:
        opp_cards[oppo_card_m_r[1]].append(oppo_card_m_r[0])

    rank = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    suit = ['S', 'C', 'D', 'H']

    for card in opp_cards[r]:
        for my_card in my_cards[r]:
            if rank.index(my_card) > rank.index(card):
                opp_cards[r].remove(card)
                my_cards[r].remove(my_card)
                break
        if opp_cards[r]:
            return 'NO'
    suit.remove(r)
    for char in suit:
        for card in opp_cards[char]:
            for my_card in my_cards[char]:
                if rank.index(my_card) > rank.index(card):
                    opp_cards[char].remove(card)
                    my_cards[char].remove(my_card)
                    break
            if opp_cards[char]:
                for card in opp_cards[char]:
                    if my_cards[r]:
                        opp_cards[char].remove(card)
                        my_cards[r] = my_cards[r][1:]
                    else:
                        return 'NO'
            if opp_cards[char]:
                return 'NO'

    return 'YES'


def main():
    with open("INPUT.TXT", "r", encoding='utf-8') as input_file, open("OUTPUT.TXT", "w",
                                                                      encoding='utf-8') as output_file:
        n, m, r = [i for i in input_file.readline().split()]
        s1, s2 = input_file.readline().split(), input_file.readline().split()

        result = function(s1, s2, r)
        output_file.write(result)

        # output_file.write(('NO', 'YES')[function(my_cards, opp_cards, r)])


if __name__ == '__main__':
    main()
