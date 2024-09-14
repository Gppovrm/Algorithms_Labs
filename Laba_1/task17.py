def knight_move_number(n: int):
    mod = 10 ** 9
    move = [0, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    for i in range(n - 1):
        move = [
            (move[4] + move[6]) % mod,
            (move[6] + move[8]) % mod,
            (move[7] + move[9]) % mod,
            (move[4] + move[8]) % mod,
            (move[0] + move[3] + move[9]) % mod,
            0,
            (move[0] + move[1] + move[7]) % mod,
            (move[2] + move[6]) % mod,
            (move[1] + move[3]) % mod,
            (move[2] + move[4]) % mod
        ]
    return sum(move) % mod


if __name__ == '__main__':
    with open("input.txt", "r", encoding='utf-8') as input_file, open("output.txt", "w",
                                                                      encoding='utf-8') as output_file:
        n = int(input_file.readline())
        result = knight_move_number(n)
        output_file.write(str(result))
